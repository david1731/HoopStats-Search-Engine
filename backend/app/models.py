# -*- coding: utf-8 -*-
from app.dbmodels.models import *
from django.db import models

# Player Model
class Player(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Team Model (if needed)
class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Game Model
class Game(models.Model):
    date = models.DateField()
    home_team = models.ForeignKey(Team, related_name='home_games', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_games', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date}"


# Player Stats Model
class PlayerStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_starter = models.BooleanField(default=False)
    minutes = models.IntegerField()
    points = models.IntegerField()
    assists = models.IntegerField()
    offensive_rebounds = models.IntegerField()
    defensive_rebounds = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    turnovers = models.IntegerField()
    defensive_fouls = models.IntegerField()
    offensive_fouls = models.IntegerField()
    free_throws_made = models.IntegerField()
    free_throws_attempted = models.IntegerField()
    two_pointers_made = models.IntegerField()
    two_pointers_attempted = models.IntegerField()
    three_pointers_made = models.IntegerField()
    three_pointers_attempted = models.IntegerField()

    def __str__(self):
        return f"{self.player.name} in {self.game}"


# Shots Model
class Shots(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_made = models.BooleanField()
    location_x = models.FloatField()
    location_y = models.FloatField()

    def __str__(self):
        return f"Shot by {self.player.name} in {self.game} (Made: {self.is_made})"
