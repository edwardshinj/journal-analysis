from django.contrib import admin

# Register your models here.

from .models import User, ResponseSchema, Question, Entry, Response, EntryText

admin.site.register(User)
admin.site.register(ResponseSchema)
admin.site.register(Question)
admin.site.register(Entry)
admin.site.register(Response)
admin.site.register(EntryText)