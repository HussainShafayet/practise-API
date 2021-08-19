from django.db import models
import datetime
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
def current_year():
    return datetime.date.today().year
def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Movie(models.Model):
    title=models.CharField(max_length=100)
    year=models.PositiveIntegerField(default=current_year(),validators=[MinValueValidator(1980),max_value_current_year])
    rated=models.CharField(max_length=100)
    released=models.DateField(auto_now_add=False)
    runtime=models.CharField(max_length=100)
    genre =models.TextField()
    director=models.CharField(max_length=100)
    writer=models.TextField()
    actors=models.TextField()
    plot=models.TextField()
    language= models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    award=models.TextField()
    poster=models.ImageField(upload_to='images/')
    # ratings=models.ArrayField()
    ratings=models.CharField(max_length=100)
    metascore=models.CharField(max_length=50)
    imdbRating=models.FloatField()
    imdbVote=models.IntegerField()
    imdbID=models.CharField(max_length=50)
    Type=models.CharField(max_length=50)
    dvd=models.DateField()
    boxOoffice=models.CharField(max_length=100)
    production=models.CharField(max_length=50)
    response=models.BooleanField()

    def __str__(self):
        return self.title


class Comments(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    comment=models.TextField()

