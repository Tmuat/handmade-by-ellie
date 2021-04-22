from django.shortcuts import render, get_object_or_404


from products.models import Product


def all_products(request):
    """
    A view to show all products, including sorting and search queries.
    """

    products = Product.objects.all()

    context = {
        "products": products,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_slug):
    """
    A view to show an individual product from the product slug.
    """

    product = get_object_or_404(Product, slug=product_slug)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
