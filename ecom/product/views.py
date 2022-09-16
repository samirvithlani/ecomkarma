
from .models import Product
from django.shortcuts import render
from django.views.generic import ListView,DetailView

# Create your views here.
def index(request):
    return render(request, 'index.html')

class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name ="products/productlist.html"

    