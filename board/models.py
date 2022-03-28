from django.db import models
from django.contrib.auth.models import User

CATEGORIES = [('TN', 'Танки'), ('HL', 'Хилы'), ('DD', 'ДД'), ('TR', 'Торговцы'),
              ('GL', 'Гилдмастеры'), ('KV', 'Квестгиверы'), ('KY', 'Кузнецы'),
              ('KO', 'Кожевники'), ('ZE', 'Зельевары'), ('MR', 'Мастера заклинаний')]


class Advert(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=128)
    text = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORIES, default='TN')
    creation_date = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f'{self.heading}'


class Comment(models.Model):
    text = models.TextField()
    advert_comment = models.ForeignKey(Advert, on_delete=models.CASCADE)
    author_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def accept(self):
        self.accepted = True
        self.save()

    def __str__(self):
        return f'{self.text}'
