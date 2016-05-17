"""book_stats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^top10$', views.render_top10),
    url(r'^count$', views.render_word_and_count),
    url(r'^title$', views.render_book_title),
    url(r'^$', views.book_stats),
    url(r'^favicon.ico$', RedirectView.as_view(
        url=staticfiles_storage.url('jokes/favicon.ico'),
        permanent=False),name="favicon"),
]
