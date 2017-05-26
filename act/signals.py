from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from models import DockerJob, Scheduler



def restart_scheduler():
    """
    helper to restart scheduler, gets called by signals

    :return:
    """
    obj = Scheduler.objects.all()
    for o in obj:
        o.restart = True
        o.save()


@receiver(post_save, sender=DockerJob)
def restart_scheudler_after_creating_job(sender, instance=None, created=False, **kwargs):
    """
    send a signal to the schedulers to restart when a new job is created
    """
    restart_scheduler()


@receiver(post_delete, sender=DockerJob)
def restart_scheduler_after_deleting_job(sender, instance=None, created=False, **kwargs):
    """
    send a signal to the schedulers to restart when a job is deleted
    """
    restart_scheduler()