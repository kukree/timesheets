from django.db import models
from company_panel.models import Company
from django.conf import settings
from manage_app.models import Task
from projects.models import Project
from datetime import date, time


class Entry(models.Model):
    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
        ordering = ['company', 'user', 'date']

    company = models.ForeignKey(Company, models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name='+')
    date = models.DateField(default=date.today)
    project = models.ForeignKey(Project, models.CASCADE, related_name='entries')
    task = models.ForeignKey(Task, models.CASCADE, related_name='+')
    notes = models.TextField(max_length=350, blank=True, default=' ')
    timer = models.TimeField(default=time(0, 0))
    start_time = models.TimeField(default=time(0, 0))
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.project.name
