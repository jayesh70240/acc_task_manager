from rest_framework import serializers
from .models import UserData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["id", "email", "name", "password"]
        extra_kwargs = {
            'password': {'write_only': True} #hides the pass
        }

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data.update({
            "user": {
                "id": self.user.id,
                "name": self.user.name,
                "email": self.user.email,
            }
        })

        return data