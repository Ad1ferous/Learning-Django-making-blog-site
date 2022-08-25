from django.shortcuts import render, get_object_or_404
from .models import Post, Group

NUMBER_OF_LATEST_POSTS = 10


def index(request):
    posts = Post.objects.all()[:NUMBER_OF_LATEST_POSTS]
    template = 'posts/index.html'
    context = {
        'title': 'Последние обновления на сайте',
        'text': 'Это главная страница Yatube',
        'posts': posts,
    }

    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUMBER_OF_LATEST_POSTS]
    template = 'posts/group_list.html'
    context = {
        'title': f'Записи сообщества {group}',
        'text': 'Здесь будет информация о группах проекта Yatube',
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
