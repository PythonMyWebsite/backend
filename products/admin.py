from django.contrib import admin

from .models import Category,Product,ProductComment,ProductImage,ProductInfo

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductComment)
admin.site.register(ProductImage)
admin.site.register(ProductInfo)