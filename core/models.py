from django.db import models

class TopPost(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.tag


class Post(models.Model):
    odam = models.CharField(max_length=31)
    nomi = models.CharField(max_length=31)
    rasm1 = models.CharField(max_length=255)
    rasm2 = models.CharField(max_length=255)
    read = models.IntegerField(default=2)
    haqida = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(TopPost, blank=True)

    def __str__(self) -> str:
        return self.odam