# Generated by Django 3.2 on 2022-09-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cate', models.CharField(max_length=100)),
                ('selectfile', models.FileField(upload_to='MyNotes')),
                ('comments', models.TextField()),
            ],
        ),
    ]
