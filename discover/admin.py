from django.contrib import admin
from models import Scan, SpeedTest

@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'gateway', 'type',
                    'processed', 'created', 'modified')
    search_fields = ('id', 'user__username', 'gateway')

@admin.register(SpeedTest)
class SpeedTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'gateway', 'processed',
                    'created', 'modified')
    search_fields = ('id', 'user__username', 'gateway')

