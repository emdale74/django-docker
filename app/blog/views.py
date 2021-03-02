from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Article, Comment
from .forms import CommentForm, EditArticle


def index(request):
    latest_articles_list = Article.objects.order_by('-submission_date')[:5]
    context = {'latest_articles_list': latest_articles_list}
    return render(request, 'articles/index.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        comment_model = Comment()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_model.description = form.cleaned_data['description']
            comment_model.article_fk = article
            comment_model.save()
    try:
        comments = Comment.objects.filter(article_fk=article_id)
    except Comment.DoesNotExist:
        comments = ""
    comment_form = CommentForm(initial={'article_fk': article_id})
    context = {'article': article, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'articles/detail.html', context)


def edit(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        comment_model = Comment()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_model.description = form.cleaned_data['description']
            comment_model.article_fk = article
            comment_model.save()
    edit_form = EditArticle(initial={'title': article.title, 'description': article.description})
    context = {'edit_form': edit_form, 'article_id': article_id}
    return render(request, 'articles/edit.html', context)
