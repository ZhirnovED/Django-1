from django.db import models

# Create your models here.
class Article(models.Model):
    article_title = models.CharField('Статья', max_length=200)
    article_text = models.TextField('Контент')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Review(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Автор', max_length = 50)
    review_text = models.CharField('Текст комментария', max_length=200)
    rating_value = models.IntegerField('Рейтинг')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
