from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import authentication,permissions
from .serializers import *
from .permissions import *
from django.utils import timezone
from django.contrib.auth.hashers import make_password

# class DefaultMixin(object):
#
#     authentication_classes = (
#         authentication.BasicAuthentication,
#         authentication.TokenAuthentication,
#     )
#
#     permission_classes = (
#        permissions.IsAuthenticated,
#
#     )



class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'players': reverse(PlayerList.name,
            request=request),
            'game-categories': reverse(GameCategoryList.name,
            request=request),
            'games': reverse(GameList.name,
            request=request),
            'scores': reverse(ScoreList.name,
            request=request),
            'users': reverse(UserList.name,
            request=request)

        })

class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'


class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'

    def perform_create(self, serializer):
        games = GameCategory.objects.all()
        serializer.save(owner=User.objects.get(pk=6).player,
                        game_category=games[0])


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'

    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsOwnerOrReadOnly
    # )


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'

    # def perform_create(self, serializer):
    #     usuario = User.objects.get(username=self.request.data['user'])
    #     player = Player(created=timezone.now(),
    #                     telefone=self.request.data['telefone'],
    #                     gender=self.request.data['gender'],
    #                     user_id=usuario.id,
    #                     first_name=usuario.first_name,
    #                     last_name=usuario.last_name
    #                     )
    #     player.save()
        #serializer.save(player=player)

    # def perform_create(self, serializer):
    #     senha = make_password("%s" % self.request.data['password'])
    #     usuario = User(username=self.request.data['username'],
    #              first_name=self.request.data['first_name'],
    #              last_name=self.request.data['last_name'],
    #              email=self.request.data['email'],
    #              password=senha,
    #              last_login=timezone.now(),
    #              is_superuser=False,
    #              is_staff=True,
    #              is_active=True,
    #              date_joined=timezone.now())
    #
    #     usuario.save()
    #     serializer.save(user=usuario)


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'


class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-list'


class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-detail'


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

    def perform_create(self, serializer):
        senha = make_password("%s" % self.request.data['password'])

        serializer.save(username=self.request.data['username'],
                     first_name=self.request.data['first_name'],
                     last_name=self.request.data['last_name'],
                     password=senha,
                     last_login=timezone.now(),
                     is_superuser=False,
                     is_staff=True,
                     is_active=True,
                     date_joined=timezone.now())

        usuario_criado = User.objects.get(username=self.request.data['username'])
        player = Player(created=timezone.now(),
                        telefone=None,
                        gender=None,
                        user_id=usuario_criado.id,
                        first_name=usuario_criado.first_name,
                        last_name=usuario_criado.last_name)

        player.save()
        print("Salvou Player")





class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

