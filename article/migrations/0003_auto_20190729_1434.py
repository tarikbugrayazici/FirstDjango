# Generated by Django 2.2.3 on 2019-07-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190729_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Makaleye Fotoğraf Ekleyin',
        ),
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye Fotoğraf Ekleyin'),
        ),
    ]
