# Generated by Django 4.2.7 on 2024-01-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phonepe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('merchant_transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('pg_transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]