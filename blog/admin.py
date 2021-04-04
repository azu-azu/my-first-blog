from django.contrib import admin
from .models import Post

# モデルをadmin（管理画面）上で見えるようにするため、モデルを登録する
admin.site.register(Post)