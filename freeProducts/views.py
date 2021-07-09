from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from products.models import Product
# Create your views here.


class FreeProductFeaturedListView(ListView):
    template_name = "products/featured-list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.get_by_category("free").featured()


class FreeProductFeaturedDetailView(DetailView):
    queryset = Product.objects.get_by_category("free").featured()
    template_name = "products/featured-detail.html"


class FreeProductListView(ListView):
    template_name = "products/product_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FreeProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.get_by_category("free")


class FreeProductDetailSlugView(DetailView):
    queryset = Product.objects.get_by_category("free")
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance


class FreeProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)



