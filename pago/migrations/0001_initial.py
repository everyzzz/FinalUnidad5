# Generated by Django 4.1.4 on 2022-12-19 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('services', models.CharField(choices=[('Netflix', 'Netflix'), ('Amazon Video', 'Amazon Video'), ('Star +', 'Star +'), ('Paramount +', 'Paramount +')], max_length=100)),
                ('pay_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pagos',
            },
        ),
    ]