from flask import Flask, request, jsonify
import joblib

model = joblib.load('MLLogistic.joblib')
joblib.dump(model, 'MLLogistic.joblib')
app = Flask(__name__)

category_mappings = {
    'job': ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management',
            'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'],
    'marital': ['divorced', 'married', 'single'],
    'education': ['primary', 'secondary', 'tertiary', 'unknown'],
    'default': ['no', 'yes'],
    'housing': ['no', 'yes'],
    'loan': ['no', 'yes']
}

# Convert categories to numerical codes
def encode_category(value, category_list):
    if value in category_list:
        return category_list.index(value)
    return -1  # Default for unknown values


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        print(data)
        # Extract and encode input data
        input_data = [
            data['age'],
            encode_category(data['job'], category_mappings['job']),
            encode_category(data['marital'], category_mappings['marital']),
            encode_category(data['education'], category_mappings['education']),
            encode_category(data['default'], category_mappings['default']),
            encode_category(data['housing'], category_mappings['housing']),
            encode_category(data['loan'], category_mappings['loan'])
        ]

        print(input_data)
        # Make prediction
        predictions = model.predict([input_data])
        prediction_list = predictions.tolist()

        print(prediction_list)

        return jsonify({'prediction': prediction_list})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
