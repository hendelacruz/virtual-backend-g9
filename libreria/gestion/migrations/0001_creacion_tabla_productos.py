# Generated by Django 3.2.7 on 2021-09-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoModel',
            fields=[
                ('productoId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('productoNombre', models.CharField(db_column='nombre', max_length=45)),
                ('productoPrecio', models.DecimalField(db_column='precio', decimal_places=2, max_digits=5)),
                ('productoUnidadMedida', models.TextField(choices=[('UN', 'UNIDAD'), ('DOC', 'DOCENA'), ('CI', 'CIENTO'), ('MI', 'MILLAR')], db_column='unidad_medida', default='UN')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'db_table': 'productos',
                'ordering': ['-productoPrecio'],
            },
        ),
    ]
