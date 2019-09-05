from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, unique=True)
    parent = models.ForeignKey('Category', null=True, blank=True, related_name='cat_child', on_delete=models.CASCADE)
    order = models.IntegerField(blank=True, null=True)
    hidden = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Categories'

    @property
    def products(self):
        return self.categories.all().order_by('-id')[:8]
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=512)
    slug = models.CharField(max_length=512, unique=True)
    category = models.ForeignKey('Category', related_name='categories', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user= models.ForeignKey('auth.User', on_delete=models.PROTECT)
    short_description = models.CharField(max_length=256)
    description = models.TextField(max_length=2048)
    quantity = models.IntegerField(default=1)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inacive')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactive')
    
    class Meta:
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new:
            super(Product, self).save()
            self.slug = '%s-%i' %( slugify(self.name) , self.id)
        super(Product, self).save(*args, **kwargs)

class ProductQuestion(models.Model) :
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, unique=False)
    question = models.TextField(max_length=2000)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='questions')
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inacive')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactive')



class ProductAnswer(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    answer = models.TextField(max_length=2000)
    question = models.ForeignKey('ProductQuestion', on_delete=models.CASCADE, related_name='answers')

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User',unique=True, on_delete=models.CASCADE, related_name='userprofile')
    cpf = models.CharField(max_length=11,null=True, blank=True)
    celphone = models.CharField(max_length=15,null=True, blank=True)
    cep = models.CharField(max_length=10,null=True, blank=True)
    address_1 = models.CharField(max_length=256,null=True, blank=True)
    address_2 = models.CharField(max_length=256,null=True, blank=True)
    address_3 = models.CharField(max_length=256,null=True, blank=True)
    city = models.CharField(max_length=256,null=True, blank=True)
    state = models.CharField(max_length=128,null=True, blank=True)
    remote_costumer_id = models.CharField(max_length=256, null=True, blank=True)
    remote_receiver_id = models.CharField(max_length=256, null=True, blank=True)