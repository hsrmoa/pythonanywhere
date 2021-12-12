from django.contrib import admin
from djangofrontapp.models import DsUser, Post, Tag
# Register your models here.

class adminUser(admin.ModelAdmin):
    list_display = ('id',"password")

admin.site.register(DsUser, adminUser);
admin.site.register(Tag);
admin.site.register(Post);