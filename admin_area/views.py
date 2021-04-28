from django.conf import settings
from django.core.mail import send_mass_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import render_to_string

from checkout.models import Order


@staff_member_required
def admin_home(request):
    """
    A view to return the admin home page.
    """

    if not request.user.is_staff:
        messages.info(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    orders = Order.objects.all().order_by("-date")

    order_count = orders.count()

    completed_order_count = orders.filter(status="complete").count()

    processing_order_count = orders.filter(status="processing").count()

    most_recent_orders = orders[:8]

    context = {
        "orders": most_recent_orders,
        "order_count": order_count,
        "completed_order_count": completed_order_count,
        "processing_order_count": processing_order_count,
    }

    template = "admin_area/admin_home.html"

    return render(request, template, context)


@staff_member_required
def all_orders(request):
    """
    A view to show all orders, including filtering and search queries
    """

    order_page = True
    order_list = Order.objects.all().order_by("-date")
    query = None
    page = request.GET.get("page", 1)

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]

            queries = Q(order_number__icontains=query) | Q(
                full_name__icontains=query
            )
            order_list = order_list.filter(queries)

    paginator = Paginator(order_list, 25)
    num_pages = paginator.num_pages

    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    template_name = "admin_area/admin_orders.html"

    context = {
        "order_page": order_page,
        "orders": orders,
        "num_pages": num_pages,
        "query": query,
    }

    return render(request, template_name, context)


@staff_member_required
def order_detail(request, order_number):
    """
    A view to show individual order details
    """

    order = get_object_or_404(Order, order_number=order_number)

    template = "admin_area/admin_order_detail.html"
    context = {
        "order": order,
    }

    return render(request, template, context)


@staff_member_required
def dispatch_orders(request):
    """
    Change the status of orders to dispatched and send email.
    """
    if request.method == "POST":
        selected = request.POST.get("id-selected")
        ids = selected.split(",")
        email_messages = list()
        for count, order_id in enumerate(ids):
            order = Order.objects.get(id=order_id)
            if order.status == "dispatched" or order.status == "complete":
                pass
            else:
                message_name = str("dispatch_message" + str(count))
                subject = (
                    "Handmade By Ellie Dispatch Notice:"
                    + f"{order.order_number}"
                )
                message = render_to_string(
                    "admin_area/emails/dispatch_email.txt", {"order": order}
                )
                message_name = (
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [order.email],
                )
                email_messages.append(message_name)
        try:
            send_mass_mail(email_messages, fail_silently=False)
            messages.success(request, "Dispatch Emails Sent!")
        except BadHeaderError:
            return HttpResponse("Invalid header found.")

        Order.objects.filter(id__in=ids).update(status="dispatched")

    redirect_url = request.POST.get("redirect_url")

    return redirect(redirect_url)
