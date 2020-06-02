from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db.models import Sum


class User(AbstractUser):

    def get_user_endpoint(self):
        last_request = Logger.objects.filter(user=self).last().created
        last_login = self.last_login
        return f'user:{self.username}, last login: {last_login}, last request: {last_request}'


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # We take the queryset with records greater than 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # We take the queryset with records less than 0
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        # We take the total rating
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def posts(self):
        return self.get_queryset().filter(content_type__model='Post')


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Dislike'),
        (LIKE, 'Like')
    )

    vote = models.SmallIntegerField(choices=VOTES)
    user = models.ForeignKey('social_network.User',
                             on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()


class Post(models.Model):
    author = models.ForeignKey('social_network.User',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    votes = GenericRelation(LikeDislike, related_query_name='posts')


class Logger(models.Model):
    user = models.ForeignKey('social_network.User',
                               on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)



