from django.conf.urls import patterns, url

from lecturers import views

urlpatterns = patterns ('',
	url(r'^$', views.lecturer_listing, name='lecturer_listing'),
	url(r'^(\d+)/$', views.lecturer_details, name='lecturer_details'),

)
