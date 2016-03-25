"""site_fejesp URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Esta é a url geral do projeto. Nela, deve-se apenas importar as urls.py dos Apps instalados
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include("blog.urls", namespace='blog')),
    url(r'^processo_seletivo/', include("processo_seletivo.urls", namespace='processo_seletivo')),
    url(r'^parceiros/', include("parceiros.urls", namespace='parceiros')),
    url(r'^ej/', include("ejs.urls", namespace='ejs')),
]

# Fluxo de informação
# urls -> views -> template (html)
# urls -> views -> models -> views -> template (html)
# urls -> views -> forms -> models -> views -> template (html)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
