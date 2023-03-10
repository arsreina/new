# Generated by Django 4.1.4 on 2022-12-19 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Cap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_created=True, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='static')),
                ('is_selected', models.BooleanField(default=False)),
                ('is_in_cart', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caps.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.IntegerField(default=0)),
                ('caps', models.ManyToManyField(related_name='cart', to='caps.cap')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='N/A', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_created=True)),
                ('status', models.CharField(choices=[('delivered', 'delivered'), ('on the way', 'on the way'), ('unpaid', 'unpaid'), ('finished', 'finished')], max_length=100)),
                ('delivery_date', models.DateField()),
                ('address', models.CharField(default='address', max_length=256)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caps.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caps.brand')),
            ],
        ),
        migrations.AddField(
            model_name='cap',
            name='categories',
            field=models.ManyToManyField(related_name='caps', to='caps.category'),
        ),
        migrations.AddField(
            model_name='cap',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='caps.collection'),
        ),
        migrations.AddField(
            model_name='cap',
            name='sizes',
            field=models.ManyToManyField(related_name='caps', to='caps.size'),
        ),
        migrations.AddField(
            model_name='brand',
            name='categories',
            field=models.ManyToManyField(related_name='brands', to='caps.category'),
        ),
    ]
