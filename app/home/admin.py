from django.contrib import admin

from django.contrib import admin
from .models import Node, DutyForToday, PPO, NumbersPhone, Messages


admin.site.register(Node)
admin.site.register(DutyForToday)
admin.site.register(PPO)
admin.site.register(NumbersPhone)
admin.site.register(Messages)

