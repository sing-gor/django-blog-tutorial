# Generated by Django 3.0.7 on 2020-07-08 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_status', models.IntegerField(choices=[(0, '发布'), (1, '草稿')], default=1, verbose_name='是否显示')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('body', models.TextField(verbose_name='文章内容')),
                ('author', models.CharField(default='Sing', max_length=100, verbose_name='作者')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章列表',
                'db_table': 'articles',
            },
        ),
    ]
