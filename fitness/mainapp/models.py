from django.db import models


# Create your models here.
# Фитнес приложение в котором распредленны разные группы мышц по отдельным группам с упражнениям


class Exercise(models.Model):
    objects = None
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.name


class Part_of_the_body(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Card(models.Model):
    text = models.TextField(blank=True, null=True)
    part_of_the_body = models.ManyToManyField(Part_of_the_body)

    def __str__(self):
        return self.part_of_the_body.name
