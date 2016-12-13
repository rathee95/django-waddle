from django.conf.urls import url
from .views import all_questions 

urlpatterns = [
    url(r'^all/$',  all_questions),
]
