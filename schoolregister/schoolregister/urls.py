from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('theme.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^lecturers/', include('lecturers.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
