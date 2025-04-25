from django.contrib import admin
from announcement.models import Item, Recall
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 
                    'sub_category', 
                    'title',
                    'price',
                    'article',
                    'count',
                    'created_at', 
                    'updated_at'
                    ]
    
admin.site.register(Item, ItemAdmin)

class RecallAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'rate']
    
admin.site.register(Recall, RecallAdmin)