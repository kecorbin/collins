from django.contrib import admin
from models import Scan, SpeedTest

@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'type',
                    'processed', 'results',
                    'created', 'modified')
    search_fields = ('id', 'user__username',)

@admin.register(SpeedTest)
class SpeedTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'results',)
    search_fields = ('id', 'user__username',)

