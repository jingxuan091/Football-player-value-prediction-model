import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
import pickle




def create_LR():
    model = LinearRegression()
    return model

def create_GBR(n_estimators=100, max_depth=3, learning_rate=0.1):
    model = GradientBoostingRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        learning_rate=learning_rate
    )
    return model


def train_model(model, X, y):
   # X = training_data.drop(columns=['market_value_in_eur'])
   # y = training_data['market_value_in_eur']
    model.fit(X, y)
    with open('trained_model.pkl', 'wb') as f:
        trained_model = pickle.dump(model,f)
    return trained_model


def prediction(X):

    # Load the trained model from the file
    with open('trained_model.pkl', 'rb') as f:
        trained_model = pickle.load(f)

    # Use the trained model to make predictions on new data
    predictions = trained_model.predict(X)

    # Print the predictions
    return predictions







"""
old piece of code. You never know...

def make_predictions(data,model):
    print ("Hello! I am an empty prediction function.\nI am looking for my purpose in life!")



class Linear:
    def __init__(self, n_estimators=100, max_depth=3, learning_rate=0.1):
        self.model = LinearRegression(
            n_estimators=n_estimators,
            max_depth=max_depth,
            learning_rate=learning_rate
        )

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        return mse

class Linear_mae:
    def __init__(self, n_estimators=100, max_depth=3, learning_rate=0.1):
        self.model = LinearRegression(
            n_estimators=n_estimators,
            max_depth=max_depth,
            learning_rate=learning_rate
        )

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        return mae
"""
