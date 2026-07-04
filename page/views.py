# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
from .models import Product


# Create your views here.
def get_product(request):
    product=Product.objects.all()
    context={
        'products':product
    }
    return render(request,'product/list.html',context)

def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={
        'dilshodjon':product
    }
    return render(request,'product/detail.html',context)

def create_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        if title and price and description:
            Products.objects.create(
                title=title,
                price=price,
                description=description
            )
            return redirect('list')

    return render(request, 'product/create.html')