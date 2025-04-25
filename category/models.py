from django.db import models


class CommonInfo(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.title
        
        
class Category(CommonInfo):
    
    class Meta:
        db_table = 'category_tb'
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    

    
    
class SubCategory(CommonInfo):
    category = models.ForeignKey(
        Category, 
            on_delete=models.CASCADE, 
                related_name='sub_categories'
        )
    
    class Meta:
        db_table = 'sub_category_tb'
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"