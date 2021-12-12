from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# Dsuser 모델 
class DsUser(AbstractUser) :
     user_id = models.CharField(max_length=100,unique=True);  # id     
     def __str__(self):
          return str(self.id);
          
# Tag 모델
class Tag(models.Model):
     tag = models.CharField(max_length=2000)

     def __str__(self) :
          return str(self.id);

# Post 모델
class Post(models.Model):
     writer = models.ForeignKey(DsUser, on_delete=models.CASCADE, db_column="user_id");  # 작성자     
     imageUrl = models.CharField(max_length=2000, null=True);   # 이미지 주소
     contents = models.TextField(null=True);  # 내용
     createDt = models.DateTimeField(auto_now_add=True);
     tag = models.ManyToManyField(Tag, blank=True);

     def __str__(self):
          return str(self.id);


