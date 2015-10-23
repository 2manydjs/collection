"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import (
        password_reset,
        password_reset_done,
        password_reset_confirm,
        password_reset_complete
)

urlpatterns = patterns('',
                      url(r'^$', 'collection.views.index', name='home'),
                      url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
                      url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
                      url(r'^privatelabels/(?P<slug>[-\w]+)/$', 'collection.views.privatelabel_detail', name='privatelabel_detail'),
                      url(r'^privatelabels/(?P<slug>[-\w]+)/edit/$', 'collection.views.edit_privatelabel', name='edit_privatelabel'),
                      url(r'^accounts/', include('registration.backends.simple.urls')),
                      url(r'^accounts/password_reset/$', password_reset, {'template_name': 'registration/password_reset_form.html'}, name="password_reset"),
                      url(r'^accounts/password_reset/done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name="password_reset_done"),
                      url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'}, name="password_reset_confirm"),
                      url(r'^accounts/password_reset/done/$', password_reset_done, {'template_name': 'registration/password_reset_complete.html'}, name="password_reset_complete"),
                      url(r'^admin/', include(admin.site.urls)),
)
