from django.contrib import admin
from .models import Vote,Choice,Poll
# Register your models here.

admin.site.register(Choice)
admin.site.register(Poll)
