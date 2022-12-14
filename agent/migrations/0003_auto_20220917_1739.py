# Generated by Django 3.2 on 2022-09-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_rename_image_agent_model_image_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent_model',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo electrónico [*]'),
        ),
        migrations.AlterField(
            model_name='agent_model',
            name='image_main',
            field=models.ImageField(default='', upload_to='img_agent/', verbose_name='Imagen [*]'),
        ),
        migrations.AlterField(
            model_name='agent_model',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre [*]'),
        ),
    ]
