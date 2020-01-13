from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

User = get_user_model()

# Create your models here.


class team(models.Model):
    userid = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    slug = models.SlugField(allow_unicode=True, unique=True)
    team_name = models.CharField(max_length=256, unique=True)
    team_motto = models.TextField()
    contact_no = models.CharField(max_length=10)
    location = models.CharField(max_length=256)
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.team_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.team_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("team:teamdetail", kwargs={"slug": self.slug})


class matchset(models.Model):
    match_date = models.DateTimeField()
    team1 = models.ForeignKey(team,related_name='one', blank=True, default='',on_delete=models.CASCADE)
    team2 = models.ForeignKey(team,related_name='two', blank=True, default='', on_delete=models.CASCADE)
    match_location = models.CharField(max_length=200)

    def __str__(self):
        return "{} VS {}".format(self.team1,self.team2)

    def get_absolute_url(self):
        return reverse("team:matchlist")
