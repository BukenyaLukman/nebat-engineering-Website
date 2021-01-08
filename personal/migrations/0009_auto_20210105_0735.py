# Generated by Django 2.2.15 on 2021-01-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0008_about_about_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'About Statement',
            },
        ),
        migrations.RemoveField(
            model_name='about',
            name='about_description',
        ),
    ]