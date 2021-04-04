from django.conf import settings
from django.db import models
from django.utils import timezone

# class：オブジェクトの定義、Post：モデル名（大文字で始める）
# models.Model：ポストがdjangoModel、djangoがこれはデータベースに保存すべきものとわかるようにしている
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) # 他のモデルへのリンク
    title = models.CharField(max_length=200) # 文字数が制限されたテキストを定義するフィールド
    text = models.TextField() # 制限無しの長いテキスト用
    created_date = models.DateTimeField(default=timezone.now) # 日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)

    # ブログを公開するメソッド、classにインデントする（モデルのメソッド）
    def publish(self):
        self.published_date = timezone.now()
        self.save

    def __str__(self):
        return self.title # メソッドは何かをリターンする