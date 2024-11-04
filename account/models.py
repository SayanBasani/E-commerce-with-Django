from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        SELLER = "SELLER", "Seller"
        USER = "USER", "User"

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        is_new_user = not self.pk
        super().save(*args, **kwargs)

        if is_new_user:
            if self.role == self.Role.ADMIN:
                Admin.objects.create(user=self)
            elif self.role == self.Role.SELLER:
                Seller.objects.create(user=self)
            elif self.role == self.Role.USER:
                UserProfile.objects.create(user=self)


class Admin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Admin: {self.user.username}"


class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Establishes a one-to-one relationship
    SELLER_STATE = {
        ('Y', 'YES'),
        ('N', 'NO'),
        ('B', 'Blocked'),
        ('S', 'Suspended')
    }
    account_create_time = models.DateTimeField(auto_now=True)  # Automatically set the time of creation
    seller_status = models.CharField(max_length=1, choices=SELLER_STATE)

    def __str__(self):
        return f"Seller: {self.user.username}"


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"UserProfile: {self.user.username}"
