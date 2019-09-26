from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
import requests
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .forms import UserForm
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes, renderer_classes, authentication_classes
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from core.models import Province, Program, FiveW, District, GapaNapa


# Create your views here.


def login_test(request):
    user = authenticate(username='sumit', password='sumit1234')

    # return HttpResponse(user)
    return HttpResponse(request.user.has_perm('core.can_add_district'))


@login_required()
def uploadData(request):
    if "GET" == request.method:
        return render(request, 'dashboard.html')
    else:
        csv = request.FILES["csv_file"]
        df = pd.read_csv(csv)
        upper_range = len(df)
        org_col = df['ORGANIZATION NAME']

        try:
            # fiveData = [
            #     FiveW(
            #         program_name=Program.objects.get(program_name='Naxa'),
            #         partner_name=Partner.objects.get(partner_name='Naxa')
            #     ) for row in range(0, 2)

            # sdaadassda sadsad

            # ]
            # five = FiveW.objects.bulk_create(fiveData)
            # list = []
            # for row in range(0, upper_range):

            # try:
            #     imp_partner_1 = Partner.objects.get(program_name=df['IMPLEMENTING PARNTER 1'][row])
            #
            # except:
            #     imp_partner_1 = None
            #
            #
            # try:
            #     imp_partner_2 = Partner.objects.get(program_name=df['IMPLEMENTING PARTNER2'][row])
            #
            # except:
            #     imp_partner_2 = None
            #
            # try:
            #     imp_partner_3 = Partner.objects.get(program_name=df['IMPLEMENTING PARTNER 3'][row])
            #
            # except:
            #     imp_partner_3 = None
            #
            # try:
            #     program = Program.objects.get(program_name=df['PROGRAMME NAME'][row])
            #
            # except:
            #     program = None
            #
            # try:
            #     district = District.objects.get(program_name=df['DISTRICT'][row])
            #
            # except:
            #     district = None
            #
            # try:
            #     nagarpalika = GapaNapa.objects.get(program_name=df['Nagarpalika'][row])
            #
            # except:
            #     nagarpalika = None

            # FiveW.objects.create(fiveData)

            return HttpResponse(df['ORGANIZATION NAME'][0])
        except Exception as e:
            return HttpResponse(e)


def ShapefileUpload(request):
    if "GET" == request.method:

        return render(request, 'shapefile.html')
    else:
        shapefile = request.FILES["shapefile"]
        url = 'http://139.59.67.104:8080/geoserver/rest/workspaces/Naxa/datastores/river/file.shp'
        headers = {
            'Content-type': 'application/zip',
        }
        response = requests.put(url, headers=headers, data=shapefile, auth=('admin', 'geoserver'))
        # print(response)
        return HttpResponse(response.status_code)


def Invitation(request):
    if "GET" == request.method:
        form = UserForm()
        return render(request, 'adduser.html', {'form': form})
    else:
        subject = 'Thank you for registering to our site'
        message = render_to_string('mail.html', {'context': 'values'})
        recipient_list = ['rounnn8@gmail.com']
        email = EmailMessage(
            subject, message, 'from@example.com', recipient_list
        )
        email.content_subtype = "html"
        mail = email.send()

        return HttpResponse(mail)


@authentication_classes([SessionAuthentication, ])
@api_view()
def auth(request):
    user = request.user
    # return HttpResponse(user)

    if user is None:
        return Response({'error': 'Please authorize first'},
                        status=HTTP_400_BAD_REQUEST)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


def check_login(request):
    if "GET" == request.method:
        form = UserForm()
        return render(request, 'adduser.html', {'form': form})
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        users = authenticate(request, username=username, password=password)
        if users is not None:
            login(request, users)
            return HttpResponse(request.user)
        else:
            return HttpResponse("login failed")


def province_list(request):
    template_name = 'province_list.html'
    province = Program.objects.order_by('id')
    data = {}
    data['object_list'] = province
    data['sumit'] = 'province'
    return render(request, template_name, data)
