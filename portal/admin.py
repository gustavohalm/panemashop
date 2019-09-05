from django.contrib import admin
from portal.models import  Category, Product, ProductQuestion, ProductAnswer, UserProfile
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',) }


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductQuestion)
admin.site.register(ProductAnswer)
admin.site.register(UserProfile)