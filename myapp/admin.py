from django.contrib import admin
from .models import *


# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    list_display = ["good_id", "good_name"]  # Выводит 2 поля

    # list_display = [field.name for field in Goods._meta.fields]                  # Выводит все поля
    list_filter = ["good_id"]                                                            # Фильтр по поляи

    class Meta:
        model = Goods


class HorseAdmin(admin.ModelAdmin):
    list_display = ["horse_id", "horse_name"]  # Выводит 2 поля

    # list_display = [field.name for field in Goods._meta.fields]                  # Выводит все поля
    # list_filter = ["good_id"]                                                            # Фильтр по поляи

    class Meta:
        model = Horses


class RunAdmin(admin.ModelAdmin):
    # list_display = ["good_id", "good_name"]  # Выводит 2 поля

    # list_display = [field.name for field in Goods._meta.fields]                  # Выводит все поля
    # list_filter = ["good_id"]                                                            # Фильтр по поляи

    class Meta:
        model = Run


class RunsAdmin(admin.ModelAdmin):
    list_display = ["runs_run_id", "runs_horse_id"]  # Выводит 2 поля

    # list_display = [field.name for field in Goods._meta.fields]                  # Выводит все поля

    class Meta:
        model = Runs




admin.site.register(Goods, GoodsAdmin)
admin.site.register(Horses, HorseAdmin)
admin.site.register(Run, RunAdmin)
admin.site.register(Runs, RunsAdmin)
