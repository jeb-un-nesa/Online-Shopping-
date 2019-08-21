from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.


class CustomUser(AbstractUser):
    pass
    user_type = models.TextField(null=True, blank=True, choices=[('seller', 'seller'), ('buyer', 'buyer')],
                                   verbose_name="User Type")
    phone_regex = RegexValidator(regex=r'^(?:\+?88)?01[1-9]\d{8}$',
                                 message="Invalid Mobile No.")
    Mobile_no = models.CharField(validators=[phone_regex], max_length=15, blank=True)  # validators should be a list

    def __str__(self):
        return self.email

class product(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=200, default='')
    description = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    seller_name = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='image_folder/', default='image_folder/None/no-img.jpg')
