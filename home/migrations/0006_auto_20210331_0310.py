# Generated by Django 3.1.7 on 2021-03-31 01:10

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210331_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='category1',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='category2',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
    ]
