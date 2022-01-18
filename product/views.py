from django.utils import timezone
from django.db.models.query_utils import PathInfo
from django.shortcuts import redirect, render, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/accounts/signup")
def create(request : WSGIRequest):
    if request.method == 'POST':
        # return render(request, 'products/create.html', {"error":"All feilds are required"})
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith("http://") or request.POST['url'].startswith("https://"):
                product.url = request.POST['url']
            else:
                product.url = "http://" + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.votes_total = 1
            product.voters.add(request.user)
            product.hunter = request.user
            product.save()
            return redirect('/product/'+str(product.id))
        else:
            return render(request, 'product/create.html', {"error":"All feilds are required"})
    else:
        return render(request, 'product/create.html')

def detail(request : WSGIRequest, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/detail.html', {'product':product})

@login_required(login_url="/accounts/signup")
def upvote(request : WSGIRequest, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        if request.user in product.voters:
            product.voters.remove(request.user)
        else:
            product.voters.add(request.user)
        product.votes_total = len(product.voters)
        product.save()
        return redirect('/product/'+str(product.id))
    return redirect('')

@login_required(login_url="/accounts/signup")
def upvote_home(request : WSGIRequest, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        if request.user in product.voters:
            product.voters.remove(request.user)
        else:
            product.voters.add(request.user)
        product.votes_total = len(product.voters)
        product.save()
        products = Product.objects
        return render(request, 'product/home.html', {'products':products})
    return redirect('')

def home(request : WSGIRequest):
    products = Product.objects
    return render(request, 'product/home.html', {'products':products})