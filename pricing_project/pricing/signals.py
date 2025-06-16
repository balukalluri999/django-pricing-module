from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PricingConfig, ConfigChangeLog
from threading import local

# Thread-local storage for the current user
_user = local()

def set_current_user(user):
    _user.value = user

def get_current_user():
    return getattr(_user, 'value', None)

@receiver(post_save, sender=PricingConfig)
def log_config_save(sender, instance, created, **kwargs):
    action = 'create' if created else 'update'
    ConfigChangeLog.objects.create(
        config=instance,
        action=action,
        performed_by=get_current_user()
    )

@receiver(post_delete, sender=PricingConfig)
def log_config_delete(sender, instance, **kwargs):
    ConfigChangeLog.objects.create(
        config=instance,
        action='delete',
        performed_by=get_current_user()
    )
