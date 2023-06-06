# Generated by Django 4.2.1 on 2023-06-05 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_remove_book_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='age_group',
            field=models.CharField(choices=[('A', '0-3 Months'), ('B', '3-6 Months'), ('C', '6-12 Months'), ('D', '1-3 Years'), ('E', '3-7 Years'), ('F', '7-13 Years')], default='A', max_length=1),
        ),
    ]