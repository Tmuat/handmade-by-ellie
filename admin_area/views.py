from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, reverse, get_object_or_404

from checkout.models import Order


@staff_member_required
def admin_home(request):
    """
    A view to return the admin home page.
    """

    if not request.user.is_staff:
        messages.info(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    orders = Order.objects.all().order_by('-date')

    order_count = orders.count()

    completed_order_count = orders. \
        filter(status='complete').count()

    processing_order_count = orders. \
        filter(status='processing').count()

    most_recent_orders = orders[:8]

    context = {
        'orders': most_recent_orders,
        'order_count': order_count,
        'completed_order_count': completed_order_count,
        "processing_order_count": processing_order_count,
    }

    template = 'admin_area/admin_home.html'

    return render(request, template, context)
