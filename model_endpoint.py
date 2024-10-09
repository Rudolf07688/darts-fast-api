from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from darts import TimeSeries
from darts.models import RandomForest  # or any other Darts model you're using
import uvicorn

app = FastAPI()

# Load your pre-trained model
model = RandomForest.load("xgb_model.pkl")

class InputData(BaseModel):
    values: list[float]
    timestamps: list[str]

class ForecastParams(BaseModel):
    horizon: int = 1

@app.post("/predict")
async def predict(request: dict):
    data = InputData(**request['data'])
    params = ForecastParams(**request['params'])
    
    try:
        # Convert input data to Darts TimeSeries
        series = TimeSeries.from_dataframe(
            pd.DataFrame({"value": data.values}, index=pd.to_datetime(data.timestamps, format="%Y-%m-%d"))
        )
        
        # Make prediction
        prediction = model.predict(n=params.horizon, series=series)
        
        # Convert prediction to a list of dictionaries
        forecast_data = [
            {"timestamp": timestamp.strftime("%Y-%m-%d"), "value": float(value)}
            for timestamp, value in zip(prediction.time_index, prediction.values().flatten())
        ]
        
        return {"forecast": forecast_data}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)