from django.db import models

# Create your models here.

class Round(models.Model):
    workout = models.ForeignKey('workouts.Workout', on_delete=models.CASCADE, related_name='rounds')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='owned_rounds', blank=True, null=True)
    round_number = models.PositiveIntegerField()
    time = models.PositiveIntegerField(help_text="Round duration in seconds")
    intensity = models.PositiveIntegerField(help_text="Intensity level from 1 to 10")
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Round {self.round_number} of {self.workout}"
    

