from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=220)

    def __str__(self):
        return self.name

    def movies_count(self):
        return  self.movies.count()




class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director,related_name="movies", on_delete=models.CASCADE)

    def __str__(self):
        return self.title





STAR_CHOICES = ((i, '*' * i) for i in range(6))


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=STAR_CHOICES,default=1)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review')


