from rest_framework import serializers
from .models import Muzika, Kategory, Comment, CommentLike, MuzikaLike, CustomUser

class KategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategory
        fields = '__all__'

class MuzikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muzika
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'

class MuzikaLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuzikaLike
        fields = '__all__'
