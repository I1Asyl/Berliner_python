# users/admin.py
from django.contrib import admin
from .models import Team, Membership, Application, Post, Comment

class TeamAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'teamLeader']

class CommentAdmin(admin.ModelAdmin):
    fields = ['content', 'post', 'author']

class MembershipAdmin(admin.ModelAdmin):
    fields = ['member', 'team', 'isLeader', 'isEditor']   

class ApplicationAdmin(admin.ModelAdmin):
    fields = ['member', 'team']  

class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'team'] 

admin.site.register(Team, TeamAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)