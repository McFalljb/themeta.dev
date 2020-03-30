from django.contrib import admin

# Register your models here.
from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Post



class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/Date', {'fields': ['title', 'published']}),
        ('Author', {'fields': ['author']}),
        ('Content', {'fields': ['content']})
    ]

    formfield_overrides = {
		models.TextField: {'widget': TinyMCE(mce_attrs={'width': 1000})}
	}

admin.site.register(Post, PostAdmin)