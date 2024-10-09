# Darts FastAPI

## Overview
This repository contains a Python application that uses FastAPI to serve a Darts model. The model is trained using Jupyter Notebooks and can be used for forecasting.

## Features
- FastAPI endpoint for serving the Darts model
- Easy to install dependencies using Poetry
- Example scripts to start the endpoint and test the API

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Rudolf07688/darts-fast-api.git
   cd darts-fast-api
   ```

2. Install the dependencies:
   ```sh
   poetry install --no-root
   ```

## Usage

### Train the Model
To train the model, run:
```sh
python train.py
```
This should produce a new model artifact in the form of a `pkl` file.

### Start the Endpoint
To start the FastAPI endpoint, run:
```sh
python model_endpoint.py
```

### Test the Endpoint
You can test the API by running:
```sh
python call_api.py
```
You should receive a JSON response with forecasted values.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or issues, please open an issue on GitHub.

---

Feel free to add more sections or modify the current ones as needed.
```

You can edit the `README.md` file in the GitHub web interface by navigating to the file and clicking the pencil icon to start editing.