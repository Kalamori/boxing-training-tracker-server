from django.db import models

# Create your models here.
class Workout(models.Model):
    WORKOUT_TYPES = [
        ('shadowboxing', 'Shadowboxing'),
        ('bagwork', 'Bag work'),
        ('pad_work', 'Pad Work'),
        ('sparring', 'Sparring'),
        ('conditioning', 'Conditioning'),
        ('strength_training', 'Strength Training'),
        ('flexibility', 'Flexibility'),
        ('jump_rope', 'Jump Rope'),
        ('heavy_bag', 'Heavy Bag'),
        ('calisthenics', 'Calisthenics'),
        ('abdominal', 'Abdominal'),
        ('footwork', 'Footwork'),
        ('running', 'Running'),
        ('other', 'Other'),
    ]

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='owned_workouts', blank=True)
    workout_type = models.CharField(max_length=50, choices=WORKOUT_TYPES)
    date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.owner.username}'s {self.workout_type} on {self.date}"
    

