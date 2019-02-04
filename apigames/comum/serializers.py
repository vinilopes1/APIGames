from rest_framework import serializers
from .models import *

class GameSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user.username')
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),
                             slug_field='name')

    class Meta:
        model = Game
        fields = (
            'url',
            'id',
            'game_category',
            'name',
            'owner',
            'release_date',)


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.SlugRelatedField(queryset=Player.objects.all(), slug_field="first_name")
    game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field="name")
    class Meta:
        model = Score
        fields = (
            'url',
            'id',
            'score',
            'score_date',
            'player',
            'game',

        )



class UserSerializer(serializers.HyperlinkedModelSerializer):
    # games = PlayerGameSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'first_name', 'last_name', 'player')


class PlayerGameSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Game
        fields = ('url','name')

# class PlayerUserSerializer(serializers.HyperlinkedModelSerializer):
#
#
#     class Meta:
#         model = User
#         fields = ('url','username','first_name','last_name')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.CharField(write_only=False, read_only=True)
    last_name = serializers.CharField(write_only=False, read_only=True)
    #games = PlayerGameSerializer(many=True,read_only=True)

    class Meta:
        model = Player
        fields = (
            'url',
            'id',
            'first_name',
            'last_name',
            'telefone',
            'gender',
            'user',
        )


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameCategory
        fields = (
            'url',
            'name',
            'description',
        )




