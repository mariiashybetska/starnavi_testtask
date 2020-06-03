from rest_framework import generics as g

from social_network.models import LikeDislike
from social_network.api.serializers import LikeSerializer


class LikesAnalytics(g.ListCreateAPIView):
    queryset = LikeDislike.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(vote=1)