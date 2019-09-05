from . import models
import algoliasearch_django as algolia



class ProductIndex(algolia.AlgoliaIndex):
    fields = ('id', 'name', 'short_description', 'slug', 'description', 'price')
    settings = {'searchableAttributes': ['name', 'description'],}
    index_name = 'product_index'


algolia.register( models.Product, ProductIndex)
algolia.register(models.Category)