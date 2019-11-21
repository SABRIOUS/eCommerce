from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Product
from django.http import Http404

# Create your views here.
# you can use class based views or function based views

# %%%%%%%%%
# in this views we have stuided two things &&& Function Views and Class Based Views
# you canjust use one
# %%%%%%%%%%%
class ProductFeaturedListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"
    def get_queryset(self,*args,**kwargs):
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured_detail.html"
    # def get_queryset(self,*args,**kwargs):
    #     return Product.objects.featured()


class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"
    # here we don'\t know what context should we write , but we know it from this Function
    # def get_context_data(self, *args,**kwargs):
    #     context = super(ProductListView,self).get_context_data(*args,**kwargs)
    #     print(context) "we got object_list as key of dictionary"
    #     return context

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all()

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request,"products/list.html",context)

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product,slug=slug,active=True)
        try:
            instance = Product.objects.get(slug=slug,active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found... ")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug,active=True)
            instance= qs.first()
        except:
            raise Http404("What...?")
        return instance




class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"
    # here we don'\t know what context should we write , but we know it from this Function
    # here will return 'object' not like object_list

    def get_context_data(self, *args,**kwargs):
        context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
        return context


    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product Doesn't Exist...........")
        return instance

    # another way
    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


def product_detail_view(request,pk=None,*args,**kwargs):
    # instance = Product.objects.get(pk=pk) ['OR']
    # instance = get_object_or_404(Product,pk=pk) ['OR']
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print("No Product Here")
    #     raise Http404("Product Doesn't Exist...........")
    # except:
    #     print("huh?")

    # to be able to call a queryset
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product Doesn't Exist...........")
    # print(instance)
    # instance = Product.objects.filter(id=pk)
    # print(instance)
    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product Doesn't Exist...........")

    context = {
        'object': instance,
    }
    return render(request,"products/detail.html",context)
