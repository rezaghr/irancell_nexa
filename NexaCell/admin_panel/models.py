from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)  # Explicit primary key
    name = models.CharField(max_length=200)
    in_app_transaction = models.PositiveIntegerField()
    bought_pakage_amount = models.PositiveIntegerField()
    shop_transaction = models.PositiveIntegerField()

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