from django.contrib import admin

from groups.models import Group, GroupMember


class GroupMemberInline(admin.TabularInline):
    model = GroupMember


admin.site.register(Group)
