from django.conf.urls import url
from .views import login ,logout, home
urlpatterns = [
    
    url(r'^logout/$',logout,name="logout"),
    url(r'^(?P<id>\d+)/home/$', home,name ="home"),  
]
