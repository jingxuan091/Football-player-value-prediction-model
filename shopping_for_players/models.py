from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import LinearRegression
from sklearn.metrics import mean_squared_error

class GBR:
    def __init__(self, n_estimators=100, max_depth=3, learning_rate=0.1):
        self.model = GradientBoostingRegressor(
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
