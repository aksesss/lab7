from django.db import models


# Create your models here.
class Goods(models.Model):
    good_id = models.AutoField(primary_key=True)  # Тип поля
    good_name = models.CharField(max_length=254, unique=True)
    good_count = models.IntegerField()
    good_cost = models.IntegerField()
    good_characteristic = models.CharField(max_length=254)

    class Meta:
        verbose_name = "Good"
        verbose_name_plural = "Goods"


class Horses(models.Model):
    horse_id = models.AutoField(primary_key=True)
    horse_name = models.CharField(max_length=100)


class Run(models.Model):
    run_id = models.AutoField(primary_key=True)
    runs_date = models.DateField()
    runs_time = models.TimeField()


class Runs(models.Model):
    smth = models.AutoField(primary_key=True)
    runs_run_id = models.IntegerField()
    runs_horse_id = models.CharField(max_length=100)
