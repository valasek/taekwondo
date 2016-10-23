from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Member


class IndexView(generic.ListView):
    template_name = 'taekwondo/index.html'
    context_object_name = 'members_list'

    def get_queryset(self):
       """Return the list of members."""
       return Member.objects.all  # order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Member
    template_name = 'taekwondo/detail.html'
