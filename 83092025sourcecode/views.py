from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import customerChurn
from .models import annModel
from . import signals
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.conf import settings
from django.http import HttpResponse
from sklearn.preprocessing import StandardScaler
import joblib 
import os
from keras.models import load_model


#Customer churn view

def churn(request):
    '''

    Tenure = models.IntegerField(verbose_name="Tenure")
    TotalCharges = models.FloatField(verbose_name="Total Charges", default=0.0)
    InternetService = models.CharField(verbose_name="Internet Service",choices = INTERNET_CHOICES)
    Contract = models.CharField(verbose_name= "Contract",choices =CONTRACT_CHOICES)
    OnlineSecurity = models.CharField(verbose_name="Online Security", choices=ONLINESECURITY_CHOICES)
    techSupport = models.CharField(verbose_name = "Tech Support", choices = ONLINESECURITY_CHOICES)
    MonthlyCharges = models.FloatField(verbose_name= "Monthly Charges", default=0.0)

    '''
    # path to the model path
    MODEL_PATH = os.path.join(os.path.dirname(__file__), "finalmodel/")
    SCALER_PATH = os.path.join(os.path.dirname(__file__), "churnscaler.joblib")
    template_name = 'user/ann.html'
    


    if request.method =='POST':
        form = customerChurn(request.POST) 
        if form.is_valid():
            '''

           [["tenure","TotalCharges","InternetService","Contract","OnlineSecurity","TechSupport","PaymentMethod","MonthlyCharges"]]
            
            '''
            Tenure = form.cleaned_data["Tenure"]
            TotalCharges = form.cleaned_data["TotalCharges"]
            InternetService = form.cleaned_data["InternetService"]
            Contract = form.cleaned_data["Contract"]
            OnlineSecurity = form.cleaned_data["OnlineSecurity"]
            techSupport = form.cleaned_data["techSupport"]
            PaymentMethod = form.cleaned_data["PaymentMethod"]
            MonthlyCharges = form.cleaned_data["MonthlyCharges"]

            data = [[Tenure,TotalCharges,InternetService,Contract,OnlineSecurity,techSupport,PaymentMethod,MonthlyCharges]]

            scaler = joblib.load(SCALER_PATH)
            transformed_data = scaler.transform(data)

            model  = load_model(MODEL_PATH)

            value = model.predict(transformed_data)
            print(value[0][0])

            if value[0][0]>0.5:
                prediction_form = customerChurn(initial={'Churn': "Yes"})
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










     
    


   


    
