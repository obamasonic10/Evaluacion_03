<<<<<<< HEAD
# Generated by Django 3.2.4 on 2021-06-09 19:24
=======
# Generated by Django 3.2.4 on 2021-06-09 19:16
>>>>>>> 11a16997c79d9e1a684791c36bc0b8e12b25ee05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamburgame', '0002_auto_20210609_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]
