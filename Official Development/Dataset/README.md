# Dataset

## 1. Oliveira Dataset Notebook
This notebook conducts the necessary steps for data pre-processing of the dataset to make it suitable for use in ML model training, tuning, and evaluation. Its outputs will be found in the subdirectories of `IB` and `TB`.

## 2. Clustering (Malicious & Benign) Notebooks
This notebook conducts data clustering using the source dataset (i.e., ground truth) for use in dataset analysis. Note that no data clustering will actually occur for benign samples but there is one step from data clustering that needs executing to it. Its outputs will be found in the subdirectory of `Clustering`

## 3. PatternCompare Notebook
This notebook is the implementation of the steps presented in question #3 (*Are there any key similarities or differences between malicious and benign samples in terms of API Call Patterns?*) in the study's Section 4.2.6.

## 4. InstanceCompare Notebook
This notebook is the implementation of the steps presented in question #4 (*Are there any unique indicators to malicious samples in terms of specific API Call(s) alone?*) in the study's Section 4.2.6.

## 5. `api_calls.txt`
This file contains the string equivalent of the integer API Calls of the source dataset. It is used during inverse label encoding in the notebooks in this directory and possibly in other notebooks in other directories as well.