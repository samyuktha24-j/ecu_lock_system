from django.db import models

class ECU(models.Model):
    ecu_id = models.CharField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=64)  # store hash or encrypted version
    status = models.CharField(max_length=10, default="LOCKED")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ecu_id
