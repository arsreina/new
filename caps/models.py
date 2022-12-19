from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, related_name='brands')
    image = models.ImageField(upload_to='static', blank=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=3, null=False, default='N/A')

    def __str__(self):
        return self.name


class Cap(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection,
                                   on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    categories = models.ManyToManyField(Category, related_name='caps')
    sizes = models.ManyToManyField(Size, related_name='caps')
    price = models.IntegerField()
    image = models.ImageField(upload_to='static', blank=True, null=True)
    is_selected = models.BooleanField(default=False)
    is_in_cart = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_created=True, null=True)

    def count(self):
        return self.sizes.count()

    def brand_name(self):
        return self.brand.name

    def get_name(self):
        name = self.name if self.name else self.collection.name
        return name

    def description(self):
        return self.collection.description

    def __str__(self):
        return self.name


class Cart(models.Model):
    caps = models.ManyToManyField(Cap, related_name='cart')
    delivery = models.IntegerField(blank=False, default=0)

    def get_cost(self):
        return sum([(cap.price * cap.count()) for cap in self.caps.all()]) + self.delivery

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    status_choices = (
        ('delivered', 'delivered'),
        ('on the way', 'on the way'),
        ('unpaid', 'unpaid'),
        ('finished', 'finished')
    )
    status = models.CharField(choices=status_choices, max_length=100)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_date = models.DateField(auto_created=True)
    delivery_date = models.DateField()
    address = models.CharField(max_length=256, blank=False, default='address')

    def __str__(self):
        return self.status
