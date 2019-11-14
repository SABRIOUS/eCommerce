from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Product
# Create your views here.
# you can use class based views or function based views


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"
    # here we don'\t know what context should we write , but we know it from this Function
    # def get_context_data(self, *args,**kwargs):
    #     context = super(ProductListView,self).get_context_data(*args,**kwargs)
    #     print(context) "we got object_list as key of dictionary"
    #     return context

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request,"products/list.html",context)




class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"
    # here we don'\t know what context should we write , but we know it from this Function
    # here will return 'object' not like object_list
    
    def get_context_data(self, *args,**kwargs):
        context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
        print(context)
        return context

def product_detail_view(request,pk=None,*args,**kwargs):
    # instance = Product.objects.get(pk=pk)
    instance = get_object_or_404(Product,pk=pk)

    context = {
        'object': instance,
    }
    return render(request,"products/detail.html",context)
