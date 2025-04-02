# ML Model Prediction API

This is a Flask-based API that serves a machine learning model to make predictions based on user input data. The model uses logistic regression and categorical encoding.

## Features
- Accepts JSON input via POST requests
- Encodes categorical data before feeding it into the model
- Returns predictions in JSON format

## Requirements
Make sure you have Python installed and install the necessary dependencies:

```sh
pip install flask joblib scikit-learn
```

## File Structure
```
.
|-- MLLogistic.joblib   # Pre-trained ML model
|-- app.py              # Flask API

```

## How to Run
1. Ensure that `MLLogistic.joblib` exists in the project directory.
2. Run the Flask server:
   ```sh
   python app.py
   ```
3. The server will start at `http://127.0.0.1:5000/`

## API Endpoint
### **POST /predict**
**Description:** Predict the output based on input data.

#### Request Body (JSON):
```json
{
    "age": 35,
    "job": "technician",
    "marital": "married",
    "education": "secondary",
    "default": "no",
    "housing": "yes",
    "loan": "no"
}
```

#### Response:
```json
{
    "prediction": ["yes|no"]
}
```

## Explanation of Key Functions
- **`encode_category(value, category_list)`**: Converts categorical string values into numerical codes.
- **Flask API routes**:
  - `/predict`: Receives input data, encodes it, and returns a prediction.

## Troubleshooting
- If you get an error related to missing `MLLogistic.joblib`, ensure the trained model is in the project directory.
- If the server doesn't start, verify that Flask is installed (`pip install flask`).
- Ensure that categorical values in the request match the expected values in `category_mappings`.

## Author
Developed by Kasun Kavinda

