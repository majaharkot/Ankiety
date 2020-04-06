from django.contrib import admin
from formularze import models
from django.forms import Textarea
from django.db.models.fields import TextField


admin.site.register(models.Kategoria)

class OdpowiedziInline(admin.TabularInline):
    model = models.Odpowiedz
    fields = ['tekst_odpowiedzi']
    extra = 3
    max_num = 6


@admin.register(models.Pytanie)
class PytanieAdmin(admin.ModelAdmin):
    fields = ('kategoria', 'tekst_pytania')
    inlines = [OdpowiedziInline]
    search_fields = ['tekst_pytania']
    list_per_page = 10
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})}
    }