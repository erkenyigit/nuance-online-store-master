from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from product_app.models import Product
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Cart


# Create your views here.
@login_required
def shopping_cart(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'cart/newcart.html', {"cart": cart_obj})


@login_required
def update(request):
    product_id = request.POST.get('product_id')
    # remove_id = request.POST.get('remove_id')
    print(product_id)
    # print(remove_id)
    if product_id is not None:
        try:
            product_object = Product.objects.get(id=product_id)
            print(product_object)
        except Product.DoesNotExist:
            print("This product does not exist!")
            return HttpResponseRedirect(reverse("shopcart"))
        # TODO: Quantity check !
        # try:
        #     product_obj = Product.objects.get(quantity=product_id)
        # except Product.DoesNotExist:
        #     print("This product does not exist!")
        #     return HttpResponseRedirect(reverse("shopcart"))
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_object in cart_obj.products.all():
            print("HEREEEEE")
            cart_obj.products.remove(product_object)
            print("DELETED")
        else:
            print("I am added bro")
            cart_obj.products.add(product_object)
    return HttpResponseRedirect(reverse("shopcart"))


@login_required
def delitem(request):
    product_id = request.POST.get('hope')
    print("why not HEREEEEE")
    print(product_id)
    if product_id is not None:
        product_object = Product.objects.get(id=product_id)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        print(cart_obj)
        if product_object in cart_obj.products.all():
            cart_obj.products.remove(product_object)
    return HttpResponseRedirect(reverse("shopcart"))
