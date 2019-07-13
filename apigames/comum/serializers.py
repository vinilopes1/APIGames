from rest_framework import serializers
from .models import *

class GameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCategory
        fields = (
            'id',
            'name',
            'description',
        )

class PlayerGameSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Game
        fields = ('url','name')

class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    first_name = serializers.CharField(write_only=False, read_only=True)
    last_name = serializers.CharField(write_only=False, read_only=True)
    games = PlayerGameSerializer(many=True,read_only=True)

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
            'games',
            'qtd_games'
        )



class GameSerializer(serializers.ModelSerializer):

    # game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),
    #                          slug_field='name')
    #owner = PlayerSerializer()

    class Meta:
        model = Game
        fields = (
            'url',
            'id',
            'name_category',
            'game_category',
            'name',
            #'owner',
            'name_owner',
            'release_date',)

        read_only_fields = ('release_date','game_category' )

        #extra_kwargs = {'game_category':{'write_only': True}}


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



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'first_name', 'last_name', 'player')

        read_only_fields = ('player', )





# class PlayerUserSerializer(serializers.HyperlinkedModelSerializer):
#
#
#     class Meta:
#         model = User
#         fields = ('url','username','first_name','last_name')







