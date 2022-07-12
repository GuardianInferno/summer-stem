from rest_framework import serializers
from .models import userInfo, objectInfo

class ObjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = objectInfo
        fields = (
            "object_name",
            "object_amount",
            "object_price",

        )


class UserInfoSerializer(serializers.ModelSerializer):
    object_info = ObjectInfoSerializer(many=True)
    class Meta:
        model = userInfo
        fields = (
            "id",
            "username",
            "money",
            "join_date",
            'object_info'
        )

