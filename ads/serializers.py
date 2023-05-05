from rest_framework import serializers

from .models import Ad


class IsPublishedTrueValidator:
    def __call__(self, value):
        if value:
            raise serializers.ValidationError('This field cannot be True')


class LongerThanTenCharValidator:
    def __call__(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Name of ad cannot be less than 10 characters.')


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'name', 'author', 'price']


class AdRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    desc = serializers.CharField(required=False)
    is_published = serializers.BooleanField(validators=[IsPublishedTrueValidator()])
    name = serializers.CharField(validators=[LongerThanTenCharValidator()])

    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

    def save(self, **kwargs):
        ad = super().save()

        if self.context['request'].user != self.initial_data['author']:
            ad.author = self.context['request'].user

        ad.save()
        return ad


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id']
