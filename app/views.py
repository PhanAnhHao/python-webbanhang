from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def contact(req):
    if req.user.is_authenticated:
        customer = req.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {
            'get_cart_items': 0, 
            'get_cart_total': 0
            }
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub = False)
    context = {
        'items': items, 
        'order': order, 
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login,
        'categories': categories
        }
    return render(req, 'app/contact.html', context)

def detail(req):
    if req.user.is_authenticated:
        customer = req.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {
            'get_cart_items': 0, 
            'get_cart_total': 0
            }
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    id = req.GET.get('id', '')
    products = Product.objects.filter(id=id)
    categories = Category.objects.filter(is_sub = False)
    context = {
        'items': items, 
        'order': order, 
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login,
        'categories': categories,
        'products': products
        }
    return render(req, 'app/detail.html', context)

def category(req):
    if req.user.is_authenticated:
        customer = req.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {
            'get_cart_items': 0, 
            'get_cart_total': 0
            }
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub = False)
    active_category = req.GET.get('category', '')
    if active_category:
        products = Product.objects.filter(category__slug = active_category)
    context = {
        'cartItems': cartItems,
        'categories': categories,
        'products': products,
        'active_category': active_category,
        'user_not_login': user_not_login,
        'user_login': user_login
    }

    return render(req, 'app/category.html', context)


def search(req):
    if req.method == "POST":
        searched = req.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
    if req.user.is_authenticated:
        customer = req.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {
            'get_cart_items': 0, 
            'get_cart_total': 0
            }
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub = False)
    products = Product.objects.all()

    return render(req, 'app/search.html', {
        "searched": searched, 
        "keys": keys,
        'products': products, 
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login,
        'categories': categories
        })

def register(req):
    form = CreateUserForm()
    if req.method == "POST":
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    categories = Category.objects.filter(is_sub = False)
    context = {
        'form': form,
        'user_not_login': "show",
        'user_login': "hidden",
        'categories': categories
    }

    return render(req, 'app/register.html', context)

def loginPage(req):
    if req.user.is_authenticated:
        return redirect('home')
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            messages.info(req,'Username or password is incorrect!')
    categories = Category.objects.filter(is_sub = False)
    context = {
        'user_not_login': "show",
        'user_login': "hidden",
        'categories': categories
    }
    return render(req, 'app/login.html', context)

def logoutPage(req):
    logout(req)
    return redirect('login')

def home(req):
    if req.user.is_authenticated:
        customer = req.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {
            'get_cart_items': 0, 
            'get_cart_total': 0
            }
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub = False)

    products = Product.objects.all()
    context = {
        'products': products, 
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login,
        'categories': categories
        }
    return render(req, 'app/home.html',context)

def cart(req):
    if req.user.is_authenticated:
        customer = req.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {
            'get_cart_items': 0, 
            'get_cart_total': 0
            }
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub = False)
    context = {
        'items': items, 
        'order': order, 
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login,
        'categories': categories
        }
    return render(req, 'app/cart.html', context)

def checkout(req):
    if req.user.is_authenticated:
        customer = req.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {
            'get_cart_items': 0, 
            'get_cart_total': 0
            }
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub = False)
    context = {
        'items': items, 
        'order': order, 
        'cartItems': cartItems,
        'user_not_login': user_not_login,
        'user_login': user_login,
        'categories': categories
        }
    return render(req, 'app/checkout.html', context)

def updateItem(req):
    data = json.loads(req.body)
    productId = data['productId']
    action = data['action']
    customer = req.user
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    
    if action == 'add':
        orderItem.quantity +=1
    elif action == 'remove':
        orderItem.quantity -=1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('added', safe=False)

