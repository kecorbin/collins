from django.contrib import admin
from models import Job, Host, Service, SpeedTestResult


class CustomJobAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'type',
                    'processed', 'results',
                    'created', 'modified')
    search_fields = ('id', 'user__username',)

class CustomServiceAdmin(admin.ModelAdmin):
    list_display = ('host', 'protocol', 'port',)


class CustomHostAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip', 'name', 'os', 'lastboot')


class CustomSpeedTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'results',)
    search_fields = ('id', 'user__username',)

admin.site.register(Job, CustomJobAdmin)
admin.site.register(Host, CustomHostAdmin)
admin.site.register(Service, CustomServiceAdmin)
admin.site.register(SpeedTestResult, CustomSpeedTestAdmin)
