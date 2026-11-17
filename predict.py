import pickle
import pandas as pd

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'FraudDetection-model.bin'

with open(model_file, 'rb') as f_in:
    preprocessor, model = pickle.load(f_in)

app = Flask('fraud-detection')

@app.route('/predict', methods=['POST'])
def predict():
    transaction = request.get_json()
    df_transaction = pd.json_normalize(transaction)

    X = preprocessor.transform(df_transaction)
    y_pred = model.predict_proba(X)[0, 1]
    fraud = y_pred >= 0.55

    result = {
        'fraud_probability': float(y_pred),
        'fraud': bool(fraud)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)