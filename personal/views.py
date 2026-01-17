from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article

# Create your views here.
def home(request):
    # This fetches all articles from the database
    articles = Article.objects.all()
    return render(request, 'personal/index.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    return render(request, 'personal/article.html', {
        'article': article
    })

@login_required
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'personal/dashboard.html', {
        'articles': articles
    })

@login_required
def add_article(request):
    if request.method == "POST":
        Article.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            published_date=request.POST.get('published_date'),
            author=request.user
        )
        return redirect('personal/dashboard')
    return render(request, 'personal/add-article.html')

@login_required
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)

    if request.method == "POST":
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.published_date = request.POST.get('published_date')
        article.save()

        return redirect('personal/dashboard')

    return render(request, 'personal/edit-article.html', {
        'article': article
    })


