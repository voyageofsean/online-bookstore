from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Book(models.Model):
    #主键创建后不能被修改
    ISBN=models.CharField(primary_key=True,max_length=10)
    #nvarchar和nchar差别在数组填充上，干脆不做区分了
    BookName=models.CharField(max_length=50)
    BookAuthor=models.CharField(max_length=50)
    BookNum=models.IntegerField(validators = [MaxValueValidator(10000),MinValueValidator(0)])
    BookPrice=models.FloatField(validators=[MaxValueValidator(10000),MinValueValidator(0)])
    #这两个需求分析改成date类
    PublishDate=models.DateField('date published',null=True)
    ShelfDate=models.DateField('date shelfed',null=True)
    BookInformation=models.TextField(null=True)
    
class User(models.Model):
    UserName=models.CharField(primary_key=True,max_length=10)
    UserAddress=models.CharField(max_length=50)
    UserKey=models.CharField(max_length=25)
    
class ShoppingCart(models.Model):
    UserName=models.ForeignKey(User,on_delete=models.CASCADE)
    ISBN=models.ForeignKey(Book,on_delete=models.CASCADE)
    ShoppingNum=models.IntegerField(validators=[MaxValueValidator(10000),MinValueValidator(1)])
    
class Order(models.Model):
    #这个自动生成int(11) 
    OrderID=models.AutoField(primary_key=True)
    UserName=models.ForeignKey(User,on_delete=models.CASCADE)
    OrderCard=models.CharField(max_length=19)
    OrderAddress=models.TextField()
    OrderTime=models.DateTimeField('date ordered')
    OrderInformation=models.TextField()