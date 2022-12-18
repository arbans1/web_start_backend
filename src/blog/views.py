from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    """
    index 페이지를 보여줍니다.
    """

    # Post 모델에서 모든 Post 객체를 가져옵니다.
    posts = Post.objects.all().order_by('-pk')

    # return render(request=request, template_name="blog/index.html")

    # render 함수의 두 번째 인수로 context를 전달합니다.
    return render(request=request, template_name="blog/index.html", context={"posts": posts})
