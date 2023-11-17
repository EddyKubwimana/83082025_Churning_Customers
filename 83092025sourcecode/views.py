from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import customerChurn
from .models import annModel
from . import signals
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import HttpResponse
from sklearn.preprocessing import StandardScaler
import joblib 
import os
from keras.models import load_model


#Customer churn view

def churn(request):
  
    # path to the model path
    MODEL_PATH = os.path.join(os.path.dirname(__file__), "finalmodel/")
    SCALER_PATH = os.path.join(os.path.dirname(__file__), "churnscaler.joblib")
    # template for the view
    template_name = 'user/ann.html'
    


    if request.method =='POST':
        form = customerChurn(request.POST) 
        if form.is_valid():
        
            # cleaning data from the django form
        
            Tenure = form.cleaned_data["Tenure"]
            TotalCharges = form.cleaned_data["TotalCharges"]
            InternetService = form.cleaned_data["InternetService"]
            Contract = form.cleaned_data["Contract"]
            OnlineSecurity = form.cleaned_data["OnlineSecurity"]
            techSupport = form.cleaned_data["techSupport"]
            PaymentMethod = form.cleaned_data["PaymentMethod"]
            MonthlyCharges = form.cleaned_data["MonthlyCharges"]
            
            # Make an array from the cleaned data
            data = [[Tenure,TotalCharges,InternetService,Contract,OnlineSecurity,techSupport,PaymentMethod,MonthlyCharges]]
            
            # loading the scaler
            
            scaler = joblib.load(SCALER_PATH)
            
            #Transforming the data
            transformed_data = scaler.transform(data)
             
            #Loading the model
            model  = load_model(MODEL_PATH)
            
            # predict the propability of churn or not
            value = model.predict(transformed_data)

            if value[0][0]>0.5:
                prediction_form = customerChurn(initial={'Confidence':f"{round(value[0][0],2)*100}",'Churn': "Yes"})
                prediction_form.fields["Tenure"].initial = None
                prediction_form.fields["TotalCharges"].initial = None
                prediction_form.fields["InternetService"].initial = None
                prediction_form.fields["Contract"].initial = None
                prediction_form.fields["OnlineSecurity"].initial = None
                prediction_form.fields["techSupport"].initial = None
                prediction_form.fields["PaymentMethod"].initial = None
                prediction_form.fields["MonthlyCharges"].initial = None
    

                return render(request,template_name,{"form":prediction_form})
            else:

                prediction_form = customerChurn(initial={'Churn': "No"})
                prediction_form.fields["Tenure"].initial = None
                prediction_form.fields["TotalCharges"].initial = None
                prediction_form.fields["InternetService"].initial = None
                prediction_form.fields["Contract"].initial = None
                prediction_form.fields["OnlineSecurity"].initial = None
                prediction_form.fields["techSupport"].initial = None
                prediction_form.fields["PaymentMethod"].initial = None
                prediction_form.fields["MonthlyCharges"].initial = None
                return render(request,template_name,{"form":prediction_form})

    else:
        form = customerChurn()


    return render(request,template_name,{"form":customerChurn()})










     
    


   


    
