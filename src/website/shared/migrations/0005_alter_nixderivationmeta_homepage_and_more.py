# Generated by Django 4.2.7 on 2023-12-05 03:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shared", "0004_alter_nixlicense_spdx_id_alter_nixlicense_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nixderivationmeta",
            name="homepage",
            field=models.URLField(null=True),
        ),
    ]
