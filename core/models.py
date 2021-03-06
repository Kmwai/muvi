from django.db import models
from django.urls import reverse


class Movie(models.Model):
    """
    Model representing a movie
    """
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, 'NR - Not Rated'),
        (RATED_G, 'G - General Audiences'),
        (RATED_PG, 'PG - Parental Guidance'),
        (RATED_R, 'R - Restricted'),
    )

    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=50)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED)
    runtime = models.PositiveIntegerField()
    url = models.URLField(blank=True)

    class Meta:
        ordering = '-year', 'title'

    def get_absolute_url(self):
        return reverse('MovieDetail', args=[self.id, self.slug])

    def __str__(self):
        return '{} ({})'.format(self.title, self.year)





