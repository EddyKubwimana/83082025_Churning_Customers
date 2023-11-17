from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
 
    path('churn/',user_views.churn, name = 'churn')
]       
  
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
