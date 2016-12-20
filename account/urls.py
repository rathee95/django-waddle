from django.conf.urls import url
from .views import login , home
urlpatterns = [
    url(r'^login/$', login),
    url(r'^home/$', home),  

]
