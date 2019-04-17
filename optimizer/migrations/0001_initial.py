# Generated by Django 2.2 on 2019-04-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw', models.BooleanField(default=False)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_qty', models.IntegerField()),
                ('time_sec', models.IntegerField()),
                ('ingredients', models.ManyToManyField(related_name='recipes', through='optimizer.Ingredient', to='optimizer.Resource')),
                ('product', models.ForeignKey(on_delete='PROTECT', to='optimizer.Resource')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete='CASCADE', to='optimizer.Recipe'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='resource',
            field=models.ForeignKey(on_delete='CASCADE', to='optimizer.Resource'),
        ),
    ]
