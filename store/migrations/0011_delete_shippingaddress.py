# Generated by Django 3.2 on 2021-04-20 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_email_reminderemail_remindemail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
