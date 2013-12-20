#coding:utf-8
from django.template.loader import get_template
from django.http import HttpResponse,Http404
from django.template import Template,Context
from django.shortcuts import render_to_response
import sys
sys.path.append('/home/awen/weibo/weibo/extract')
import main
import datetime,os

def hello(request):
    return HttpResponse("Hello World")

def current_time(request):
    now = datetime.datetime.now()
    t=Template("<html><body>It is now {{current}}</body></html>")
    html=t.render(Context({'current':now}))
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body>In %s hour,it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)

def html_time(request):
    now = datetime.datetime.now()
    t=get_template('time.html')
    html=t.render(Context({'current':now}))
    return HttpResponse(html)


def display_meta(request):
    values=request.META.items()
    values.sort()
    html=[]
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,v))
    return HttpResponse('<table>%s</table>'%'\n'.join(html))

def show_map(request):
    error=True
    return render_to_response('map.html',{'error':error})

def search(request):
    if 'location' in request.GET:
        message = 'You searched for :%r'%request.GET['location']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def weibo(request):
    if 'location' in request.GET:
        message=request.GET['location']
        main.apply_access_token()
        main.updateweibo(message)
        out="you have update a weibo"
    else:
        out ='please input a weibo'
    return HttpResponse(out)

def location(request):
    if 'location' in request.GET:
        message=request.GET['location']
        main.apply_access_token()
        file_out=main.add_timeline(message)
        dic=main.get_geo(message)
        loc={}
        loc['lat']=dic['latitude']
        loc['longs']=dic['longitude']
        f=open(file_out,'r')
        i=1
        latlong={}
        for line in f.readlines():
            c={}
            c['info']=line.split(';')[-4]
            c['lat']=line.split(';')[-3]
            c['longs']=line.split(';')[-2]
            c['address']=line.split(';')[-2]
            latlong[i]=c
            i +=1
        f.close()
        return render_to_response('map.html',locals())
    else:
        error=True
        return render_to_response('map.html',{'error':error})

def test(request):
    if 'location' in request.GET and request.GET['location']:
       file_name='黑龙江省哈尔滨市南岗区西大直街92号2013-12-03(12:12:1386075113).txt'
       file_path='/home/awen/weibo/weibo/forum/'
       file_dir=file_path+file_name;
       f=open(file_dir,'r')
       i=1
       loc={}
       loc['lat']=44.733438
       loc['long']=116.615019
       latlong={}
       for line in f.readlines():
           c={}
           train=line.split(';')[-4:]
           c['info']=train[0]
           c['lat']=train[1]
           c['longs']=train[2]
           c['address']=train[2]
           latlong[i]=c
           i +=1
       f.close()
       return render_to_response('map.html',locals())
    else:
        error = True
        return render_to_response('map.html',{'error':error})
    
    

        
