# Generated by Django 3.1.4 on 2021-01-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0012_auto_20210107_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='converted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
