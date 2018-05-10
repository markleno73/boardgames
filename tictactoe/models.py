from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=models.CASCADE)
    second_player = models.ForeignKey(User, related_name="games_second_player", on_delete=models.CASCADE)
    next_to_move = models.ForeignKey(User, related_name="games_to_move", on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)