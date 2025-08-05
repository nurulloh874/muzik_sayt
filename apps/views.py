from django.shortcuts import render, get_object_or_404
from .models import Muzika, Comment, Kategory
from rest_framework import viewsets
from .models import Muzika, Kategory, Comment, CommentLike, MuzikaLike
from .serializers import *


def home(request):
    musics = Muzika.objects.all()
    return render(request, 'index.html', {'musics': musics})

def music_detail(request, pk):
    music = get_object_or_404(Muzika, pk=pk)
    comments = music.comments.all()
    return render(request, 'music_detail.html', {'music': music, 'comments': comments})


class MuzikaViewSet(viewsets.ModelViewSet):
    queryset = Muzika.objects.all()
    serializer_class = MuzikaSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def index(request):
    category_id = request.GET.get('category')
    categories = Kategory.objects.all()

    if category_id:
        musics = Muzika.objects.filter(category_id=category_id)
        selected_category = get_object_or_404(Kategory, id=category_id)
    else:
        musics = Muzika.objects.all()
        selected_category = None

    return render(request, 'index.html', {
        'categories': categories,
        'musics': musics,
        'selected_category': selected_category
    })


