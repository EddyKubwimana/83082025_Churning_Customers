
## Overview

This repository contains the code and resources for the "Churning Customers" project. 
here is the link to the project deployement 
- deployment link : https://www.agentconnect.live/churn
-  demonstration link video : https://youtu.be/w3ZbO-p9OGE


## Project Description

The project aims to predict if customer has stopped doing business with a company based on some variables

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Training](#model-training)
- [Results](#results)
- [License](#license)

## Installation

Dependency used for the implementation of the project:

```bash
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
- The model takes the following columns from the dataset = tenure,TotalCharges,InternetService,Contract,OnlineSecurity,TechSupport,PaymentMethod,"MonthlyCharges
- After the model is deployed it predicts  the proprability of a customer churn.

```bash

from keras.models import load_model
loaded_model = load_model("/content/drive/MyDrive/IntroAi/finalmodel")
loaded_model.predict([Xtest])

```

## Data
The data used for training and testing of the model was borrowed from kaggle on this link : https://www.kaggle.com/datasets/blastchar/telco-customer-churn
the data was cleaned and encoded using pandas factorize method. After being factorized, it was scaled using standard scaler.

```bash
![visualization](https://example.com/path/to/logo.png)

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

  ```

# Evaluate and print results
```bash

loss, accuracy = model.evaluate(xtest, ytest)
print(f'Test loss: {loss}, Test accuracy: {accuracy}')

```

# Plot the training history
```bash
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()

  ```


The model was trained using artifical neural network with GreadSearch to find the best hyperparamaters .
```bash


```

## Results

After training the model, I was able to achieve the accuracy of 79% and AUC score of 83.4%

## License

This project is licensed under the [MIT License](LICENSE).

---

Thanks !!!!
