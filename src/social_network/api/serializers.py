from rest_framework import serializers

from social_network.models import LikeDislike


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikeDislike
        fields = ('vote',
                  'user',
                  'content_type',
                  'object_id',
                  'content_object',
                  'objects')
