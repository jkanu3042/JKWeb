from django.db import models

# Create your models here.
from django.urls.base import reverse


class Post(models.Model):
    title = models.CharField('TITLE',max_length=40)
    slug = models.SlugField('SLUG', unique='True', allow_unicode=True, help_text='one word for title alias. ')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural='posts'
        db_table = 'free_board'
        ordering = ('-modify_date', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('free_board:post_detail', args=(self.slug, ))

