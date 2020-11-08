from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:  #configure serializer to point to a specific model in the profilesproject
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password' : {
                'write_only': True, #Only used to create new objects or update objects. Not for retrieving objects
                'style': {'input_type': 'password'}

            }
         }

         #overriding the create function of the object manager. We need it to use the create_user function instead of the create
         # function. We do that so that password is created as a hash instead of the cleartext password of the default create.
    def create(self, validated_data):
        """Create and return a new user """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


    def update(self, instance, validated_data):
        """Handle updating user account """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance,validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')

        # Users should not create new user profile while adding feed data. Only authenticated user can be assigned new feed data

        extra_kwargs = {'user_profile':{'read_only': True}}
