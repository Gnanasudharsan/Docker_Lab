# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

if __name__ == '__main__':
    # Load the Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Added modification: shuffle dataset manually
    shuffle_index = np.random.permutation(len(X))
    X, y = X[shuffle_index], y[shuffle_index]

    # Train-test split with changed random_state
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=21
    )

    # Modified model parameters
    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=5,
        random_state=21
    )
    model.fit(X_train, y_train)

    # Save model with new name
    joblib.dump(model, 'iris_model_custom.pkl')

    print("Model training completed — custom version by Gnana!")