from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from groups.models import Group


class CreateGroupView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name', 'description']


class SingleGroup(DetailView):
    model = Group


class ListGroups(ListView):
    model = Group
