from django.db import models

# Create your models here.
# class Product(models.Model):
#     title = models.CharField(max_length=256, blank=False, verbose_name="Product Title")
#     price = models.IntegerField(blank=False, verbose_name= "Product Price", default=0)


# CREATE TABLE students_product (
#     "id" integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
#     "title" VARCHAR(256) NOT NULL,
#     "price" integer DEFAULT 0 NOT NULL
# );


class Student(models.Model):
    """Student Model"""

    # VARCHAR
    first_name = models.CharField(max_length=256, blank=False, verbose_name="Ім'я")

    last_name = models.CharField(max_length=256, blank=False, verbose_name="Прізвище")

    middle_name = models.CharField(
        max_length=250, blank=True, verbose_name="По-батькові", default=""
    )
    # DATE
    birthday = models.DateField(blank=False, verbose_name="Дата народження", null=True)
    # "img/image_4.png"
    photo = models.ImageField(blank=True, verbose_name="Фото", null=True)

    ticket = models.CharField(max_length=256, blank=False, verbose_name="Білет")

    notes = models.TextField(blank=True, verbose_name="Додаткові нотатки")
