from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django. urls import reverse

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .serializers import ReviewSerializer

from .forms import ReviewFilter

from .models import Article, Review

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'main/index.html', {'articles': articles})

def detail(request, article_id):
    try:
        content = Article.objects.get(id=article_id)
    except:
        raise Http404('')

    reviews = content.review_set.order_by('-id')

    form = ReviewFilter(request.GET)

    if form.is_valid():
        if form.cleaned_data['min_rating']:
            reviews = reviews.filter(rating_value__gte=form.cleaned_data['min_rating'])

        if form.cleaned_data['max_rating']:
            reviews = reviews.filter(rating_value__lte=form.cleaned_data['max_rating'])

        if form.cleaned_data['author_name']:
            reviews = reviews.filter(author_name__icontains=form.cleaned_data['author_name'])

        if form.cleaned_data['review_text']:
            reviews = reviews.filter(review_text__icontains=form.cleaned_data['review_text'])



    return render(request, 'main/detail.html', {'content': content, 'reviews':reviews, "form":form})

def review(request, article_id):
    try:
        content = Article.objects.get(id=article_id)
    except:
        raise Http404('')

    return render(request, 'main/review.html', {'content': content})
def leave_comment(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404('')

    article.review_set.create(author_name = request.POST['name'], review_text = request.POST['text'], rating_value = request.POST['rating'] )

    return HttpResponseRedirect(reverse('main:detail', args=(article.id,)) )


# =============== API

class ReviewApiView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # parser_classes = (MultiPartParser, FormParser, JSONParser)
    http_method_names = ['get', 'post']