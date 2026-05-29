from django.db import models
import uuid

class MenuItem(models.Model):
    CATEGORY_CHOICES = (
        ('breakfast', 'Завтрак'),
        ('lunch', 'Обед'),
        ('dinner', 'Ужин'),
        ('snack', 'Закуска'),
        ('beverage', 'Напиток'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    composition = models.TextField(blank=True, help_text='Состав блюда')
    calories = models.IntegerField(blank=True, null=True)
    proteins = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fats = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    allergens = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Меню'
        ordering = ['category', 'name']
    
    def __str__(self):
        return f'{self.name} ({self.get_category_display()})'


class Shift(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
    
    def __str__(self):
        return f'{self.name} ({self.start_time} - {self.end_time})'


class Order(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('paid', 'Оплачен'),
        ('delivered', 'Выдан'),
        ('cancelled', 'Отменен'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='orders')
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    order_date = models.DateField()
    delivery_date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Заказ #{self.id} - {self.user.username}'


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Позиция в заказе'
        verbose_name_plural = 'Позиции в заказах'
    
    def __str__(self):
        return f'{self.menu_item.name} x{self.quantity}'
