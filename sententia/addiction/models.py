from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



CONDITIONS = (
    (0, 'alcohol'),
    (10, 'Food'),
    (20, 'Tobacco'),
    (30, 'Drugs'),
    (40, 'Cannabis'),
    (50, 'Cocaine'),
    (60, 'Heroin'),
    (70, 'ATS'),
    (80, 'Gambling'),
    (90, 'Video Games'),
    (100, 'Internet'),
    (110, 'Sex'),
    (120, 'Shopping'),
    (130, 'Work'),
    (140, 'Masturbation'),
    (150, 'Illegal Drugs'),
    (160, 'Legal Drugs'),
    (170, 'Caffeine'),
    (180, 'Being Bitchy'),
    (190, 'masturbation'),
    (200, 'Marijuana'),
    (210, 'Nicotine'),
)

class Addictions(models.Model):
    user = models.ForeignKey(User, related_name="addictions")
    recorded_at = models.DateTimeField(default=timezone.now(), editable=False)

    condition = models.IntegerField(choices=CONDITIONS)
    notes = models.TextField(blank=True, null=True, default="")
    money = models.IntegerField(blank=True, null=True, default="")

    def __str__(self):
        return '{} for {}.' .format( self.recorded_at.strftime('%d-%m-%Y %H:%M:%S'),self.get_condition_display())

    class Meta:
        verbose_name = "Addiction"
        verbose_name_plural = "Addictions"