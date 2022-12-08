from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article
# from django.utils.translation import gettext as _
from django.conf import settings

# Create your views here.
def index(request, appname, modelname, id):
    if request.method == 'GET':
        obj = Article.objects.all().filter(id = id)
        url = '/admin/'+ appname + '/'+ modelname +'/'+ str(id) +'/change/'
        choices = []
        for i in settings.LANGUAGES:
            choices.append(i[0])
        objectfields = []
        for k in obj[0].title:
            objectfields.append(k)
        # newchoices = settings.LANGUAGES.filter(i)
        newchoices = list(set(choices) - set(objectfields))
        return render(request, 'index.html', {'obj': obj[0], 'url': url, "choices": choices, "newchoices": newchoices})
    else:
        body = request.POST.copy()
        del body['csrfmiddlewaretoken']
        finaldata = {}
        data = {}
        finaldata['default'] = body['default']
        del body['default']
        for i in body:
            data[i] = body[i]
        finaldata['title'] = data
        Article.objects.filter(id = id).update(**finaldata)
        return HttpResponseRedirect('/admin/testapp/article/')

def add(request, appname, modelname):
    if request.method == 'GET':
        # obj = Article.objects.all()[id-1]
        url = '/admin/'+ appname + '/'+ modelname + '/add/'
        choices = []
        for i in settings.LANGUAGES:
            choices.append(i[0])
        return render(request, 'add.html', {'url': url,"choices":choices})
    else:
        body = request.POST.copy()
        del body['csrfmiddlewaretoken']
        finaldata = {}
        data = {}
        finaldata['default'] = body['default']
        del body['default']
        for i in body:
            data[i] = body[i]
        finaldata['title'] = data
        Article.objects.create(**finaldata)
        return HttpResponseRedirect('/admin/testapp/article/')

def delete(request, appname, modelname):
    if request.method == 'GET':
        # obj = Article.objects.all()[id-1]
        url = '/admin/'+ appname + '/'+ modelname + '/delete/'
        # print(type(settings.LANGUAGES[0]))
        # print(settings.LANGUAGES[0])
        return render(request, 'delete.html', {'url': url,"choices":settings.LANGUAGES})
    else:
        # body = request.POST.copy()
        # del body['csrfmiddlewaretoken']
        # finaldata = {}
        # data = {}
        # for i in body:
        #     data[i] = body[i]
        # finaldata['title'] = data
        # finaldata['checking_name'] = '69'
        # print(finaldata)
        # Article.objects.create(**finaldata)
        # print(data, type(data))
        return HttpResponseRedirect('/admin/testapp/article/')