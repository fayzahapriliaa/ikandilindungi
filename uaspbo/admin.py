from django.contrib import admin
from .models import *


class bukuikan(admin.ModelAdmin):
    list_display = ['nama', 'nama_ilmiah', 'img', 'detail']
    search_fields = ['nama', 'nama_ilmiah']
    list_filter = ['kelompok_id']
    list_per_page = 4

admin.site.register(Kelompok)
admin.site.register(Ikan, bukuikan)
