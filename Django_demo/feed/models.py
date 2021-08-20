from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    token = models.CharField(max_length=40)

class role_date_data(models.Model):
    date = models.CharField(max_length=20)
    # 生产
    production = models.IntegerField()
    # 收购
    bidders = models.IntegerField()
    # 运输
    transport = models.IntegerField()
    # 销售
    sale = models.IntegerField()
    # 消费者
    consume = models.IntegerField()