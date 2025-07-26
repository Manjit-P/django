from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from accounts.models import CustomUser
from django.urls import reverse

category_choices = (
    ('D','Daily'),
    ('W','Montly'),
    ('M','Weekly'),
)

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE,)
    created_on = models.DateField(default=timezone.now)
    due = models.DateField(default=timezone.now)
    category = models.TextField(choices=category_choices, max_length= 1)
    completed = models.BooleanField(default= False)
    now = models.DateField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Task.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("task", kwargs={'slug' :self.slug})
