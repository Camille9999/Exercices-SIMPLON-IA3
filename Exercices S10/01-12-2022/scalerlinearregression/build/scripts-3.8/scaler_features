import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder


def scaler_cat(X_train, X_test):
    ohe = OneHotEncoder(sparse=False)
    ohe.fit(X_train)
    return pd.DataFrame(ohe.transform(X_test))

def scaler_num(X_train, X_test, scaler=MinMaxScaler()):
    scaler.fit(X_train)
    return pd.DataFrame(scaler.transform(X_test))

def scaler_features(X_train, X_test):

    X_train_cat = X_train.select_dtypes(include=['category'])
    X_test_cat = X_test.select_dtypes(include=['category'])
    X_test_cat_scaled_df = scaler_cat(X_train_cat, X_test_cat)

    X_train_num = X_train.select_dtypes(include=['float64','int64'])
    X_test_num = X_test.select_dtypes(include=['float64','int64'])
    X_test_num_scaled_df = scaler_num(X_train_num, X_test_num)

    return pd.concat([X_test_cat_scaled_df, X_test_num_scaled_df], axis=1)
