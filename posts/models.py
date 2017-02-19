from django.db import models

# Create your models here.
from users.models import Users


class Post(models.Model):
    post = models.CharField(max_length=1000, null=False)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, related_name='posts', db_index=True)

    def to_json(self, keys=[]):
        data = {
            'post': self.post,
            'likes': self.likes,
            'created_at': self.created_at,
            'id': self.id
        }
        if 'user' in keys:
            data['user'] = self.user.to_json()

        if 'comments' in keys:
            data['comments'] = [c.to_json(keys=['user']) for c in self.comments.all().order_by('-updated_at')]

        return data


class Comment(models.Model):
    comment = models.CharField(max_length=100, null=False)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, related_name='comments')
    user = models.ForeignKey(Users, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self, keys=[]):
        data = {
            'id':self.id,
            'comment': self.comment,
            'likes': self.likes,
            'created_at': self.created_at
        }
        if 'user' in keys:
            data['user'] = self.user.to_json()

        if 'post' in keys:
            data['post'] = self.post.to_json()

        return data
