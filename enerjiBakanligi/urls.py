"""enerjiBakanligi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static

from enerjiBakanligi import settings


class HomePageView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        self.template_name = "index.html"
        return context


class Yemek(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(Yemek, self).get_context_data(**kwargs)
        self.template_name = "yemek.html"
        return context


class Doviz(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(Doviz, self).get_context_data(**kwargs)
        self.template_name = "doviz.html"
        return context


class Arac(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(Arac, self).get_context_data(**kwargs)
        self.template_name = "arac.html"
        return context

class Rehber(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(Rehber, self).get_context_data(**kwargs)
        self.template_name = "rehber.html"
        return context

class Hava(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(Hava, self).get_context_data(**kwargs)
        self.template_name = "hava.html"
        return context

class Haberler(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(Haberler, self).get_context_data(**kwargs)
        self.template_name = "haberler.html"
        return context

class Duyurular(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(Duyurular, self).get_context_data(**kwargs)
        self.template_name = "duyurular.html"
        return context


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', HomePageView.as_view(), name='homepage'),
    re_path(r'yemek', Yemek.as_view(), name='yemek'),
    re_path(r'doviz', Doviz.as_view(), name='doviz'),
    re_path(r'arac', Arac.as_view(), name='arac'),
    re_path(r'rehber', Rehber.as_view(), name='rehber'),
    re_path(r'hava', Hava.as_view(), name='hava'),
    re_path(r'haberler', Haberler.as_view(), name='Haberler'),
    re_path(r'duyurular', Duyurular.as_view(), name='duyurular'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.ASSETS_URL, document_root=settings.ASSETS_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
