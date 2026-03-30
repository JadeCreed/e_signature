from django.db import models

ROLE_CHOICES = (
    ('farmer', 'Farmer'),
    ('president', 'Brgy President'),
)

class User(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    barangay = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Planting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barangay = models.CharField(max_length=100)
    area_planted = models.FloatField()
    signature = models.TextField()  # ✅ ADD THIS
    created_at = models.DateTimeField(auto_now_add=True)
class Harvesting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barangay = models.CharField(max_length=100)
    area_harvested = models.FloatField()
    ave_yield = models.FloatField()
    volume = models.FloatField()
    signature = models.TextField()  # base64
    created_at = models.DateTimeField(auto_now_add=True)