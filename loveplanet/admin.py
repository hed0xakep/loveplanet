from django.contrib import admin
from .models import MemberModel
@admin.register(MemberModel)
class MemberModelAdmin(admin.ModelAdmin):
    pass
