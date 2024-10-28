# Generated by Django 4.2.16 on 2024-10-28 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0039_cvederivationclusterproposal_derivations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='cve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='container', to='shared.cverecord'),
        ),
        migrations.AddIndex(
            model_name='affectedproduct',
            index=models.Index(condition=models.Q(('package_name__isnull', False)), fields=['package_name'], name='affprod_with_pkgnames_idx'),
        ),
    ]
