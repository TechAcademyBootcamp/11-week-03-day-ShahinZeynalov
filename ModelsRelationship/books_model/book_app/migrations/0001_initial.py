# Generated by Django 2.2.8 on 2019-12-18 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=63, verbose_name='Fullname')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/author_images', verbose_name='Author Image')),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], verbose_name='Gender')),
                ('birthday', models.DateField(auto_now=True, verbose_name='Birthday')),
                ('nationality', models.CharField(max_length=63, verbose_name='Nation')),
                ('info', models.TextField(default='Author info ...', verbose_name='Info')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ('fullname',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Book Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Price')),
                ('page_count', models.IntegerField(default=0, verbose_name='Page Size')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='images/book_images/', verbose_name='Cover Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_app.Author')),
                ('category_id', models.ManyToManyField(to='book_app.Category')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ('title',),
            },
        ),
    ]
