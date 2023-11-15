# bank-sentinel

## about
An ML-approach to predicting bank failure. A part of the requirements for CPTR 435 Machine lLearning and ECON 328 Money and Banking.

Data is to be retrieved from the FDIC using their BankFind API from https://banks.data.fdic.gov/docs/#/Structure/searchInstitutions

This project is based on work from:

https://doi.org/10.1016/j.ribaf.2017.07.104 - Predicting bank failure: An improvement by implementing a machine-learning approach to classical financial ratios

https://doi.org/10.1016/j.dss.2012.11.015 - Partial Least Square Discriminant Analysis for bankruptcy prediction

https://doi.org/10.1016/j.eswa.2008.01.053 - Effects of feature construction on classification performance: An empirical study in bank failure prediction

## roadmap
Step 1: Develop the API GET calls to pull the required financials from the FDIC database. The features to be used in the model are described in the literature linked above. We can retrieve them by following the guide to variables provided by the FDIC in the risview_properties.yaml file. 

Step 2: Clean and preprocess the data as necessary.

Step 3: Train, test, and evaluate several competing ML models for binary classification.