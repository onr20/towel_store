# Generated by Django 3.2.2 on 2021-05-07 15:49

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
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=255)),
                ('avatar', models.ImageField(upload_to='')),
                ('role', models.CharField(choices=[('ADM', 'Admin'), ('USR', 'User')], default='USR', max_length=3)),
                ('preferred_communication_channel', models.CharField(choices=[('PST', 'Post Mail'), ('EML', 'E-Mail')], default='EML', max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
