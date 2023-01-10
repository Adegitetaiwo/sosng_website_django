from genericpath import exists
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, status, serializers



from .models import PassCode, Program, ProgramResource
from django.urls import reverse_lazy
from django.utils import timezone as tz

from .serializers import PassCodeSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class programListView(ListView):
    model = Program

class programDetailView(DetailView):
    model = Program

    # override get_context_data to pass in all extra
    def get_context_data(self, **kwargs):
        context = super(programDetailView, self).get_context_data(**kwargs)
        program_list = Program.objects.all().order_by('-id')[:6]
        current_time = tz.now()
        print(current_time)
        context['program_list'] = program_list
        context['current_time'] = current_time

        return context


def classroom(request):
    
   context = {}

   return render(request=request,
                 template_name='classroom.html', context=context)


@csrf_exempt
@api_view(['POST'])
def passCode(request):
    
    data = request.data or request.query_params
    serializer =  PassCodeSerializer(data= data)
    
    if serializer.is_valid():
        program_id = serializer.validated_data['id']
        code = serializer.validated_data['code']
        
        try:
            if Program.objects.filter(id=program_id).exists():
                object = Program.objects.filter(id = program_id)[0]
                if PassCode.objects.filter(program = object).exists() and PassCode.objects.filter(program=object)[0].code == code:
                    resource = ProgramResource.objects.filter(program = object).all().order_by('id')
                    
                    return Response({
                        'code': 200,
                        'status': 'success',
                        'message': 'Passcode is valid',
                        'resource': resource.values()
                    }, status.HTTP_200_OK)

                else:
                    return Response({
                        'code': 400,
                        'status': 'Bad request',
                        'message': 'Passcode is Invalid'
                    }, status.HTTP_400_BAD_REQUEST)


        except Exception as e:
            raise serializers.ValidationError({
                'error': f'{e}'
            })
    else:
        raise serializers.ValidationError(
            serializer.errors
        )