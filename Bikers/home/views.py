from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

"""
class IndexView( generic.ListView ):
    template_name="polls/index.html"
    context_object_name="latest_added_articles_list"

    def get_queryset(self):
        #Return the last published articles
        return Question.objects.filter(
            pub_date__lte=timezone.now() # lte == "Less Than or Equal"
        ).order_by('-pub_date')[:5]
"""
def index(request):
    return HttpResponse(" You are at the home index!")
