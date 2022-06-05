from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404,HttpResponseRedirect
from django.urls import reverse



# Create your views here.

articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics': 'Politics Page'
}


 #
 # def simple_view(request):
 #    return HttpResponse('SIMPLE VIEW')

 # def sports_view(request):
 #    return HttpResponse(articles['sports'])
 #
 # def finance_view(request):
 #    return HttpResponse(articles['finance'])

def news_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        # result = 'No Page for that topic!'
        # return HttpResponseNotFound(result)
        raise Http404('404 GENERIC ERROR') # 404.html

def add_view(request,num1,num2):
    add_result = num1 + num2
    result = f"{num1}+{num2} = {add_result}"
    return HttpResponse(str(result))

# domain.com/my_app/0 -----> domain.com.my_app/Sports

def num_page_view(request,num_page):
    topics_list = list(articles.keys()) #['sports','finance','politics']
    topic = topics_list[num_page]
    return HttpResponseRedirect(reverse('topic-page',args=[topic]))
