# Generated by Django 4.2.7 on 2023-11-30 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Danh sách loại món',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tên món')),
                ('price', models.IntegerField(default=0, verbose_name='Giá')),
                ('description', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('image', models.ImageField(upload_to='uploads/product/', verbose_name='Hình ảnh')),
                ('ordered_times', models.IntegerField(default=0, verbose_name='Số lần đặt')),
                ('min_user_rating', models.IntegerField(default=0, verbose_name='Điểm thấp nhất để được mua')),
                ('combo', models.BooleanField(default=False)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webstore.category', verbose_name='Loại món')),
            ],
            options={
                'verbose_name_plural': 'Danh sách các món',
            },
        ),
    ]