'''
# Shell session 1
# python manage.py shell
'''

from tags.models import Tag

qs = Tag.objects.all()
print(qs)
t_shirt = Tag.objects.last()
t_shirt.title
t_shirt.slug

t_shirt.products
"""
Reutrns:
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x1112f3fd0>
"""

t_shirt.products.all()
"""
This is an actual queryset of PRODUCTS
Much like Products.objects.all(), but in this case it's ALL of the products that are
related to the "t_shirt" tag
"""
t_shirt.products.all().first()
"""
returns the first instance, if any
"""

exit()

'''
# Shell session 2
# python manage.ppy shell
'''
from products.models import Product



qs = Product.objects.all()
print(qs)
shirt = qs.first()
shirt.title
shirt.description

shirt.tag
'''
Raises an error because the Product model doens't have a field "tag"
'''

shirt.tags
'''
Raises an error because the Product model doens't have a field "tags"
'''

shirt.tag_set
'''
This works because the Tag model has the "products" field with the ManyToMany to Product
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x10c0e75f8>
'''

shirt.tag_set.all()
'''
Returns an actual Queryset of the Tag model related to this product
<QuerySet [<Tag: T shirt>, <Tag: TShirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: t_shirt>]>
'''
