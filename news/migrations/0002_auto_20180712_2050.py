# Generated by Django 2.0.5 on 2018-07-12 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='article',
            name='redacteur',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
