# from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Ad
from carts.models import Cart


class AdFeaturedListView(ListView):
    template_name = "ads/ad_featured_list.html"
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Ad.objects.all().featured()

class AdListView(ListView):
    template_name = "ads/ad_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AdListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Ad.objects.all()

class AdDetailSlugView(DetailView):
    queryset = Ad.objects.all()
    template_name = "ads/ad_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AdDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Ad, slug=slug, active=True)
        try:
            instance = Ad.objects.get(slug=slug, active=True)
        except Ad.DoesNotExist:
            raise Http404("Not found..")
        except Ad.MultipleObjectsReturned:
            qs = Ad.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance

class AdDetailView(DetailView):
    # queryset = Ad.objects.all()
    template_name = "ads/ad_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AdDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Ad.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Ad doesn't exist")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Ad.objects.filter(pk=pk)