import readtime
from django.db import models
from tinymce import models as tinymce_models

STATUS = ((0, "Draft"), (1, "Publish"))


class PostManager(models.Manager):
    def change_status(self, pk, new_status):
        post = Post.objects.get(pk=pk)
        post.status = new_status
        post.save()


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    created_by = models.ForeignKey(
        "consumers.Consumer", on_delete=models.CASCADE, related_name="post_created_by"
    )
    updated_by = models.ForeignKey(
        "consumers.Consumer", on_delete=models.CASCADE, related_name="post_updated_by"
    )

    category = models.ForeignKey(
        "blog.Category", on_delete=models.CASCADE, related_name="blog_category"
    )

    keywords = models.CharField(max_length=255, null=True, blank=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    image_img = models.ImageField(upload_to="posts/", blank=True, null=True)
    image_link = models.URLField(max_length=255, blank=True, null=True)
    content = tinymce_models.HTMLField()

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    objects = PostManager()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_readtime(self):
        result = readtime.of_text(self.content)
        return result.text


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
