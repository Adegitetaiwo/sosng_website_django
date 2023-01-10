from django.shortcuts import render
from program.models import Program
import datetime
import pytz

# Create your views here.
def index(request):
   latest_program = Program.objects.filter(feature = True).last()
   programs = Program.objects.all()[:6]
   current_date = datetime.datetime.now(pytz.utc)

   context = {
      "latest_program": latest_program,
      "programs": programs,
      "current_date": current_date
   }

   return render(request=request,
                 template_name='index.html', context=context)

def contact(request):
    
   context = {}

   return render(request=request,
                 template_name='contact.html', context=context)
