from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
      url(r'^$', views.index, name='index')
)

handler404 = 'polls.views.error404'