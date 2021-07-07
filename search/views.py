from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product
from ads.models import Ad


# Create your views here.
class SearchView(ListView):
    template_name = "search/views.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        context['query'] = self.request.GET.get('q')
        context['products_result'] = Product.objects.search(query)
        context['ads_result'] = Ad.objects.search(query)
        return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        print(method_dict)
        if query is not None:
            return Product.objects.search(query)
            '''
                    __icontains = field contains this
                    __iexact = fields is exactly this
            '''
        return Product.objects.featured()



class SearchProductView(ListView):
    template_name = "search/views.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        print(method_dict)
        if query is not None:
            return Product.objects.search(query)
            '''
                    __icontains = field contains this
                    __iexact = fields is exactly this
            '''
        return Product.objects.featured()

class SearchAdView(ListView):
    template_name = "search/views.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchAdView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        print(method_dict)
        if query is not None:
            return Ad.objects.search(query)
            '''
                    __icontains = field contains this
                    __iexact = fields is exactly this
            '''
        return Ad.objects.featured()