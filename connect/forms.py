from django import forms
from connect.models import Tunnel


class TunnelForm(forms.ModelForm):
    class Meta:
        model = Tunnel
        fields = ['remotehost', 'remoteport', 'timeout']


class ConsoleForm(forms.ModelForm):
    class Meta:
        model = Tunnel
        fields = ['remotehost', 'remoteport', 'timeout', 'proxyport']
