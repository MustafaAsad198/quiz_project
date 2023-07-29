# Generated by Django 4.0.2 on 2023-07-29 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='question_images/')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.section')),
            ],
        ),
    ]
