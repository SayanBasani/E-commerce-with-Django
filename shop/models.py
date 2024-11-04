from django.db import models
# from django.contrib.auth.models import User
from account.models import Seller,CustomUser,UserProfile
# Create your models here.
class seller_product(models.Model):
  user = models.ForeignKey(Seller , on_delete=models.CASCADE,related_name='uploaded_items')
  item_name = models.CharField(max_length=150)
  item_others_details = models.JSONField()
  upload_datetime = models.DateTimeField( auto_now=True)
  description = models.TextField(max_length=1000)
  price = models.CharField(max_length=100)
  product_id = models.CharField(max_length=20, unique=True, editable=False)
  @property
  def item_id(self):
      return f'{self.user.username[0:3]}_{self.upload_datetime.strftime("%Y%m%d%H%M%S")}'

  def __str__(self) -> str:
    return f'{self.product_id}'
  
class ItemImage(models.Model):
    related_product = models.ForeignKey(seller_product, on_delete=models.CASCADE, related_name='images')
    image_id = models.CharField(max_length=50,unique=True)
    image = models.ImageField(upload_to='shopping_items/')

    def __str__(self):
      return f'Image for {self.related_product.item_name}'

class cartItems(models.Model):
  user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
  productid = models.CharField(max_length=50)
  quantity = models.IntegerField(default = 1)
  upload_datetime = models.DateTimeField( auto_now=True)
  def __str__(self) -> str:
     return f'{self.productid}'

class item_review(models.Model):
  item = models.ForeignKey(seller_product, on_delete=models.CASCADE , related_name='review')
  review_datetime = models.DateTimeField( auto_now=True)
  commented_person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  comment = models.TextField()
  like = models.IntegerField(default=0)

  def __str__(self) :
    return f'{self.review_datetime}'