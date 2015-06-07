from django.contrib import admin
from mymodel.models import Goods,SalesRecord,Member,Staff,Person,StockRecord

# Register your models here.
admin.site.register(Goods)
admin.site.register(SalesRecord)
admin.site.register(Member)
admin.site.register(Staff)
admin.site.register(Person)
admin.site.register(StockRecord)
