# Generated by Django 2.2.6 on 2019-10-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sId', models.CharField(max_length=3)),
                ('sName', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'student_Record',
            },
        ),
    ]
