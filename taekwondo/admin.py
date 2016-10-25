from django.contrib import admin

# Register your models here.
from .models import Competition, Member, Team, Level, Sex, MemberCompetition
from .models import Tki, Tull, Matsogi, Wirok

admin.site.register(Competition)
admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Tki)
admin.site.register(Tull)
admin.site.register(Matsogi)
admin.site.register(Wirok)
admin.site.register(Sex)
admin.site.register(Level)
admin.site.register(MemberCompetition)
