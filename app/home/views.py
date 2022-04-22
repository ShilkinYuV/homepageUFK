from django.shortcuts import render
import datetime
from .models import *

def home(request):
	now = datetime.datetime.now()
	duty = DutyForToday.objects.filter(date=now)
	messages = Messages.objects.filter(date_end__gte=now)
	sysppo = PPO.objects.all()
	# print(duty.kabinet_five)
	node = Node.objects.all().order_by('-id')
#  [:4]
	date_dict = dict()
	date_dict['node'] = node
	date_dict['duty'] = duty
	date_dict['sysppo'] = sysppo
	date_dict['messages'] = messages

	return render(request, 'home/index.html', date_dict)
