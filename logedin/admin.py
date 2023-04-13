# users/admin.py
from django.contrib import admin
from .models import Team, Membership, Application, Post

class TeamAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'teamLeader']

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