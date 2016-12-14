from django.conf.urls import url
from .views import all_questions, get_questions 

urlpatterns = [
    url(r'^all/$',  all_questions),
    url(r'^(?P<id>[0-9]+)/$',get_questions )
]
