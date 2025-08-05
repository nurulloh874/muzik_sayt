from django.contrib import admin
from .models import CustomUser, Kategory, Muzika, Comment, CommentLike, MuzikaLike
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Kategory)
admin.site.register(Muzika)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(MuzikaLike)
