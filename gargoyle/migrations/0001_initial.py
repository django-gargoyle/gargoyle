import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('key', models.CharField(primary_key=True, serialize=False, max_length=64)),
                ('value', models.JSONField(default=dict)),
                ('label', models.CharField(max_length=64, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(null=True)),
                ('status', models.PositiveSmallIntegerField(
                    default=1,
                    choices=[(1, b'Disabled'), (2, b'Selective'), (3, b'Global'), (4, b'Inherit')],
                )),
            ],
            options={
                'verbose_name_plural': 'switches',
                'verbose_name': 'switch',
                'permissions': (('can_view', 'Can view'),),
            },
        ),
    ]
