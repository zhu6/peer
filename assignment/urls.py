from django.conf.urls import patterns, url

from assignment import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<a_name>\w+)/$', views.home, name='home'),
    url(r'^(?P<a_name>\w+)/(?P<p_name>\w+)/$', views.page, name='page'),
    url(r'^(?P<a_name>\w+)/page/stats/$', views.stats, name='stats'),

    url(r'^(?P<a_name>\w+)/submission$', views.submission, name='submission'),
    url(r'^(?P<a_name>\w+)/submission/(?P<username>\w+)/files$', views.submission_files, name='submission_files'),
    url(r'^(?P<a_name>\w+)/submission/add$', views.submission_add, name='submission_add'),
    url(r'^(?P<a_name>\w+)/submission/(?P<id>[0-9]+)/delete$', views.submission_delete, name='submission_delete'),

    url(r'^(?P<a_name>\w+)/review/(?P<id>[0-9]+)$', views.review, name='review'),
    url(r'^(?P<a_name>\w+)/reviewconvo/(?P<id>[0-9]+)$', views.review_convo, name='review_convo'),
    url(r'^(?P<a_name>\w+)/reviewmenu/1$', views.review_menu, name='review_menu'),


    url(r'^(?P<a_name>\w+)/reviewconvosubmit/(?P<id>[0-9]+)$', views.submit_reviewconvo, name='submit_reviewconvo'),
    url(r'^(?P<a_name>\w+)/reviewconvodelete/(?P<id>[0-9]+)$', views.delete_reviewconvo, name='delete_reviewconvo'),

    url(r'^(?P<a_name>\w+)/reviewscore/(?P<review_id>[0-9]+)/(?P<value>[0-9]+)$', views.submit_reviewscore, name='submit_reviewscore'),
)
