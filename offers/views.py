# from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Offer
from carts.models import Cart


class OfferFeaturedListView(ListView):
    template_name = "offers/offers_featured_list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Offer.objects.get_by_category("shop").featured()


class OfferFeaturedDetailView(DetailView):
    queryset = Offer.objects.get_by_category("shop").featured()
    template_name = "offers/featured_detail_offers.html"


class OfferListView(ListView):
    template_name = "offers/offers_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OfferListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Offer.objects.get_by_category("shop")


class OfferDetailSlugView(DetailView):
    queryset = Offer.objects.get_by_category("shop")
    template_name = "offers/offers_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OfferDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Offer, slug=slug, active=True)
        try:
            instance = Offer.objects.get(slug=slug, active=True)
        except Offer.DoesNotExist:
            raise Http404("Not found..")
        except Offer.MultipleObjectsReturned:
            qs = Offer.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance


# class OfferDetailView(DetailView):
#     # queryset = Offer.objects.all()
#     template_name = "offers/details_offers.html"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(OfferDetailView, self).get_context_data(*args, **kwargs)
#         print(context)
#         # context['abc'] = 123
#         return context
#
#     def get_object(self, *args, **kwargs):
#         request = self.request
#         pk = self.kwargs.get('pk')
#         instance = Offer.objects.get_by_id(pk)
#         if instance is None:
#             raise Http404("Offer doesn't exist")
#         return instance
#
#     # def get_queryset(self, *args, **kwargs):
#     #     request = self.request
#     #     pk = self.kwargs.get('pk')
#     #     return Offer.objects.filter(pk=pk)
#
#
