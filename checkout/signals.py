from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from checkout.models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the order line item total when we save it.
    """

    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def delete_on_save(sender, instance, **kwargs):
    """
    Delete the order line item total when we save it.
    """

    instance.order.update_total()
