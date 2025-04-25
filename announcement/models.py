from django.db import models
from category.models import CommonInfo, SubCategory

class Item(CommonInfo):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    article = models.CharField(max_length=100, null=True, blank=True)
    count = models.PositiveIntegerField(default=0)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'item_tb'
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    
    def __str__(self):
        return self.title
    

class Recall(models.Model):
    full_name = models.CharField(max_length=250)
    comment = models.TextField()
    RATE_CHOICE = (
        (1, "Ужасно"),
        (2, "Плохо"),
        (3, "Не плохо"),
        (4, "Хорошо"),
        (5, "Превосходно"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)    
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICE, null=True, blank=True)
    
    class Meta:
        db_table = 'rate_tb'
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    
    def __str__(self):
        return f"{self.full_name} -> {self.rate}"    
    

    # image = models.ImageField(verbose_name="Главная картинка товара", upload_to="items/img_box")
