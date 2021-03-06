from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.contrib.auth import get_user_model
User = get_user_model()

class Genre(models.Model):
    name = CharField(max_length=50)
    favorited_by = ManyToManyField(
        User,
        related_name='favorite_genres',
        blank=True
    )

    def __str__(self):
        return f'{self.name}'

class Link(models.Model):
    platform = CharField(max_length=50)
    url = CharField(max_length=300)

    def __str__(self):
        return f'{self.platform}'

class Instrument(models.Model):
    name = CharField(max_length=50)
    icon = CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'

class Musician(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.CharField(max_length=300)
    instruments = ManyToManyField(
        Instrument,
        related_name='musicians',
        blank=True
    )
    user = models.ForeignKey(
        User,
        related_name='musician',
        on_delete=CASCADE,
        blank=True,
        default=None,
        null=True
    )

    def __str__(self):
        return f'Musician {self.id} on {self.name}'

class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    year_formed = models.IntegerField()
    logo = models.CharField(max_length=300, blank=True)
    cover_image = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=200)
    genres = models.ManyToManyField(
        Genre, 
        related_name='artists', 
        blank=True
    )
    links = models.ManyToManyField(
        Link,
        related_name='artists',
        blank=True
    )
    musicians = ManyToManyField(
        Musician,
        related_name='artists',
        blank=True
    )
    favorited_by = ManyToManyField(
        User,
        related_name='favorite_artists',
        blank=True
    )
    owner = ForeignKey(
        User,
        related_name='artist_owner',
        on_delete=CASCADE,
        null=True,
        default=1
    )

    def __str__(self):
        return f'{self.name}'

class Release(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=6)
    release_date = models.DateField()
    artwork = models.CharField(max_length=300)
    artist = models.ForeignKey(
        Artist,
        related_name='releases',
        on_delete=CASCADE
    )
    genres = models.ManyToManyField(
        Genre, 
        related_name='releases', 
        blank=True
    )
    links = models.ManyToManyField(
        Link,
        related_name='releases',
        blank=True
    )
    favorited_by = ManyToManyField(
        User,
        related_name='favorite_releases',
        blank=True
    )
    owner = ForeignKey(
        User,
        related_name='release_owner',
        on_delete=CASCADE,
        null=True,
        default=1
    )

    def __str__(self):
        return f'{self.name}'

class Track(models.Model):
    name = models.CharField(max_length=100)
    length = models.IntegerField()
    track_index = models.IntegerField()
    artist = models.ForeignKey(
        Artist,
        related_name='tracks',
        on_delete=CASCADE
    )
    release = models.ManyToManyField(
        Release,
        related_name='tracks',
        blank=True
    )
    genres = models.ManyToManyField(
        Genre, 
        related_name='tracks', 
        blank=True
    )
    links = models.ManyToManyField(
        Link,
        related_name='tracks',
        blank=True
    )
    favorited_by = ManyToManyField(
        User,
        related_name='favorite_tracks',
        blank=True
    )
    owner = ForeignKey(
        User,
        related_name='track_owner',
        on_delete=CASCADE,
        null=True,
        default=1
    )

    def __str__(self):
        return f'{self.name}'
