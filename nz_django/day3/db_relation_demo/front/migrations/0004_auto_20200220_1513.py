# Generated by Django 2.0 on 2020-02-20 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_auto_20200220_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='front.FrontUser'),
        ),
    ]