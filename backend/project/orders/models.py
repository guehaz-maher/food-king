from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Order(models.Model):
    STATUS = (
        ('pending' , 'pending'),
        ('preparing', 'preparing'),
        ('ready', 'ready'),
        ('delivered', 'delivered'),
        ('adress', 'delivery_adress')
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.TimeField(auto_now_add = True)
    total_price = models.IntegerField()
    status = models.CharField(max_length=20, choices = STATUS, default = 'pending')

    def __str__(self):
        return f'{self.user} - {self.status}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.CharField(max_length = 36)
    quantity = models.IntegerField(default = 1)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.order.user} - {self.menu_item}'
