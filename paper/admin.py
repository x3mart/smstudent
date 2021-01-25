from django.contrib import admin

from .models import ReadyPaper, OrderedPaper

class PaperAdmin(admin.ModelAdmin):
    pass
class OrderedPaperAdmin(PaperAdmin):
    pass


admin.site.register(ReadyPaper)
admin.site.register(OrderedPaper, OrderedPaperAdmin)

