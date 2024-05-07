from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Danh sách loại món'

class Product(models.Model):
    name = models.CharField(verbose_name='Tên món',max_length=50)
    price = models.IntegerField(verbose_name='Giá',default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, verbose_name='Loại món')
    description = models.CharField(max_length=250, default='', blank= True, null = True)
    image = models.ImageField(upload_to= 'uploads/product/',verbose_name='Hình ảnh')
    ordered_times = models.IntegerField(default=0, verbose_name='Số lần đặt')
    min_user_rating = models.IntegerField(default=0, verbose_name='Điểm thấp nhất để được mua')
    combo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Danh sách các món'
    



    