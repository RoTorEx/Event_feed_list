from django.db import models


class User(models.Model):
    """Users."""

    first_name = models.CharField(max_length=64, verbose_name="First name")
    last_name = models.CharField(max_length=64, verbose_name="Second name")

    def __str__(self):
        return f"User: {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Post(models.Model):
    """Post."""

    title = models.CharField(max_length=256, verbose_name="Post")
    content = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="post")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-date_create",)


class Achievement(models.Model):
    """Achievement."""

    title = models.CharField(max_length=256, verbose_name="Achievement")
    condition = models.CharField(max_length=512, verbose_name="Condition")
    image = models.ImageField(upload_to="achievement_image", verbose_name="Image")

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="achievement")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Achievement"
        verbose_name_plural = "Achievement"
        ordering = ("user",)


class Advertising(models.Model):
    """Advertisements."""

    title = models.CharField(max_length=256, verbose_name="Advertising")
    content = models.TextField()
    image = models.ImageField(upload_to="advertising_image", verbose_name="Image")
    url = models.URLField(max_length=1024)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Advertising"
        verbose_name_plural = "Advertising"
        ordering = ("-date_create",)
