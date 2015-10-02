"""meridian URL Configuration

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

from django.conf.urls import include, url
from django.contrib import admin
from base import views as base_views
from partner import views as partner_views
from santech import views as santech_views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap

base_urls = [
    url(r'^$', base_views.home, name='home'),
]

partner_urls = [
    url(r'^$', partner_views.index, name='home'),
    url(r'^feature', partner_views.features, name='features'),
    url(r'^pricing', partner_views.pricing, name='pricing'),
    url(r'^services', partner_views.services, name='services'),
    url(r'^contacts', partner_views.contacts, name='contacts'),
    url(r'^equipment', partner_views.equipment, name='equipment'),
    url(r'^company', partner_views.company, name='company'),
    url(r'^workers', partner_views.workers, name='workers'),
]

santech_urls = [
    url(r'^$', santech_views.home, name='home'),
    url(r'^blog/$', santech_views.blog, name='blog'),
    url(r'^blog/article=(?P<article>[0-9]+)/', santech_views.blog_article, name='blog_article'),
    url(r'^pricing/', santech_views.pricing, name='pricing'),
    url(r'^reviews/', santech_views.reviews, name='reviews'),
    url(r'^services/$', santech_views.services, name='services'),
    url(r'^services/article=(?P<article>[0-9]+)/', santech_views.services_article, name='services_article'),
    url(r'^contacts/', santech_views.contacts, name='contacts'),
    url(r'^workers/', santech_views.workers, name='workers'),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(base_urls)),
    url(r'^santech/', include(santech_urls)),
    url(r'^partner/', include(partner_urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='base/robots.txt'), name='robots'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)