from django.db.models.signals import post_save
from django.dispatch import receiver
from models import DockerJob, Scheduler


@receiver(post_save, sender=DockerJob)
def set_scheduler_restart_flag(sender, instance=None, created=False, **kwargs):
    if created:
        print("trying to set restart flag; sender=", sender, "created=", created)
        obj = Scheduler.objects.get(id=1)
        print("Was:", obj.restart)
        Scheduler.objects.select_related().filter(id=1).update(restart=True)
        print("Now:", obj.restart)
