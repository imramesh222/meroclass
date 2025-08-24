from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
from .models import Course

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Course)
def log_course_update(sender, instance, created, **kwargs):
    """
    Logs when a course is created or updated.
    """
    if created:
        logger.info(f"New course created: {instance.title} (ID: {instance.id})")
    else:
        logger.info(f"Course updated: {instance.title} (ID: {instance.id})")
        
        # Log which fields were updated if the instance has a _state attribute
        if hasattr(instance, '_state') and hasattr(instance._state, 'db'):
            db = instance._state.db
            if db:
                old_instance = sender.objects.using(db).get(pk=instance.pk)
                changed_fields = []
                for field in instance._meta.fields:
                    field_name = field.name
                    old_value = getattr(old_instance, field_name)
                    new_value = getattr(instance, field_name)
                    if old_value != new_value:
                        changed_fields.append(f"{field_name}: {old_value} -> {new_value}")
                
                if changed_fields:
                    logger.info(f"Changed fields for course {instance.id}: {', '.join(changed_fields)}")
