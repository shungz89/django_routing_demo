from django.http import Http404
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
}

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 Generic Error")

def num_page_view(request, num_page):
    
    topics_list = list(articles.keys())
    topic = topics_list[num_page]
        
    return HttpResponseRedirect(reverse(f'topic-page', args=[topic]))





