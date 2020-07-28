from django.db import models

class Accounter(models.Model):
    name = models.CharField(max_length=20)
    call = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shop/photo')
    content = models.TextField()
    price = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)
    account = models.ForeignKey(Accounter, on_delete=models.CASCADE,db_column='name')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title


