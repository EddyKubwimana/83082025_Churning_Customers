from django.db import models

class annModel(models.Model):
    '''

    -Model for the second asssignment of our artificial intellegence course
    
    '''
    INTERNET_CHOICES = [
        (0, 'DSL'),
        (1, 'Fiber optic'),
        (2, 'No'),
    ]

    CONTRACT_CHOICES =[
        (0,'Month-to-Month'),
        (1,'One year'),
        (2,'Two year'),
        ]
    

    ONLINESECURITY_CHOICES=[
        (0,'No'),
        (1,'Yes'),
        (2,'No internet service')
    ]

    PAYMENTMETHOD={

        (0,"Electronic check"),
        (1,"Mailed check"),
        (2,"Bank Transfer"),
        (3,"Credit Card"),
    }



    Tenure = models.IntegerField(verbose_name="Tenure")
    TotalCharges = models.FloatField(verbose_name="Total Charges", default=None)
    InternetService = models.IntegerField(verbose_name="Internet Service",choices = INTERNET_CHOICES)
    Contract = models.IntegerField(verbose_name= "Contract",choices =CONTRACT_CHOICES)
    OnlineSecurity = models.IntegerField(verbose_name="Online Security", choices=ONLINESECURITY_CHOICES)
    techSupport = models.IntegerField(verbose_name = "Tech Support", choices = ONLINESECURITY_CHOICES)
    PaymentMethod = models.IntegerField(verbose_name = "Payment Method", choices = PAYMENTMETHOD)
    MonthlyCharges = models.FloatField(verbose_name= "Monthly Charges", default=None)
   Confidence = models.CharField(verbose_name="Confidence",default=None, max_length=10, blank=True)
    Churn = models.CharField(verbose_name="Customer Churn",default=None, max_length=4, blank=True)

    def __str__self():
        return "ann"




