import requests


url = 'http://localhost:9696/predict'

transaction = {
    "transaction_id": "20001",
    "amount_usd": 165,
    "merchant_category": "Gift Cards", 
    "card_type": "Visa",
    "auth_method": "No Authentication",
    "channel": "Contactless",
    "device_type": "Android Phone",
    "is_foreign_transaction": "False",
    "hours_since_last_txn": 0.16,
    "txn_count_last_24h": "7",
    "distance_from_home_km": 12.91,
    "card_age_months": 47,
    "customer_age": 20,
    "account_balance_usd": 3810.25,
    "is_new_merchant": "True",
    "used_vpn": "False",
    "ip_country_mismatch": "False",
    "billing_shipping_mismatch": "False",
    "cvv_retry_count": 2,
    "velocity_score": 59.8,
    "time_of_day_hour": 17,
    "day_of_week": "Friday",
    "is_ai_generated_scam_attempt": "False",
    "merchant_risk_score": 57,
    "prior_disputes":0
}


response = requests.post(url, json=transaction).json()
print(response)

if response['fraud'] == True:
    print('Possible Transaction Fraud %s' % transaction['transaction_id'])
else:
    print('Not a Transacion Fraud %s' % transaction['transaction_id'])