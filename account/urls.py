from django.conf.urls import url
from .views import login ,logout, home, forget_password, reset_password
urlpatterns = [
    
    url(r'^logout/$',logout,name="logout"),
    url(r'^forgot_password/$',forget_password,name="forgot-password"),
    url(r'^reset/(?P<id>\d+)/(?P<otp>\d{4})/$',reset_password,name="reset-password"),
    url(r'^(?P<id>\d+)/home/$', home,name ="home"),  
]
