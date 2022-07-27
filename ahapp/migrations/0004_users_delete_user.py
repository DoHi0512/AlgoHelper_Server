# Generated by Django 4.0.6 on 2022-07-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahapp', '0003_user_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
