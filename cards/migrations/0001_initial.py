# Generated by Django 3.1.5 on 2021-02-11 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('mana_cost', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MagicSet',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CardFace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mana_cost', models.CharField(max_length=20)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faces', to='cards.card')),
            ],
        ),
    ]
