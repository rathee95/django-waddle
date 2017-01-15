from django.conf.urls import url
from .views import login , home
urlpatterns = [
    url(r'^login/$', login,name="login"),
    url(r'^(?P<id>\d+)/home/$', home,name ="home"),  

]
