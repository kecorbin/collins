from django.contrib import admin
from connect.models import Gateway, Tunnel, CloudServer, ProxyPort
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.admin import TokenAdmin
from guardian.admin import GuardedModelAdmin

class ProxyPortAdmin(admin.ModelAdmin):
    list_display = ('cloudserver', 'proxyport', 'is_active')


class GatewayAdmin(GuardedModelAdmin):
    list_display = ('hostname', 'wanip', 'lanip', 'mac',
                    'version', 'cloudserver', 'upgrade', 'healthy',
                    'modified')
    search_fields = ('hostname',)


class TunnelAdmin(GuardedModelAdmin):
    list_display = ('id', 'user', 'gateway', 'sourceip', 'remotehost',
                    'remoteport', 'proxyport', 'timeout', 'url',
                    'processed', 'created')
    search_fields = ('id', 'user__username',)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'last_login',)


class CustomTokenAdmin(TokenAdmin):
    list_display = ('user', 'key', 'created')
    search_fields = ('user__username',)

# We have to unregister these models so that we can override them
admin.site.unregister(User)
admin.site.unregister(Token)

# Register model admin
admin.site.register(User, CustomUserAdmin)
admin.site.register(Gateway, GatewayAdmin)
admin.site.register(Tunnel, TunnelAdmin)
admin.site.register(CloudServer, admin.ModelAdmin)
admin.site.register(ProxyPort, ProxyPortAdmin)
admin.site.register(Token, CustomTokenAdmin)
