from django.contrib import admin

from django.contrib.auth.models import User

from .models import articles, author, Category, contactModel, comment_put, MyltiImage








# Register your mo
admin.site.register(Category)
admin.site.register(articles)
admin.site.register(comment_put)
admin.site.register(author)
admin.site.register(MyltiImage)

admin.site.register(contactModel)


