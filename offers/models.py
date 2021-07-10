from django.db import models

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.db.models import Q
from django.dispatch import receiver
from django.conf import settings


from aStore.utils import unique_slug_generator
from aStore.utils import upload_image_path, get_filename_ext

from accounts.models import Account

User = settings.AUTH_USER_MODEL
TYPES_OFFERS = (
    ('free', 'Free'),
    ('shop', 'Shop'),
)
TYPES_OFFERS_CONDITION =(("bon état", "Bon état"),)
TYPES_OFFERS_CATEGORY = (
    ('maison', 'Maison'),
)

class OfferQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(price__icontains=query) |
                Q(tag__title__icontains=query)
        )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()


class OfferManager(models.Manager):
    def get_queryset(self):
        return OfferQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):  # Offer.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # Offer.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def get_by_types(self, types):
        qs = self.get_queryset().filter(types=types)
        return qs

    def search(self, query):
        return self.get_queryset().active().search(query)


class Offer(models.Model):
    account = models.ForeignKey(Account,null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=50)
    types = models.CharField(max_length=120, default='shop', choices=TYPES_OFFERS)
    category = models.CharField(max_length=120, default='shop', choices=TYPES_OFFERS_CATEGORY)
    user        = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    description = models.TextField()
    condition = models.CharField(max_length=120, default='shop', choices=TYPES_OFFERS_CONDITION)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, unique=True)

    objects = OfferManager()

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug=self.slug)
        return reverse("offers:detail", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    @property
    def name(self):
        return self.title


@receiver(pre_save, sender=Offer)
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

