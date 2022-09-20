# Generated by Django 4.0.4 on 2022-09-20 16:28

import administrador.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Copiaseguridad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='Copia de Seguridad', max_length=200)),
                ('archivo', models.FileField(upload_to='copiaseguridad', validators=[administrador.models.validate_file_extension])),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Electrodomestico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('referencia', models.CharField(blank=True, max_length=25)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=20, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('stock_elemento', models.IntegerField(default=0, verbose_name='Stock')),
                ('favorito', models.BooleanField(default=False)),
                ('foto', models.ImageField(blank=True, default='carrito/casa.png', null=True, upload_to='carrito')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Anulado', 'Anulado')], default='Activo', max_length=10, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorito', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=20, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Tipos_Elemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('Accesorios', 'Accesorios'), ('Productos', 'Productos')], default='Accesorios', max_length=20, verbose_name='Categoría')),
                ('subcategoria', models.CharField(max_length=20, unique=True, verbose_name='Subcategoría')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True, help_text='MM/DD/AAAA', verbose_name='Fecha de Registro')),
                ('stock_agregada', models.IntegerField(default=0, verbose_name='Stock Nuevo')),
                ('stock_stock', models.IntegerField(verbose_name='Stock')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Anulado', 'Anulado')], default='Activo', max_length=10, verbose_name='Estado')),
                ('elemento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.elemento', verbose_name='elemento')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiposervicio', models.CharField(choices=[('Reparación', 'Reparación'), ('Mantenimiento', 'Mantenimiento')], max_length=20, verbose_name='Tipo de Servicio')),
                ('fallas_basicas', models.CharField(max_length=255, verbose_name='Falla que Presenta')),
                ('diagnostico', models.CharField(max_length=250, verbose_name='Diagnostico')),
                ('observacion', models.CharField(blank=True, max_length=100, verbose_name='Observacion')),
                ('fecha_entrada', models.DateField(auto_now=True, help_text='MM/DD/AAAA', verbose_name='Fecha de Entrada')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=20, verbose_name='Estado')),
                ('electrodomestico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.electrodomestico', verbose_name='Articulo')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.usuario', verbose_name='Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='elemento',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.marca', verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='elemento',
            name='tipo_elemento',
            field=models.ForeignKey(null='False', on_delete=django.db.models.deletion.SET_NULL, to='administrador.tipos_elemento', verbose_name='Subcategoría'),
        ),
        migrations.AddField(
            model_name='electrodomestico',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.marca', verbose_name='Marca'),
        ),
        migrations.CreateModel(
            name='Cantidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True, help_text='MM/DD/AAAA', verbose_name='Fecha de Registro')),
                ('cantidad_agregada', models.IntegerField(default=0)),
                ('cantidad_stock', models.IntegerField(verbose_name='Cantidad')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Anulado', 'Anulado')], default='Activo', max_length=10, verbose_name='Estado')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.elemento', verbose_name='Producto')),
            ],
        ),
    ]
