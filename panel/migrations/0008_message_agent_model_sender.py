# Generated by Django 3.2 on 2022-10-06 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_alter_message_agent_model_agent_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_agent_model',
            name='sender',
            field=models.CharField(default='1', max_length=3, verbose_name='Remitente bkup [*]'),
            preserve_default=False,
        ),
    ]
