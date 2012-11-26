from django.conf.urls import patterns, url

urlpatterns = patterns('privatemessages.views',
    url(r'^send_message/$', 'send_message_view'),
    url(r'^send_message_api/(?P<thread_id>\d+)/$', 'send_message_api_view'),
    url(r'^chat/(?P<thread_id>\d+)/$', 'chat_view'),
    url(r'^$', 'messages_view'),
)
