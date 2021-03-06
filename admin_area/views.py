from django.conf import settings
from django.core.mail import send_mass_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string

from admin_area.forms import (
    DeliveryFormset,
    DiscountFormset,
    ProductForm,
    ProductStockForm,
)
from checkout.models import Order
from products.models import Product, ProductStock


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
def all_products(request):
    """
    A view to show all products, including filtering and search queries
    """

    product_page = True
    product_list = Product.objects.all().order_by("-active", "name")
    query = None
    page = request.GET.get("page", 1)

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]

            queries = Q(name__icontains=query) | Q(
                category__friendly_name__icontains=query
            )
            product_list = product_list.filter(queries)

    paginator = Paginator(product_list, 10)
    num_pages = paginator.num_pages

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    template_name = "admin_area/admin_products.html"

    context = {
        "product_page": product_page,
        "products": products,
        "num_pages": num_pages,
        "query": query,
    }

    return render(request, template_name, context)


@staff_member_required
def admin_add_product(request):
    """
    A view to add a product in the store.
    """

    if not request.user.is_staff:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        form2 = ProductStockForm(request.POST)

        if form.is_valid() and form2.is_valid():
            instance = form.save(commit=False)
            instance_stock = form2.save(commit=False)
            instance.slug = slugify(instance.name)
            instance.created_by = request.user.email
            instance.updated_by = request.user.email
            instance.category.clear()
            instance.save()
            for cat in form.cleaned_data['category']:
                instance.category.add(cat)
            instance.save()
            instance_stock.product = instance
            instance_stock.save()
            messages.info(request, "Successfully added product!")
            return redirect("admin_products")
        else:
            messages.error(
                request,
                ("Failed to add product. " "Please ensure the form is valid."),
            )
    else:
        form = ProductForm()
        form2 = ProductStockForm()

    template = "admin_area/admin_add_product.html"
    context = {
        "form": form,
        "form2": form2,
    }

    return render(request, template, context)


@staff_member_required
def admin_edit_product(request, product_slug):
    """
    A view to Edit a product in the store.
    """

    if not request.user.is_staff:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, slug=product_slug)
    product_stock = get_object_or_404(ProductStock, product=product)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        form2 = ProductStockForm(request.POST, instance=product_stock)

        if form.is_valid() and form2.is_valid():
            instance = form.save(commit=False)
            if instance.created_by == "":
                instance.created_by = request.user.email
            instance.updated_by = request.user.email
            instance.category.clear()
            for cat in form.cleaned_data['category']:
                instance.category.add(cat)
            instance.save()
            form2.save()
            messages.info(request, "Successfully updated product!")
            return redirect("admin_products")
        else:
            messages.error(
                request,
                (
                    "Failed to update product. "
                    "Please ensure the form is valid."
                ),
            )
    else:
        form = ProductForm(instance=product)
        form2 = ProductStockForm(instance=product_stock)

    template = "admin_area/admin_edit_product.html"
    context = {
        "form": form,
        "form2": form2,
        "product": product,
    }

    return render(request, template, context)


@staff_member_required
def delete_product(request, product_id):
    """
    Delete a product from the store.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.info(request, "Product deleted!")
    return redirect(reverse("admin_products"))


@staff_member_required
def admin_edit_delivery(request):
    """
    A view to Edit delivery options.
    """

    if not request.user.is_staff:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        formset = DeliveryFormset(request.POST)
        if formset.is_valid():
            forms = formset.save(commit=False)
            for instance in forms:
                if instance.created_by == "":
                    instance.created_by = request.user.email
                instance.updated_by = request.user.email
            formset.save()
            messages.info(request, "Successfully updated delivery!")
            return redirect(reverse("admin_edit_delivery"))
        else:
            messages.error(
                request,
                (
                    "Failed to update delivery. "
                    "Please ensure the form is valid."
                ),
            )
    else:
        formset = DeliveryFormset()

    template = "admin_area/admin_delivery.html"
    context = {
        "formset": formset,
    }

    return render(request, template, context)


@staff_member_required
def admin_edit_discount(request):
    """
    A view to Edit discount codes.
    """

    if not request.user.is_staff:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        formset = DiscountFormset(request.POST)
        if formset.is_valid():
            forms = formset.save(commit=False)
            for instance in forms:
                if instance.created_by == "":
                    instance.created_by = request.user.email
                if instance.expiry:
                    instance.set_expiry = True
                if instance.quantity:
                    instance.set_quantity = True
            formset.save()
            messages.info(request, "Successfully updated discount codes!")
            return redirect(reverse("admin_edit_discount"))
        else:
            messages.error(
                request,
                (
                    "Failed to update discount codes. "
                    "Please ensure the form is valid."
                ),
            )
    else:
        formset = DiscountFormset()

    template = "admin_area/admin_discount.html"
    context = {
        "formset": formset,
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


@staff_member_required
def complete_orders(request):
    """
    Change the status of orders to complete.
    """

    if request.method == "POST":
        selected = request.POST.get("id-selected")
        ids = selected.split(",")
        Order.objects.filter(id__in=ids).update(status="complete")
        messages.success(request, "Order/s marked as complete!")

    redirect_url = request.POST.get("redirect_url")

    return redirect(redirect_url)
