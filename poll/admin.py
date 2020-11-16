from django.contrib import admin
from .models import Polls, Questions, Answer, Choice


admin.site.register(Polls)
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(Choice)