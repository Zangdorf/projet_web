from django.conf.urls import url
from . import views

app_name = "stock"
urlpatterns = [

    url(r'^$', views.index , name='index'), #'^$' to match root -> '^canelita' para /polls/canelita
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),

    ]
