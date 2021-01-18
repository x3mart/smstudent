from django.contrib import admin

from .models import ReadyPaper, OrderedPaper, OrderStatus, ScientificArea, Subject

admin.site.register(ReadyPaper)
admin.site.register(OrderedPaper)
admin.site.register(OrderStatus)
admin.site.register(ScientificArea)
admin.site.register(Subject)
