from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title


class NavstevaWebu(models.Model):
    datum = models.DateField(unique=True)
    pocet = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-datum"]
        verbose_name = "návštěva webu"
        verbose_name_plural = "návštěvy webu"

    def __str__(self):
        return f"{self.datum}: {self.pocet}"
