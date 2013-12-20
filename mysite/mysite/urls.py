from django.conf.urls import patterns, include, url
from mysite.views import hello,current_time,hours_ahead,html_time,display_meta,show_map,search,weibo,location,test

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^hello/$', hello),
    url('^time/$',current_time),
    url(r'^hour/plus/(\d{1,2})/$',hours_ahead),
    url('^htmltime/$',html_time),                      
    url('^display/$',display_meta),
    url('^show_map/$',show_map),
    url('^search/$',search),
    url('^weibo/$',weibo),
    url('^location/$',location),
    url('^test/$',test),                       
)
