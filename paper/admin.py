from django.contrib import admin

from .models import ReadyPaper, OrderedPaper, OrderStatus, ScientificArea, Subject, Paper

class PaperAdmin(admin.ModelAdmin):
    pass
class OrderedPaperAdmin(PaperAdmin):
    pass

admin.site.register(ReadyPaper)
admin.site.register(OrderedPaper, OrderedPaperAdmin)
admin.site.register(OrderStatus)
admin.site.register(ScientificArea)
admin.site.register(Subject)
