from django import forms
from .models import annModel
from django.db import models

class customerChurn(forms.ModelForm):
    '''

    Tenure = models.IntegerField(verbose_name="Tenure")
    TotalCharges = models.FloatField(verbose_name="Total Charges", default=0.0)
    InternetService = models.CharField(verbose_name="Internet Service",choices = INTERNET_CHOICES)
    Contract = models.CharField(verbose_name= "Contract",choices =CONTRACT_CHOICES)
    OnlineSecurity = models.CharField(verbose_name="Online Security", choices=ONLINESECURITY_CHOICES)
    techSupport = models.CharField(verbose_name = "Tech Support", choices = ONLINESECURITY_CHOICES)
    MonthlyCharges = models.FloatField(verbose_name= "Monthly Charges", default=0.0)

    '''
    
    class Meta:
        model =annModel
        fields = ["Tenure","TotalCharges","InternetService","Contract","OnlineSecurity","techSupport","PaymentMethod","MonthlyCharges","Churn"]












