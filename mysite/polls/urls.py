from django.conf.urls.defaults import *
from polls.models import Poll
from django.views.generic import DetailView, ListView


urlpatterns = patterns('',
      url(r'^$', 'index'),
      url(r'^(?P<poll_id>\d+)/$', 'detail'),
      url(r'^(?P<poll_id>\d+)/results/$', 'results'),
      url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)


handler404 = 'polls.views.error404'
handler500 = 'polls.views.error500'