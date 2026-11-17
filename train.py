import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold
from sklearn.metrics import (mutual_info_score, accuracy_score,
precision_score, recall_score, f1_score, roc_curve, auc, roc_auc_score,confusion_matrix, ConfusionMatrixDisplay, RocCurveDisplay)
from IPython.display import display
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
pd.set_option('display.max_columns', None)
df = pd.read_csv("credit_card_fraud_2026.csv")
df['day_of_week'] = df['day_of_week'].map({0: 'Sunday',
                                          1: 'Monday',
                                          2: 'Tuesday',
                                          3: 'Wednesday',
                                          4: 'Thursday',
                                          5: 'Friday',
                                          6: 'Saturday'})
categorical = ['merchant_category','card_type','auth_method','channel','device_type','is_foreign_transaction',
              'is_new_merchant', 'used_vpn', 'ip_country_mismatch', 'billing_shipping_mismatch','time_of_day_hour','day_of_week',
              'is_ai_generated_scam_attempt']
numerical = ['amount_usd','hours_since_last_txn','txn_count_last_24h','distance_from_home_km','card_age_months',
            'customer_age', 'account_balance_usd', 'cvv_retry_count', 'velocity_score', 'merchant_risk_score','prior_disputes']
df2 = df.drop(['transaction_id'], axis=1)
df_full_train, df_test = train_test_split(df2, test_size=0.2, random_state=1, stratify = df2['is_fraud'])
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1, stratify = df_full_train['is_fraud'])
y_train = df_train['is_fraud']
y_val = df_val['is_fraud']


preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical)
    ]
)
X_train_final = preprocessor.fit_transform(df_full_train)
X_test_final = preprocessor.transform(df_test)
y_full_train = df_full_train['is_fraud']
y_test = df_test['is_fraud']

model = LogisticRegression(solver='liblinear', C=1.0, random_state=1)
model.fit(X_train_final, y_full_train)

import pickle 

with open('FraudDetection-model.bin', 'wb') as f_out:
    pickle.dump((preprocessor, model), f_out)