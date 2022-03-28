# Generated by Django 4.0.3 on 2022-03-28 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('TN', 'Танки'), ('HL', 'Хилы'), ('DD', 'ДД'), ('TR', 'Торговцы'), ('GL', 'Гилдмастеры'), ('KV', 'Квестгиверы'), ('KY', 'Кузнецы'), ('KO', 'Кожевники'), ('ZE', 'Зельевары'), ('MR', 'Мастера заклинаний')], default='TN', max_length=2)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('upload', models.FileField(upload_to='uploads/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
                ('advert_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.advert')),
                ('author_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]