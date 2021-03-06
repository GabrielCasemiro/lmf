"""lmf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^categoria_editorial', views.categoria_editorial, name='editorial'),
    url(r'^categoria_artigos', views.categoria_artigos, name='artigo'),
    url(r'^categoria_destaques', views.categoria_destaques, name='destaque'),
    url(r'^categoria_cursos', views.categoria_cursos, name='curso'),
    url(r'^page/(?P<num>[0-9]+)', views.page),
    url(r'^pesquisa', views.pesquisa, name='pesquisa'),
    url(r'^contato', views.contato, name='contato'),
    url(r'^nosso-time', views.nossotime, name='nossotime'),
    url(r'^membros-antigos', views.membros_antigos, name='membros_antigos'),
    url(r'^galeria', views.galeria, name='galeria'),
    url(r'^mail', views.enviar_email, name='email'),
    url(r'^parceiros', views.parceiros, name='parceiros'),
    url(r'^newsletter', views.newsletter, name='newsletter'),
    url(r'', views.index, name='index'),
]