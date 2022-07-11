from rest_framework import serializers
from .models import userInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = userInfo
        fields = (
            "id",
            "username",
            "money",
            "join_date",
        )