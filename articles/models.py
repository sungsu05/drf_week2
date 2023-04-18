from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField(null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)