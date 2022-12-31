from django.db import models
from django.urls import reverse


class Post(models.Model):
    """
    블로그 포스트를 위한 모델입니다.

    모델 클래스 자체를 수정할 경우 makemigrations, migrate를 다시 해야 합니다. 다만 __str__ 메서드를 수정하는 경우에는 makemigrations를 할 필요가 없습니다.
    """

    title = models.CharField(max_length=30)  # 제목입니다. 최대 30자까지 허용합니다.
    content = models.TextField()  # 내용입니다. 제한 없이 허용합니다.
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일입니다. 자동으로 현재 시간이 저장됩니다.
    updated_at = models.DateTimeField(auto_now=True)  # 수정일입니다. 자동으로 현재 시간이 저장됩니다.

    # 작성자(author): 추후 추가 예정

    def __str__(self):
        """
        포스트 목록에서 보이는 부분입니다.
        """

        result = f"[{self.pk}] {self.title} ({self.created_at})"
        return result

    def get_absolute_url(self):
        """
        Post 객체의 상세 페이지로 이동할 수 있는 URL을 반환합니다.
        """
        return reverse("single_post_page", args=[self.pk])
