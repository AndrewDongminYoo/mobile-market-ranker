"""ranker URL Configuration

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
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from crawler.rank.api2 import api as api_version_2
from crawler.rank.api3 import api as cron_api
from crawler.rank.views import index, rank, redirect_to_rank, privacy
from ranker.settings import STATIC_URL, STATIC_ROOT

urlpatterns = [
                  path("", index),
                  path("rank", redirect_to_rank),
                  path("statistic/<int:following_id>", rank),
                  path('admin/', admin.site.urls),
                  path("v2/", api_version_2.urls),
                  path("cron/", cron_api.urls),
                  path("privacy", privacy),
              ] + static(STATIC_URL, document_root=STATIC_ROOT)
