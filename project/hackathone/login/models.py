from django.db import models

# Create your models here.


class Member(models.Model):
    email = models.EmailField(
        max_length=100, primary_key=True)  # 사용자가 지정한 값을 PK로
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
