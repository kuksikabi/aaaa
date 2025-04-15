# Generated by Django 2.2.28 on 2025-04-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название видео')),
                ('video_file', models.FileField(upload_to='videos/', verbose_name='Видео файл')),
                ('description', models.TextField(verbose_name='Описание видео')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(default='1.png', upload_to='', verbose_name='app/content/1.png'),
        ),
    ]
