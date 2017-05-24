from django.core.management.base import NoArgsCommand
from connect.models import Gateway as GW


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        gws = GW.objects.all()
        for gw in gws:
            print gw.pubkey
