from django.db import models

# Create your models here.

class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_username = models.CharField(max_length = 200)
    user_password = models.CharField(max_length = 200)
    user_date = models.DateField(auto_now = True)  

    def getQuery(self):
        return {
            'user_id': self.user_id,
            'user_username': self.user_username,
            'user_password': self.user_password,
            'user_date': self.user_date
        }

class ProductModel(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length = 200)
    product_price = models.FloatField()
    product_img = models.CharField(max_length = 200)

    def getQuery(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_price': self.product_price,
            'product_img': self.product_img
        }

class TransactionModel(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    transaction_date = models.DateField(auto_now = True)
    transaction_amount = models.IntegerField()

    def getQuery(self):
        return {
            'transaction_id': self.transaction_id,
            'product_id': self.product_id,
            'user_id': self.user_id,
            'transaction_date': self.transaction_date,
            'transaction_amount': self.transaction_amount
        }

