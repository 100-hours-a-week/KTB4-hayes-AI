from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV,
    train_test_split,
)


x, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=12,
    n_redundant=4,
    n_classes=2,
    random_state=42,
)

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
)

grid_model = RandomForestClassifier(random_state=42)

grid_parameters = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 5, 10],
    "min_samples_split": [2, 5],
}

grid_search = GridSearchCV(
    grid_model,
    grid_parameters,
    cv=5,
    scoring="accuracy",
)

grid_search.fit(x_train, y_train)
grid_accuracy = accuracy_score(y_test, grid_search.predict(x_test))

print("GridSearch 최적 파라미터:", grid_search.best_params_)
print(f"GridSearch 테스트 정확도: {grid_accuracy:.4f}")

random_model = RandomForestClassifier(random_state=42)

random_parameters = {
    "n_estimators": [50, 100, 150, 200, 250],
    "max_depth": [None, 5, 10, 15, 20],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
}

random_search = RandomizedSearchCV(
    random_model,
    random_parameters,
    n_iter=10,
    cv=5,
    scoring="accuracy",
    random_state=42,
)

random_search.fit(x_train, y_train)
random_accuracy = accuracy_score(y_test, random_search.predict(x_test))

print("RandomSearch 최적 파라미터:", random_search.best_params_)
print(f"RandomSearch 테스트 정확도: {random_accuracy:.4f}")
