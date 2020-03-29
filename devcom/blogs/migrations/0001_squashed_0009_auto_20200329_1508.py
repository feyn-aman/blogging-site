# Generated by Django 3.0.4 on 2020-03-29 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('blogs', '0001_initial'), ('blogs', '0002_remove_user_username'), ('blogs', '0003_auto_20200324_1853'), ('blogs', '0004_blog_datetime'), ('blogs', '0005_blog_votes'), ('blogs', '0006_auto_20200327_1324'), ('blogs', '0007_auto_20200327_1459'), ('blogs', '0008_auto_20200327_1745'), ('blogs', '0009_auto_20200329_1508')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_text', models.CharField(max_length=500)),
                ('blog_title', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=100)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog')),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]