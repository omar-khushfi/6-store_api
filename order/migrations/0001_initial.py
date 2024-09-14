# Generated by Django 5.1.1 on 2024-09-13 12:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0005_review'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='', max_length=100)),
                ('zipcode', models.CharField(default='', max_length=100)),
                ('street', models.CharField(default='', max_length=500)),
                ('state', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=100)),
                ('total_amount', models.IntegerField(default=0)),
                ('paymentstatus', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=30)),
                ('paymentmode', models.CharField(choices=[('Cod', 'Cod'), ('Card', 'Card')], default='Cod', max_length=30)),
                ('orderstatus', models.CharField(choices=[('processing', 'Processing'), ('Shipped', 'Shipped'), ('DeliveredS', 'Delivered')], default='processing', max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='order.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product')),
            ],
        ),
    ]