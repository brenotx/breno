from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(editable=False)
    content = models.TextField()
    author = models.ForeignKey('auth.User')
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['-created_at',]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug': slugify(self.title)})