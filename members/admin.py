from django.contrib import admin
from .models import Members
from .models import books
from .models import bookauthor
from .models import author
from .models import likes
from .models import dislikes
from .models import comments
from .models import bookurl
from .models import blogs
# Register your models here.
admin.site.register(Members)
# admin.site.register(bookurl)
admin.site.register(books)
admin.site.register(author)
# admin.site.register(likes)
# admin.site.register(dislikes)
# admin.site.register(bookauthor)
admin.site.register(blogs)
# admin.site.register(comments)
