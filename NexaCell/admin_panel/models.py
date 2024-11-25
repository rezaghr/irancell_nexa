from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)  # Explicit primary key
    name = models.CharField(max_length=200)
    in_app_transaction = models.PositiveIntegerField()
    bought_pakage_amount = models.PositiveIntegerField()
    shop_transaction = models.PositiveIntegerField()
    loyalty_tokens = models.PositiveIntegerField(default=0)
    
    def calculate_loyalty_tokens(self):
        total = self.in_app_transaction + self.bought_pakage_amount + self.shop_transaction 
        return total // 100  # 1 token for every 100 in total

    def save(self, *args, **kwargs):
        # Calculate and store loyalty tokens before saving
        self.loyalty_tokens = self.calculate_loyalty_tokens()
        super().save(*args, **kwargs)
        
    def __str__(self):
            return self.name
        
class PhoneNumber(models.Model):
    id = models.AutoField(primary_key=True)  # Explicit primary key
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='phone_numbers'
    )  # Foreign key to User
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.phone_number} ({self.user.name})"