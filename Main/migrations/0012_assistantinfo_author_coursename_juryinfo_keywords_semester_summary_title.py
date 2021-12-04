# Generated by Django 3.2.9 on 2021-12-04 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_remove_document_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=64)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.user')),
            ],
            options={
                'db_table': 'Title',
            },
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1024)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.user')),
            ],
            options={
                'db_table': 'Summary',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=64)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.user')),
            ],
            options={
                'db_table': 'Semester',
            },
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=128)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.user')),
            ],
            options={
                'db_table': 'Keywords',
            },
        ),
        migrations.CreateModel(
            name='JuryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=32)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.user')),
            ],
            options={
                'db_table': 'JuryInfo',
            },
        ),
        migrations.CreateModel(
            name='CourseName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=64)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.user')),
            ],
            options={
                'db_table': 'CourseName',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('student_number', models.CharField(max_length=32)),
                ('education_type', models.CharField(max_length=32)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.user')),
            ],
            options={
                'db_table': 'Author',
            },
        ),
        migrations.CreateModel(
            name='AssistantInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=32)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.user')),
            ],
            options={
                'db_table': 'AssistantInfo',
            },
        ),
    ]
