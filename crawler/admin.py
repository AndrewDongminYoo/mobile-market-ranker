from django.contrib import admin

from crawler.forms import AppChoiceField
from crawler.models import Following, App
from crawler.models import OneStoreDL
from crawler.models import Ranked
from crawler.models import TrackingApps


# Register your models here.


@admin.register(Ranked)
class Ranked(admin.ModelAdmin):
    list_display = ["app_name", "rank", "market", "deal_type", "rank_type", "created_at"]


@admin.register(Following)
class Following(admin.ModelAdmin):
    list_display = ["app_name", "created_at"]


@admin.register(App)
class App(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "app_id":
            return AppChoiceField(queryset=App.objects.order_by("app_name").all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



@admin.register(TrackingApps)
class TrackingApps(admin.ModelAdmin):
    list_display = ["app_name", "package_name", "market", "rank", "market", "deal_type", "rank_type", "created_at"]


@admin.register(OneStoreDL)
class OneStoreDL(admin.ModelAdmin):
    list_display = ["app_name", "market_appid", "genre", "downloads", "volume", "released", "created_at"]
