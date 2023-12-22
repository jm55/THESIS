from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, roc_auc_score
import lightgbm as lgbm
import time
import os

X,y = make_classification(n_samples=78000, n_features=100, n_classes=2, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1)

start_time = time.time()
model = lgbm.LGBMClassifier(boosting_type='gbdt', class_weight='balanced', objective='binary', data_sample_strategy='goss', tree_learner='data', max_depth=100, learning_rate=0.1, n_estimators=100, reg_lambda=1, num_leaves=31, device='gpu', boost_from_average='True', verbose=1, random_state=1, n_jobs=os.cpu_count())
model.fit(X_train, y_train)
end_time = time.time()

print("")
print(f"Model Hyperparameter Configuration: {model.get_params()}")
print("")
print(f"Training Time Elapsed: {end_time-start_time:0.8f}s")
print("")
y_pred = model.predict(X=X_test)
y_true = y_test
print(f"Accuracy: {accuracy_score(y_true, y_pred):0.8f}")
print(f"Precision: {precision_score(y_true, y_pred):0.8f}")
print(f"Recall: {recall_score(y_true, y_pred):0.8f}")
print(f"ROC_AUC: {roc_auc_score(y_true, y_pred):0.8f}")