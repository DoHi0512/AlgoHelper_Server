# Generated by Django 4.0.6 on 2022-07-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahapp', '0002_book_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]