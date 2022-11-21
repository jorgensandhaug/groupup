from django.contrib import admin
from .models import InterestGroup, Interest, GroupUp

# Register your models here.


class InterestGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")


class InterestAdmin(admin.ModelAdmin):
    list_display = ["name"]


class GroupUpAdmin(admin.ModelAdmin):
    list_display = ["group1", "group2"]


admin.site.register(InterestGroup, InterestGroupAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(GroupUp, GroupUpAdmin)
