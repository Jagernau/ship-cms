
from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='uploads/')

    def has_permission(self, user):
        try:
            user_file = UserFile.objects.get(user=user, file=self)
            return user_file.permission
        except UserFile.DoesNotExist:
            return None


    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_file = File.objects.get(pk=self.pk)
            if old_file.content != self.content:
                old_file.pk = None
                old_file.updated_at = timezone.now()
                old_file.save()
        super(File, self).save(*args, **kwargs)

class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    permission = models.CharField(max_length=255)
