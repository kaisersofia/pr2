from django.db import models

class NewsCategory(models.Model):
    category_name = models.CharField(max_length=32)
    category_date = (models.IntegerField())

    def __str__(self):
        return str(self.category_name)

class News(models.Model):
    news_title = models.CharField(max_length=56)
    news_text = models.TextField()
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.news_title)

