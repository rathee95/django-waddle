from django.conf.urls import url
from .views import all_questions,add_question, get_questions , show_question_add_form, save_question

urlpatterns = [
    url(r'^all/$',  all_questions),
    url(r'^(?P<id>[0-9]+)/$',get_questions ),
    url(r'^add/$',add_question,name="add-question"),
    url(r'^save/$',save_question, name="save-question"),
]
