from django.shortcuts import render
from program.models import Program
import datetime
import pytz

# Create your views here.
def index(request):
   programs = Program.objects.filter(feature =True).all()[:6]
   up_coming_program = []
   all_programs = Program.objects.all().order_by('-id')
   for i in all_programs:
      if i.not_started:
         try:
            up_coming_program.append(i)
         except Exception as e:
            continue

   current_date = datetime.datetime.now(pytz.utc)

   context = {
      "latest_program": up_coming_program[0],
      "up_coming_program": up_coming_program,
      "programs": programs,
      "current_date": current_date
   }

   return render(request=request,
                 template_name='index.html', context=context)

def contact(request):
    
   context = {}

   return render(request=request,
                 template_name='contact.html', context=context)
