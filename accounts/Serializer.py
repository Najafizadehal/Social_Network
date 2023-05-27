from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password_1 = serializers.CharField(required=True)
    password_2 = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = (
            'email', 'username', 'password_1', 'password_2',
            'first_name', 'last_name'
        )

        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

        def Validator(self, attrs):
            if attrs['password_1'] != attrs['password_2']:
                raise serializers.ValidationError({
                    'password': 'password did not match.'
                })
            return super(RegisterSerializer, self).Validator(attrs)

        def create(self, validate_data):
            user = User.object.create_user(
                username=validate_data['username'],
                email=validate_data['email'],
                first_name=validate_data.get('first_name', ''),
                last_name=validate_data.get('last_name', ''),
                password=validate_data['password_1']
            )

            # user.set_password(validate_data['password_1'])
            # user.save()

            return user
