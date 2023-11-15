# Churning Customers
Certainly! Below is a basic template for a README file for the given GitHub repository. Feel free to customize it further based on the specifics of your project.

---

# 83082025_Churning_Customers

![Project Logo/Icon/Image (if applicable)](url_to_logo_or_icon)

## Overview

This repository contains the code and resources for the "Churning Customers" project.

## Project Description

Provide a brief description of your project. What problem does it solve? What is its purpose?

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

Dependency used for the implementation of the project:

```bash
# Example installation steps
pip install -r requirements.txt
pip install pandas
pip install tensorflow
pip sklearn
pip install matplotlib
from sklearn
pip install shap
pip install joblib

```

## Usage

- The model we trained is meant to predict if a customer churn or not. It can be used to know based on different factors if the the customer churn or not
- The model takes the following array = ["tenure","TotalCharges","InternetService","Contract","OnlineSecurity","TechSupport","PaymentMethod","MonthlyCharges"]
- The one the model is loaded, it predicts either 1 or 0, 0 being NO, AND 1 Being Yes

```bash

from keras.models import load_model
loaded_model = load_model("/content/drive/MyDrive/IntroAi/finalmodel")
loaded_model.summary() 

```

## Data
The data used for training and testing of the model was borrowed from kaggle on this link : https://www.kaggle.com/datasets/blastchar/telco-customer-churn
the data was cleaned and encoded using pandas factorize method. After being factorized, it was scaled using standard scaler from sklearn.

```bash

from sklearn.preprocessing import StandardScaler

scaled = StandardScaler()

scaledata = scaled.fit_transform(x)

xdata = pd.DataFrame(scaledata, columns = x.columns)

```

## Model Training

Explain how the machine learning model was trained. Include details about the chosen algorithm, hyperparameters, and any cross-validation strategies used.

```bash
# Example training command
python train_model.py --input data/train_data.csv --model_output models/model.pkl
```

## Results

Discuss the results of your project. Include any visualizations, performance metrics, or insights gained from the analysis.

## Contributing

If you'd like to contribute to the project, please follow the guidelines outlined in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

---

Replace the placeholders such as `url_to_logo_or_icon` with actual URLs or relevant content. Add sections or modify content based on the structure and requirements of your project.
