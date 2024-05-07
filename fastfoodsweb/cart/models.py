import datetime
from django.db import models
from django.contrib.auth.models import User
from webstore.models import Product

class Address(models.Model):
    address = models.CharField(max_length=250, default='',blank=True, verbose_name="Địa chỉ")
    customer = models.ForeignKey( User, on_delete=models.CASCADE, verbose_name="Khách hàng")
    default = models.BooleanField(default=False, verbose_name="Địa chỉ mặc định")
    def __str__(self):
        return self.address
    class Meta:
        verbose_name_plural = 'Địa chỉ'

class Order(models.Model):
    CREATE = "CE"
    PREPARE = "PR"
    DELIVERY = "DE"
    DELIVERED = "DR"
    CANCELED = "CA"
    ORDER_STATUS = [
        (CREATE, "Tạo đơn"),
        (PREPARE, "Chuẩn bị"),
        (DELIVERY, "Đang giao"),
        (DELIVERED, "Đã giao"),
        (CANCELED, "Đơn hủy"),
    ]
    status = models.CharField(
        max_length=2,
        choices=ORDER_STATUS,
        default=CREATE,
    )
    receiver = models.CharField(max_length=50, default= '', blank=True,verbose_name="Người nhận")
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, default= '', blank=True,verbose_name="Địa chỉ nhận hàng")
    phone = models.CharField(max_length=20, default='',verbose_name="Số điện thoại")
    orderedTime = models.DateTimeField(verbose_name="Thời gian đặt", blank = True,null=True)
    receiveTime = models.DateTimeField(verbose_name="Thời điểm nhận", blank=True,null=True)
    total = models.IntegerField(default=0,verbose_name="Tổng đơn")
    note = models.TextField(default='', blank=True,verbose_name="Ghi chú")
    def __str__(self):
        return f'{self.customer.first_name} {self.orderedTime}'
    class Meta:
        verbose_name_plural = 'Đơn hàng'
    
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default='', blank=True, null = True)
    ADDED = "AD"
    CHOSE = "CH"
    ORDERED = "OR"
    CANCEL = "CA"
    CART_STATUS = [
        (ADDED, "Trong giỏ"),
        (CHOSE, "Chọn đặt"),
        (ORDERED, "Đã đặt"),
        (CANCEL, "Đơn hủy"),
    ]
    status = models.CharField(
        max_length=2,
        choices=CART_STATUS,
        default=ADDED,
    )
    
    def __str__(self):
        return f'{self.customer.first_name} {self.order}'
    class Meta:
        verbose_name_plural = 'Giỏ hàng'
        
