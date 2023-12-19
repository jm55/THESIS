from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import lightgbm as lgbm
X,y = make_classification(n_samples=78000, n_features=100, n_classes=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
model = lgbm.LGBMClassifier(device="cuda", verbose=1)
model.fit(X_train, y_train)