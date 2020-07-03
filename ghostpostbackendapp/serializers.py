from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Post


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["content", "is_boast", "up_votes", "down_votes",
                  "total_votes", "submit_time", "secret_key", 'id']
