from django.shortcuts import render
from .forms import *
from .models import *
from django.views.generic import DetailView

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()

    news = News.objects.all()

    admissionform = AdmissionForm()
    data = {
        'news': news,
        'admissionform': admissionform
    }
    return render(request, 'main/index.html', data)

def blog(request):

    news = Blog.objects.all()

    data = {
        'blog': news
    }
    return render(request, 'main/blog.html', data)

def courses(request):
    news = News.objects.all()
    courses = Courses.objects.all()
    data = {
        'courses': courses,
        'news': news
    }
    return render(request, 'main/courses.html', data)

class NewsDetailView(DetailView):
    model = News
    template_name = 'main/news-detail.html'
    context_object_name = 'news'