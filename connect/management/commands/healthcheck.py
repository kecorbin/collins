from django.core.management.base import NoArgsCommand
from connect.models import Gateway


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        gws = Gateway.objects.all()
        for gw in gws:
            gw.healthy = False
            gw.save()