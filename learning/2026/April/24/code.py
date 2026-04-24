"""
Code Explanation:
This script establishes a baseline comparison between raw and engineered datasets using Scikit-Learn's production estimators. It evaluates Linear, Ridge, Lasso, and ElasticNet regressions across varying penalty strengths (alpha) to observe algorithmic convergence and feature selection.
"""

from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

df_raw = pd.read_csv('raw-dataset.csv')
df_engineered = pd.read_csv('engineered-dataset.csv')
datasets = {
    'raw': df_raw,
    'engineered': df_engineered
}

alpha_values = [0.1, 1.0, 10.0, 100.0]

for dataset_name, dataset in datasets.items():
    print(f"Evaluating models on dataset: {dataset_name}")

    X = dataset.drop('EnergyConsumption', axis=1)
    y = dataset['EnergyConsumption']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    for alpha in alpha_values:
        linear = LinearRegression()
        lasso = Lasso(alpha=alpha, max_iter=10000)
        ridge = Ridge(alpha=alpha, max_iter=10000)
        elastic_net = ElasticNet(alpha=alpha, l1_ratio=0.5, max_iter=10000)

        linear.fit(X_train, y_train)
        lasso.fit(X_train, y_train)
        ridge.fit(X_train, y_train)
        elastic_net.fit(X_train, y_train)

        linear_pred = linear.predict(X_test)
        lasso_pred = lasso.predict(X_test)
        ridge_pred = ridge.predict(X_test)
        elastic_net_pred = elastic_net.predict(X_test)

        print(f"Alpha: {alpha}")

        print(f"Linear Coefficients: {linear.coef_}")
        print(f"Linear Intercept: {linear.intercept_}")
        print(f"Linear R²: {r2_score(y_test, linear_pred):.6f}")

        print(f"Lasso Coefficients: {lasso.coef_}")
        print(f"Lasso Intercept: {lasso.intercept_}")
        print(f"Lasso R²: {r2_score(y_test, lasso_pred):.6f}")

        print(f"Ridge Coefficients: {ridge.coef_}")
        print(f"Ridge Intercept: {ridge.intercept_}")
        print(f"Ridge R²: {r2_score(y_test, ridge_pred):.6f}")

        print(f"Elastic Net Coefficients: {elastic_net.coef_}")
        print(f"Elastic Net Intercept: {elastic_net.intercept_}")
        print(f"Elastic Net R²: {r2_score(y_test, elastic_net_pred):.6f}")

