from django.shortcuts import render
from program.models import Program
import datetime
import pytz
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .serializers import SubscribeSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, status, serializers



from sosn_global import settings
from .forms import EmailForm
from mailchimp_marketing import Client
from django.views.decorators.csrf import csrf_exempt
from mailchimp_marketing.api_client import ApiClientError
import mailchimp_marketing as MailchimpMarketing

mailchimp = Client()
mailchimp.set_config({
  'api_key': settings.MAILCHIMP_API_KEY,
  'server': settings.MAILCHIMP_REGION,
})

@csrf_exempt
def mailchimp_ping_view(request):
    response = mailchimp.ping.get()
    return JsonResponse(response)

def subscribe_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                member_info = {
                    'email_address': form_email,
                    'status': 'subscribed',
                }
                response = mailchimp.lists.add_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    member_info,
                )
                logger.info(f'API call successful: {response}')
                return redirect('subscribe-success')

            except ApiClientError as error:
                logger.error(f'An exception occurred: {error.text}')
                return redirect('subscribe-fail')

    return render(request, 'subscribe.html', {
        'form': EmailForm(),
    })


def subscribe_success_view(request):
    return render(request, 'message.html', {
        'title': 'Successfully subscribed',
        'message': 'Yay, you have been successfully subscribed to our mailing list.',
    })


def subscribe_fail_view(request):
    return render(request, 'message.html', {
        'title': 'Failed to subscribe',
        'message': 'Oops, something went wrong.',
    })


def unsubscribe_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data['email']
            # TODO: use Mailchimp API to unsubscribe
            return redirect('unsubscribe-success')

    return render(request, 'unsubscribe.html', {
        'form': EmailForm(),
    })


def unsubscribe_success_view(request):
    return render(request, 'message.html', {
        'title': 'Successfully unsubscribed',
        'message': 'You have been successfully unsubscribed from our mailing list.',
    })


def unsubscribe_fail_view(request):
    return render(request, 'message.html', {
        'title': 'Failed to unsubscribe',
        'message': 'Oops, something went wrong.',
    })

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


   if request.method == 'POST':
      data = request.data or request.query_params
      
      form = EmailForm(request.POST)
      if form.is_valid():
         try:
            form_email = form.cleaned_data['email']
            member_info = {
               'email_address': form_email,
               'status': 'subscribed',
               "merge_fields": {
                  "FNAME": str(form_email).split('@')[0]
               }
            }

            try:
               response = mailchimp.lists.add_list_member(list_id, member_info)
               print("response: {}".format(response))
            except ApiClientError as error:
               print("An exception occurred: {}".format(error.text))
               
         except Exception as e:
            pass



   context = {
      "latest_program": up_coming_program,
      "up_coming_program": up_coming_program,
      "programs": programs,
      "current_date": current_date,
      'subscribe_form': EmailForm(),
   }

   return render(request=request,
                 template_name='index.html', context=context)

audience_list_id = settings.MAILCHIMP_MARKETING_AUDIENCE_ID

@api_view(['POST'])
def subscribe(request):
    data = request.data or request.query_params
    serializer =  SubscribeSerializer(data= data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        
        try:
            member_info = {
               'email_address': email,
               'status': 'subscribed',
               "merge_fields": {
                  "FNAME": str(email).split('@')[0]
               }
            }
            
            try:
                response = mailchimp.lists.add_list_member(
                    audience_list_id, member_info)
                
            except ApiClientError as error:
               
               Response({
                    'code': 400,
                    'status': 'Bad Request',
                    'message': error.text
                }, status.HTTP_400_BAD_REQUEST)

            return Response({
                        'code': 200,
                        'status': 'Successfully added to List',
                        'message': 'Success! Email has been added to our Mailing List.',
                        'email': email
                    }, status.HTTP_200_OK)

            
                    
        except ApiClientError as error:
                print("An exception occurred: {}".format(error.text))
                Response({
                    'code': 400,
                    'status': 'Bad Request',
                    'message': "error.text"
                }, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
                        'code': 400,
                        'status': 'Bad Request',
                        'message': 'Invalid email address, please confirm that your email is valid!'
                        }, status.HTTP_400_BAD_REQUEST)


def contact(request):
    
   context = {}

   return render(request=request,
                 template_name='contact.html', context=context)

