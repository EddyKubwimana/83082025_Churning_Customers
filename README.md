## ==================================================================================================
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

Due to how we have many insigificant feature, we trained the model with all independent variables and run the model through shap explainer to find out the 
the feauture that have high importance
- Training of the model with all feautures:
  ```bash
  x = finaldata.drop(["Churn"],axis =1)
  y = finaldata["Churn"]
  xtrain,xtest,ytrain,ytest = train_test_split(xdata,y, test_size = 0.1, random_state =42, stratify= y)
  input_layer = Input(shape=(xtrain.shape[1],))
hidden_layer1 = Dense(12, activation="tanh")(input_layer)
dropout_layer = Dropout(0.5)(hidden_layer1)  
output_layer = Dense(1, activation='sigmoid')(dropout_layer)

model = keras.Model(inputs=input_layer, outputs=output_layer)

model.compile(optimizer=Adamax(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy'])


history = model.fit(xtrain, ytrain, epochs=100, batch_size=21, validation_split=0.2, validation_data=(xtest, ytest))

# Evaluate and print results
loss, accuracy = model.evaluate(xtest, ytest)
print(f'Test loss: {loss}, Test accuracy: {accuracy}')

# Plot the training history
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()

  ```

![Project Logo](https://example.com/path/to/logo.png)


The model was trained using artifical neural network with GreadSearch to find the best hyperparamaters .
```bash


```

## Results

Discuss the results of your project. Include any visualizations, performance metrics, or insights gained from the analysis.

## Contributing

If you'd like to contribute to the project, please follow the guidelines outlined in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

---

Replace the placeholders such as `url_to_logo_or_icon` with actual URLs or relevant content. Add sections or modify content based on the structure and requirements of your project.
