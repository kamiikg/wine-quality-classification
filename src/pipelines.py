from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

SEMENTE = 42

pipeline_logistic_regression = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000, class_weight='balanced', random_state=SEMENTE))
])

pipeline_svc = Pipeline([
    ('scaler', StandardScaler()),
    ('model', SVC(kernel='rbf', class_weight='balanced', random_state=SEMENTE))
])

pipeline_random_forest = Pipeline([
    ('model', RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=SEMENTE))
])

pipeline_knn = Pipeline([
    ('scaler', StandardScaler()),
    ('model', KNeighborsClassifier(n_neighbors=5))
])
