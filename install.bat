echo Installing Graphiz...
start ./Graphiz/readme.txt
start ./Graphiz/graphiz_9.0.exe

echo Installing Python Pre-reqs...
python --version
pip install lightgbm==4.1.0 --force-reinstall
pip install catboost==1.2.2 --force-reinstall
pip install scikit-learn==1.2.1 --force-reinstall
pip install imbalanced-learn==0.11.0 --force-reinstall
pip install pandas==2.0.3 --force-reinstall
pip install yellowbrick==1.5 
pip install statsmodels==0.14.1 
pip install mlxtend 
pip install levenshtein

echo Installing Graphiz for Python
conda install python-graphviz
conda --version