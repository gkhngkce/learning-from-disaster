# Learning From Disaster
## Purpose
This is a machine learning project for a lesson. Main purpose of the project predict how many people will be survive in a given test data.
## Methods & Approach
I tried 4 diffrent ML models. But decided **Random Forest Classifier** model to get predictions. Also tried 4 diffrent kind of methods to fill missing part of the data and decided on the most basic one which is **mean value**.

# Requirements
Python 3.7 or higher
Jupyter Notebook(Google Colab is used for development. If you are planning to use other IDE or notebooks just do not forget to change path!)

# Libraries
If you want to run project without a notebook you need to install libraries in the requirements.txt

```python
pip install -r requirements.txt
```

# Install
To copy this project to your computer just use the following code or download as zip from Code button

```python
git clone https://github.com/gkhngkce/learning-from-disaster.git
```

After that you can import Jupyter notebook file(titanic_problem.ipynb) to Google colab or your local Jupyter notebook to run.
I also Added the pure pyton code to the project(titanic_problem.py).(Do not forget required libraries)

# Data 
In data folder we have 3 csv file provided from Kaggle.
## Train
train.csv has train data 
## Test
test.csv has test data
## Submission Template
gendersubmission.csv is the template of submission format.


# Run
In Jupyter notebook just push run all button to have output.csv file.
In python you can use 
```python
python titanic_problem.py
```
