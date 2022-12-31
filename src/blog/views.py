# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.

class PostList(ListView):
    """
    PostList 뷰는 Post 모델의 모든 객체를 보여줍니다.
    """
    model = Post
    ordering = '-pk'
    # template_name = 'blog/index.html'
    # default template_name = 'blog/post_list.html'

class PostDetail(DetailView):
    """
    DetailView는 하나의 객체를 보여줍니다.
    """
    model = Post
    

'''
def index(request):
    """
    index 페이지를 보여줍니다.
    """

    # Post 모델에서 모든 Post 객체를 가져옵니다.
    posts = Post.objects.all().order_by("-pk")

    # return render(request=request, template_name="blog/index.html")

    # render 함수의 두 번째 인수로 context를 전달합니다.
    return render(request=request, template_name="blog/index.html", context={"posts": posts})
'''
'''
def single_post_page(request, pk):
    """
    single_post 페이지를 보여줍니다.
    """

    # Post 모델에서 pk에 해당하는 Post 객체를 가져옵니다.
    post = Post.objects.get(pk=pk)

    # render 함수의 두 번째 인수로 context를 전달합니다.
    return render(request=request, template_name="blog/single_post_page.html", context={"post": post})
'''
