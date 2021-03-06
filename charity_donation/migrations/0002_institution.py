# Generated by Django 3.2.9 on 2021-11-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_donation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('fundacja', 'fundacja'), ('organizacja pozarządowa', 'organizacja pozarządowa'), ('zbiórka lokalna', 'zbiórka lokalna')], default=('fundacja', 'fundacja'), max_length=128)),
                ('categories', models.ManyToManyField(to='charity_donation.Category')),
            ],
        ),
    ]
