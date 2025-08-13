from django.db import models

# 在此处定义我们的模型，用于告诉Django在应用程序中存储的数据。

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
