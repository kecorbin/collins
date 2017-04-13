from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks import execute_job
from models import DockerJob

@receiver(post_save, sender=DockerJob)
def queue_job(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    if created:
        print "new job created"
# {"DockerJob": {"image":"apic-acitoolkit-lint"}
        async = execute_job.delay({"id": instance.pk,
                           "DockerJob": {"image": instance.image}
                           })
        if async.ready():
            print("result is ready: {}".format(async.get()))
        else:
            print("result not ready")

        # profile, new = UserProfile.objects.get_or_create(user=instance)