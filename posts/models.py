import uuid

from PIL import Image
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from users.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/')
    slug = models.SlugField(max_length=50, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug


@receiver(post_save, sender=User)
def set_user_post(sender, instance, *args, **kwargs):
    if kwargs.get('created', False):
        Post.objects.create(user=instance)


@receiver(post_save, sender=Post)
def set_image_post(sender, instance, *args, **kwargs):
    if instance.image:
        img = Image.open(instance.image.path)
        if img.height > 300 and img.width:
            size = (300, 300)
            img.thumbnail(size)
            img.save(instance.image.path)


@receiver(pre_save, sender=Post)
def set_slug_post(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)
        while Post.objects.filter(slug=slug).exists():
            slug = slugify(
                f'{instance.title}-{str(uuid.uuid4())[:8]}'
            )
        instance.slug = slug
