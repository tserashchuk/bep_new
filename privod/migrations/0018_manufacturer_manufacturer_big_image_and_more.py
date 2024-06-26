# Generated by Django 4.1.7 on 2024-02-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("privod", "0017_alter_article_article_slug_alter_category_cat_slug_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="manufacturer",
            name="manufacturer_big_image",
            field=models.ImageField(
                default="placeholder.jpg",
                upload_to="",
                verbose_name="Фон производителя",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="article_slug",
            field=models.CharField(
                default="article2024-02-19 19:25:08.093817",
                max_length=200,
                verbose_name="URL",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="cat_slug",
            field=models.CharField(
                default="slug2024-02-19 19:25:08.091088",
                max_length=200,
                verbose_name="URL",
            ),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="manufacturer_slug",
            field=models.CharField(
                default="manufacturer2024-02-19 19:25:08.091628",
                max_length=200,
                verbose_name="URL",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_slug",
            field=models.CharField(
                default="product2024-02-19 19:25:08.092290",
                max_length=200,
                verbose_name="URL",
            ),
        ),
        migrations.AlterField(
            model_name="producttag",
            name="tag_slug",
            field=models.CharField(
                default="tag2024-02-19 19:25:08.091959",
                max_length=200,
                verbose_name="URL",
            ),
        ),
        migrations.AlterField(
            model_name="region",
            name="region_slug",
            field=models.CharField(
                default="region2024-02-19 19:25:08.094893",
                max_length=200,
                verbose_name="URL",
            ),
        ),
    ]
