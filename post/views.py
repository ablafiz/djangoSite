from django.shortcuts import render
from django.http import HttpResponse, response
from post.models import *
from house.models import *

# Create your views here.
def post_list(request):
    #return render(request, 'post/post_list.html', {})
    return HttpResponse("test")

def myname(request):
    students = Student.objects.all()
    posts = Post.objects.all()
    houses = House.objects.all()

    post = posts
    student = students
    context = {
        'student': student,
        'post': post,
        'house':houses

    }
    return render(request, 'post/post_list.html', context)