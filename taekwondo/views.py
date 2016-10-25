from django.shortcuts import render
from django.views import generic
from .models import Member


def index(request):
    return render(request, "taekwondo/index.html")


def member_list(request):
    return render(request, "taekwondo/member_list.html")


def competition_list(request):
    return render(request, "taekwondo/competition_list.html")


def user_list(request):
    return render(request, "taekwondo/user_list.html")


def team_list(request):
    return render(request, "taekwondo/team_list.html")


class IndexView(generic.ListView):
    template_name = 'taekwondo/index.html'
    context_object_name = 'members_list'

    def get_queryset(self):
        """Return the list of members."""
        return Member.objects.all  # order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Member
    template_name = 'taekwondo/detail.html'
