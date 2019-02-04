from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    created = models.DateTimeField(auto_now_add=True)
    # username = models.CharField(max_length=50)
    # password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    # email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE,)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return ("%s %s")%(self.first_name,self.last_name)




class Game(models.Model):
    owner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='games')
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    game_category = models.ForeignKey('GameCategory',on_delete=models.CASCADE, related_name='games')
    release_date = models.DateTimeField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Score(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='scores')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()
    score_date = models.DateTimeField()

    class Meta:
        ordering = ('-score',)

class GameCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name