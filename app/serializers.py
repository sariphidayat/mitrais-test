from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [f.name for f in User._meta.fields]

    def validate_mobile_number(self, data):
        mobile_number = data
        mobile_number_length = len(mobile_number)
        if (
            not mobile_number.startswith('628') and
                not mobile_number.startswith('08')
        ) or (mobile_number_length < 11 and mobile_number.startswith('628')) \
            or (mobile_number_length < 10 and mobile_number.startswith('08')) \
                or not mobile_number.isnumeric():
            raise serializers.ValidationError(
                "Please enter a valid Indonesian mobile number.")

        return data
