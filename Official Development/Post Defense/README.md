# Post Defense

The notebooks under this section are additional tests made in response to the recommended revisions to the study.

## 1. `[OFFICIAL] 8a - Benign Perf Validation (Original).ipynb` & `[OFFICIAL] 8c - Benign Perf Validation (Trojan-Undersampled).ipynb`

These notebooks validate the benign performance of the models to determine as to which clusters (by extension, malware type and family) are the models weak at. This also gives the study a more concrete evidence of the weakpoints of the model where were mainly attributed to the limitations of the dataset. 

## 2. `[OFFICIAL] 8b - Trojan-Undersampling Test.ipynb`

This notebook tests the model by determining if Trojans affect the benign sample performance of the model. The rationale behind this concern, as presented by the Thesis Panel, was that the model 'sees'/misclassifies the benign samples as Trojans due to its prominence among the various malware types found in the dataset.