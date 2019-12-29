from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    PAUL_PHEONIX = 'PP'
    LING_XIAOYU = 'LX'
    SHAHEEN = 'SH'
    CHAR_CHOICES = [
        (PAUL_PHEONIX, 'Paul Pheonix'),
        (LING_XIAOYU, 'Ling Xiaoyu'),
        (SHAHEEN, 'Shaheen')]

    main_char = models.CharField(
        max_length=2, 
        choices=CHAR_CHOICES, 
        default=PAUL_PHEONIX)
    

    def __str__(self):
        return self.username