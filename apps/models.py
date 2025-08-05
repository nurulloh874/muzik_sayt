from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user
class CustomUser(AbstractUser):
    klik_status = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# Kategoriya
class Kategory(models.Model):
    category_nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.category_nomi


# Musiqa
class Muzika(models.Model):
    muzika_nomi = models.CharField(max_length=255)
    muzika_url = models.URLField()
    category = models.ForeignKey(Kategory, on_delete=models.CASCADE, related_name="music")

    def __str__(self):
        return self.muzika_nomi


# Kommentariya
class Comment(models.Model):
    comment = models.TextField()
    muzika = models.ForeignKey(Muzika, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.comment[:20]}"


# Kommentlarga like
class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} liked comment {self.comment.id}"


# Musiqalarga like
class MuzikaLike(models.Model):
    muzika = models.ForeignKey(Muzika, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} liked {self.muzika.muzika_nomi}"
