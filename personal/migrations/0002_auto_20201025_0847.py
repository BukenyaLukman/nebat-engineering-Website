# Generated by Django 2.2.15 on 2020-10-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentlyAskedQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=400, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_logo', models.ImageField(blank=True, null=True, upload_to='images')),
                ('partner_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('values', models.CharField(blank=True, max_length=200, null=True)),
                ('vision', models.CharField(blank=True, max_length=300, null=True)),
                ('mission', models.CharField(blank=True, max_length=300, null=True)),
                ('descriptions', models.CharField(blank=True, max_length=500, null=True)),
                ('core_values', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='main_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='hours_of_support',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='number_of_employees',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='projects_worked_on',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='satisified_clients',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='intro',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='profession',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
