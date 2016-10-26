from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Member
from .forms import MemberForm
import logging
from django.http import JsonResponse


# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    return render(request, "taekwondo/index.html")


def member_list(request):
    logger.warning("Calling member_list")
    members = Member.objects.all()
    count = len(members)
    return render(request, "taekwondo/member_list.html", {'members': members, 'count': count})


def member_edit(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, "taekwondo/member_edit.html", {'member': member})


def member_new(request):
    logger.warning("Calling member_new")
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('member_list'))
    else:
        form = MemberForm()
    return render(request, "taekwondo/member_new.html", {'form': form})


def member_delete(request):
    logger.warning("Calling member_delete")
    if request.method == 'POST':
        if request.is_ajax():
            id = request.POST.get("id")
            member = get_object_or_404(Member, pk=id)
            member.delete()
            return JsonResponse({'id': id})
    else:
        return JsonResponse({"success": False, "error": {"code": 123, "message": "An error occurred!"}})


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
