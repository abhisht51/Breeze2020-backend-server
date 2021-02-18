from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
from events.models import Cultural_Events, Sports_Events, Technical_Events, UserManager, User, Event_Registrations , Payment, Accommodation
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.mail import send_mail

from events.serializers import Sports_Serializer
from events.serializers import Cultural_Serializer
from events.serializers import Technical_Serializer
from events.mailer import Mailer
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import random
import json
import uuid
# from django.core import serializers

# Create your views here.

def test(request):
    return HttpResponse('this is working')

def index(request):    
    return HttpResponse('lol is it done ???')


@api_view(["GET"])
def sports_events_get(request,name='cricket'):
    name = request.GET.get('name')
    sports_Data = get_object_or_404(Sports_Events, name=name) 
    serializer = Sports_Serializer(sports_Data)
    return Response(serializer.data)


@api_view(["GET"])
def sports_events_get_name_poster(request):
    sports_data = []
    for i in Sports_Events.objects.values('name','poster', 'category', 'team_size_min', 'team_size_max'):
        sports_data.append(i)
    return JsonResponse({'sports': sports_data})



@api_view(["POST"])
def sports_events_post(request):
    name = request.data.get('name')
    date = request.data.get('date')
    venue = request.data.get('venue')
    time = request.data.get('time')
    description = request.data.get('description')
    fees_amount = request.data.get('fees_amount')
    rules = request.data.get('rules')
    prize_money = request.data.get('prize_money')
    team_size = request.data.get('team_size')
    registration_link = request.data.get('registration_link')
    person_of_contact = request.data.get('person_of_contact')
    person_of_contactno = request.data.get('person_of_contactno')
    fees_snu = request.data.get('fees_snu')
    poster = request.data.get('poster')
    sports = Sports_Events(name=name, date=date, venue=venue, time=time, description=description,
                           fees_amount=fees_amount, rules=rules, prize_money=prize_money,
                           team_size=team_size, fees_snu=fees_snu, registration_link=registration_link,
                           person_of_contact=person_of_contact, person_of_contactno=person_of_contactno,
                           poster=poster
                           )
    sports.save()
    return HttpResponse('New Sports Event Added!')


# @api_view(["GET"])
# def cultural_events_get(request):
#     cultural_data = []
#     for i in Cultural_Events.objects.all().values():
#         cultural_data.append(i)
#     # print(cultural_data)
#     return JsonResponse({'cultural': cultural_data})

@api_view(["GET"])
def cultural_events_get_name_poster(request):
    cultural_data = []
    for i in Cultural_Events.objects.values('name','poster', 'category', 'team_size_min', 'team_size_max'):
        cultural_data.append(i)
    return JsonResponse({'cultural': cultural_data})

@api_view(["GET"])
def cultural_events_get(request):
    name = request.GET.get('name')
    cultural_Data = get_object_or_404(Cultural_Events, name=name) 
    serializer = Cultural_Serializer(cultural_Data)
    print(serializer.data)
    return Response(serializer.data)

@api_view(["POST"])
def technical_events_post(request):
    name = request.data.get('name')
    date = request.data.get('date')
    venue = request.data.get('venue')
    time = request.data.get('time')
    description = request.data.get('description')
    club = request.data.get('club')
    rules = request.data.get('rules')
    fees_snu = request.data.get('fees_snu')
    fees_amount = request.data.get('fees_amount')
    prize_money = request.data.get('prize_money')
    team_size = request.data.get('team_size')
    time_limit = request.data.get('time_limit')
    registration_link = request.data.get('registration_link')
    person_of_contact = request.data.get('person_of_contact')
    person_of_contactno = request.data.get('person_of_contactno')
    poster = request.data.get('poster')
    form_array = request.data.get('form_array')
    if(form_array=='success'):
        technical = Technical_Events(name=name, date=date, venue=venue, time=time,
                                description=description, club=club, rules=rules, fees_snu=fees_snu,
                                fees_amount=fees_amount, prize_money=prize_money, team_size=team_size,
                                time_limit=time_limit, registration_link=registration_link,
                                person_of_contact=person_of_contact, person_of_contactno=person_of_contactno,
                                poster=poster
                                )
        technical.save()
        return HttpResponse('New Technical Event Added!')
    else:
        return JsonResponse(form_array)



# @api_view(["GET"])
# def technical_events_get(request):
#     cultural_data = []
#     for i in Technical_Events.objects.all().values():
#         cultural_data.append(i)
#     return JsonResponse({'technical': cultural_data})

@api_view(["GET"])
def technical_events_get_name_poster(request):
    technical_data = []
    for i in Technical_Events.objects.values('name','poster', 'category', 'team_size_min', 'team_size_max'):
        technical_data.append(i)
    return JsonResponse({'technical': technical_data})

@api_view(["GET"])
def technical_events_get(request,name):
    name = request.GET.get('name')
    technical_Data = get_object_or_404(Technical_Events, name=name) 
    serializer = Technical_Serializer(technical_Data)
    return Response(serializer.data)


@api_view(["POST"])
def cultural_events_post(request):
    name = request.data.get('name')
    date = request.data.get('date')
    venue = request.data.get('venue')
    time = request.data.get('time')
    description = request.data.get('description')
    category = request.data.get('category')
    club = request.data.get('club')
    rules = request.data.get('rules')
    fees_snu = request.data.get('fees_snu')
    fees_amount = request.data.get('fees_amount')
    prize_money = request.data.get('prize_money')
    team_size = request.data.get('team_size')
    time_limit = request.data.get('time_limit')
    registration_link = request.data.get('registration_link')
    person_of_contact = request.data.get('person_of_contact')
    person_of_contactno = request.data.get('person_of_contactno')
    poster = request.data.get('poster')
    cultural = Cultural_Events(name=name, date=date, venue=venue, time=time,
                               description=description, category=category, club=club, rules=rules,
                               fees_snu=fees_snu, fees_amount=fees_amount, prize_money=prize_money,
                               team_size=team_size, time_limit=time_limit, registration_link=registration_link,
                               person_of_contact=person_of_contact, person_of_contactno=person_of_contactno,
                               poster=poster
                               )
    cultural.save()
    return HttpResponse('New Cultural Event Added!')

def indAdder(fieldDict, ind):
    dicter = {}
    for key in fieldDict:
        dicter[key] = fieldDict[key]
    dicter["label"] = dicter["label"] + ind.__str__()
    return dicter

def validateform(form_array, form_data, request):
    errors = []
    for field in form_array:

        field["label"] = field["label"].replace(" ", "_")

        if field["type"] == "fileupload":
            if field['label'] not in request.FILES:
                errors.append(field['label'] + ", a file, is required")
                continue

            f = request.FILES[field['label']]
            ext = f.split(".")[1].lower()
            file_name = uuid.uuid4().hex
            new_name = file_name + ext

            with open('static/uploads/' + new_name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

            form_data[field[label]] = new_name
        elif field['type'] == "multiple":
            count = 0
            min_s = field["min"]
            max_s = field["max"]
            subF = field["subfields"]
            for i in range(0, max_s):
                subFL = map(lambda x : indAdder(x, i), subF)
                processSub = validateform(subFL, form_data, request)
                if(len(processSub["errors"]) == 0):
                    count = count + 1
                elif(count < min_s):
                    errors.extend(processSub["errors"])
                    break
                else:
                    break
        elif field["type"] == "text" or field["type"] == "textarea":
            if field['label'] not in request.data:
                errors.append(field['label'] + " is required")
                continue
            if len(request.data.get(field['label'])) <= 0:
                errors.append(field['label'] + " is required")
                continue
        elif field["type"] == "number":
            if(type(form_data[field["label"]]) != "int"):
                errors.append(field['label'] + " needs to be a number field input")

    reter = {"values": form_data, "errors": errors}
    return reter

@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
def registerevent(request):
    x=0
    # user_id = Token.objects.filter(key=request.data.get('auth_token')).values()[0].user_id
    user = User.objects.filter(email=request.user).values()[0]
    user_id = user.get("id")
    print(user_id)
    event_id = request.data.get('event_id')
    event_name = request.data.get('event_name')
    if(len(Event_Registrations.objects.filter(user_id=user_id, event_id=event_id, event_name=event_name)) != 0):
        return Response({'error': 'Already registered', 'status': 'fail'})

    paid = "Unpaid" #Paid Status can only be changed from admin panel
    found = False
    amount = 0
    event = False
    usr = User.objects.filter(id=user_id).values()[0]
    print(usr)

    if len(Sports_Events.objects.filter(name = request.data.get('event_name'), id = request.data.get('event_id'))) > 0:
        found = True
        event = Sports_Events.objects.filter(name = request.data.get('event_name'), id = request.data.get('event_id')).values()[0]
    elif len(Technical_Events.objects.filter(name = request.data.get('event_name'), id = request.data.get('event_id'))) > 0:
        found = True
        event = Technical_Events.objects.filter(name = request.data.get('event_name'), id = request.data.get('event_id')).values()[0]
    elif len(Cultural_Events.objects.filter(name = request.data.get('event_name'), id = request.data.get('event_id'))) > 0:
        found = True
        event = Cultural_Events.objects.filter(name = request.data.get('event_name'), id = request.data.get('event_id')).values()[0]

    if not found:
        return Response({'error': 'Invalid Event Details', 'status': 'fail'})

    values = request.data
        
    #Do Validation Here!!!
    form_array = json.loads(event.get("form_array"))

    validator = validateform(form_array, values, request)
    values = validator.get("values")

    count_i=0

    while (("Name" + str(count_i)) in request.data) and (len(request.data.get("Name" + str(count_i))) > 0):
        count_i += 1

    count_i = 1 if count_i == 0 else count_i
    
    err = validator["errors"]

    if(len(err) >= 1):
        return JsonResponse({
            "status" : "fail",
            "errors" : json.dumps(err)
        })
        

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("sheet.json", scope)

    client = gspread.authorize(creds)

    event1 = client.open(event.get("name")).sheet1
    insertRow = [usr.get('first_name') + " " +  usr.get('last_name'),usr.get('college'),*(request.data.values())]

    event1.append_row(insertRow)

    amount = (event.get("fees_snu") if usr.get("college") == "Shiv Nadar University" else event.get("fees_amount"))

    new_data = Event_Registrations(user_id = user_id, event_id = event_id, numberofpeople=count_i, event_name = event_name, paid = paid, amount=amount, form_array=json.dumps(values), perperson=event.get("perperson"))
    new_data.save()
    return Response({
        "status" : "success"
    })
@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
def makePayment(request):
    x=0
    # user_id = Token.objects.filter(key=request.data.get('auth_token')).values()[0].user_id
    user = User.objects.filter(email=request.user).values()[0]
    user_id = user.get("id")
    events = request.data.get('events').split()
    registrations = []
    amount = 0
    partial = False
    for ev in events :
        tr = Event_Registrations.objects.filter(id=ev, user_id=user_id).values()[0]
        if(len(tr) <= 0):
            return Response({
                "error" : "Invalid Registration ID: " + ev,
                "status":   "fail"
            })
        amount += int(tr.get("amount") * (tr.get("numberofpeople") if tr.get("perperson") else 1))
        registrations.append(tr.get("event_name"))

    accomodations = request.data.get("accomodations")
    accom_data = []

    if accomodations != None:
        for acc in accomodations:
            accom = Accommodation.objects.filter(
                user_id=user_id, 
                start_date=acc["start_date"],
                number_of_people=acc["number_of_people"],
                include_food=acc["include_food"],
                type=acc["type"],
            )
            accom = accom.values()[0]
            accom_string = "From " + str(accom.get("start_date")) + " for " + str(accom.get("type")) + " days. People: " + str(accom.get("number_of_people")) + ". Food: " + accom.get("include_food")
            accom_data.append(accom_string)
            amount += accom["amount"]

    amountPaid = int(request.data.get("amount"))
    if(amountPaid < amount):
        partial = True

    genUUID = uuid.uuid4().hex

    payment = Payment(
        user_id=user_id,
        college=user.get("college"),
        uuid=user.get("uuid"),
        name=user.get("first_name") + user.get("last_name"),
        events=request.data.get("events"),
        payment_string=request.data.get("paystring"),
        partial=partial,
        amount=amountPaid,
        fullAmount=amount
    )
    
    payment.save()

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("sheet.json", scope)

    client = gspread.authorize(creds)

    event1 = client.open("payments").sheet1
    insertRow = [
        user.get('first_name') + " " + user.get('last_name'), 
        user.get('college'),
        user.get("uuid"),
        request.data.get("paystring"),
        "Partial Payment" if partial else "Full Payment",
        amountPaid,
        amount,
        "Events: " + str(registrations) + ", Accomodations: " + str(accom_data),
        "No",
        "Date & Time: " + datetime.now().strftime('%d-%m-%Y, %H:%M:%S')
    ]

    event1.append_row(insertRow)
    
    Event_Registrations.objects.filter(id__in=events, user_id=user_id).update(paid="Look for Payment Status", payment_id=genUUID)

    values = request.data
    mail = Mailer()
    mail.send_messages(subject='Breeze - Payment Received!',
                message_type='Transaction',
                email_data=[request.data.get("paystring"), None, None],
                to_emails=[user.get('email')])
    return Response({
        "status" : "success"
    })

@api_view(["GET"])
@permission_classes((IsAuthenticated, ))
def getPayments(request):

    user = User.objects.filter(email=request.user).values()[0]

    values = []

    for r in Payment.objects.filter(user_id=user.get("id")).values("payment_string", "partial", "fullAmount", "amount", "paid"):
        values.append(r)

    return Response({
        "status" : "success",
        "payments" : values
    })

@api_view(["GET"])
def getregisteredevent(request):
    # user_id = Token.objects.get(key=request.data.get('auth_token')).user_id
    user_id  = get_object_or_404(User,email=request.user)
    events = Event_Registrations.objects.filter(user_id = user_id.id).values()
    technical_events = []
    cultural_events = []
    sports_events = []
    for obj in events:
        if len(Sports_Events.objects.filter(name = obj.get('event_name'), id = obj.get('event_id'))) > 0:
            sports_events.append({'event_name': obj.get('event_name'), 'event_id': obj.get('event_id'), 'paid': obj.get('paid'), 'amount': obj.get('amount')})
        elif len(Technical_Events.objects.filter(name = obj.get('event_name'), id = obj.get('event_id'))) > 0:
            technical_events.append({'event_name': obj.get('event_name'), 'event_id': obj.get('event_id'), 'paid': obj.get('paid'), 'amount': obj.get('amount')})
        elif len(Cultural_Events.objects.filter(name = obj.get('event_name'), id = obj.get('event_id'))) > 0:
            cultural_events.append({'event_name': obj.get('event_name'), 'event_id': obj.get('event_id'), 'paid': obj.get('paid'), 'amount': obj.get('amount')})
    return JsonResponse({'technical_events': technical_events, 'cultural_events': cultural_events, 'sports_events': sports_events})

@api_view(["POST"])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    mobile_num = request.data.get('mobile_num')
    college = request.data.get('college')

    uid = uuid.uuid4().hex[0:5]

    while(len(User.objects.filter(uuid=uid)) > 0):
        uid = uuid.uuid4().hex[0:5]
        
    user = User.objects.create_user(email=email, password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.college = college
    user.uuid = uid
    user.mobile_num = mobile_num
    user.save()

    # Generate Token for user
    token = Token.objects.create(user=user)

    logged_in_user = User.objects.filter(email=user).values()[0]
    mail = Mailer()
    mail.send_messages(subject='Welcome to Breeze!',
                message_type='Registration',
                email_data=[uid, first_name + ' ' + last_name, college],
                to_emails=[email])
    return JsonResponse({'status': 'success', 'token': token.key, 'user_data': {
        'email': logged_in_user.get('email'),
        'first_name': logged_in_user.get('first_name'),
        'last_name': logged_in_user.get('last_name'),
        'mobile_num': logged_in_user.get('mobile_num'),
        'college': logged_in_user.get('college')
    }})


@api_view(["GET"])
def user_get(request):
    cultural_data = []
    for i in User.objects.all().values():
        cultural_data.append(i)
    return JsonResponse({'User': cultural_data})


@api_view(["POST"])
@permission_classes((AllowAny,))
def Login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = authenticate(email=email, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials', 'status': 'fail'})
    token, _ = Token.objects.get_or_create(user=user)

    logged_in_user = User.objects.filter(email=user).values()[0]

    return Response({'token': token.key, 'status': 'success', 'user_data': {
        'email': logged_in_user.get('email'),
        'first_name': logged_in_user.get('first_name'),
        'last_name': logged_in_user.get('last_name'),
        'mobile_num': logged_in_user.get('mobile_num'),
        'college': logged_in_user.get('college')
    }})


@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
def changePassword(request):
    user = get_object_or_404(User, email=request.user)
    password = request.data.get("password")
    user = authenticate(email=user.email, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials', 'status': 'fail'})
    user.set_password(request.data.get('new_password'))
    user.save()
    return JsonResponse({'status': 'success'})

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def cart(request):
    #3\user_id = Token.objects.get(key=request.data.get('auth_token')).user_id
    user_id  = get_object_or_404(User,email=request.user)
    events = Event_Registrations.objects.filter(user_id = user_id.id).values()
    accommodation = Accommodation.objects.filter(user_id = user_id.id).values()

    paid = {}
    paid['technical_events'] = []
    paid['cultural_events'] = []
    paid['sports_events'] = []
    Apaid = {}
    Apaid['Accommodation'] = []

    
    unpaid = {}
    unpaid['technical_events'] = []
    unpaid['cultural_events'] = []
    unpaid['sports_events'] = []
    Aunpaid = {}
    Aunpaid['Accommodation'] = []

    
    pending = {}
    pending['technical_events'] = []
    pending['cultural_events'] = []
    pending['sports_events'] = []
    Apending = {}
    Apending['Accommodation'] = []
    

    for obj in events:
        if(obj.get("paid") == "Paid"):
            if len(Sports_Events.objects.filter(name = obj.get('event_name'), id = obj.get('event_id'))) > 0:
                paid['sports_events'].append({'event_name': obj.get('event_name'), 'event_id': obj.get('event_id'), 'paid': obj.get('paid'), 'amount': obj.get('amount'), 'id' : obj.get("id"), "perperson" : obj.get("perperson"), "numberofpeople" : obj.get("numberofpeople")})
            elif len(Technical_Events.objects.filter(name = obj.get('event_name'), id = obj.get('event_id'))) > 0:
                paid['technical_events'].append({'event_name': obj.get('event_name'), 'event_id': obj.get('event_id'), 'paid': obj.get('paid'), 'amount': obj.get('amount'), 'id' : obj.get("id"), "perperson" : obj.get("perperson"), "numberofpeople" : obj.get("numberofpeople")})
            elif len(Cultural_Events.objects.filter(name = obj.get('event_name'), id = obj.get('event_id'))) > 0:
                paid['cultural_events'].append({'event_name': obj.get('event_name'), 'event_id': obj.get('event_id'), 'paid': obj.get('paid'), 'amount': obj.get('amount'), 'id' : obj.get("id"), "perperson" : obj.get("perperson"), "numberofpeople" : obj.get("numberofpeople")})

        elif(obj.get("paid") == "Pending Verification"):
            if len(Sports_Events.objects.filter(name = obj.get('event_name'), id = obj.get('event_id'))) > 0:
                pending['sports_events'].append({'event_name': obj.get('event_name'), 'event_id': obj.get('event_id'), 'paid': obj.get('paid'), 'amount': obj.get('amount'), 'id' : obj.get("id"), "perperson" : obj.get("perperson"), "numberofpeople" : obj.get("numberofpeople")})
            elif len(Technical_Events.objects.filter(name = obj.get('event_name'), id = obj.get('event_id'))) > 0:
                pending['technical_events'].append({'event_name': obj.get('event_name'), 'event_id': obj.get('event_id'), 'paid': obj.get('paid'), 'amount': obj.get('amount'), 'id' : obj.get("id"), "perperson" : obj.get("perperson"), "numberofpeople" : obj.get("numberofpeople")})
            elif len(Cultural_Events.objects.filter(name = obj.get('event_name'), id = obj.get('event_id'))) > 0:
                pending['cultural_events'].append({'event_name': obj.get('event_name'), 'event_id': obj.get('event_id'), 'paid': obj.get('paid'), 'amount': obj.get('amount'), 'id' : obj.get("id"), "perperson" : obj.get("perperson"), "numberofpeople" : obj.get("numberofpeople")})
        else:
            if len(Sports_Events.objects.filter(name = obj.get('event_name'), id = obj.get('event_id'))) > 0:
                unpaid['sports_events'].append({'event_name': obj.get('event_name'), 'event_id': obj.get('event_id'), 'paid': obj.get('paid'), 'amount': obj.get('amount'), 'id' : obj.get("id"), "perperson" : obj.get("perperson"), "numberofpeople" : obj.get("numberofpeople")})
            elif len(Technical_Events.objects.filter(name = obj.get('event_name'), id = obj.get('event_id'))) > 0:
                unpaid['technical_events'].append({'event_name': obj.get('event_name'), 'event_id': obj.get('event_id'), 'paid': obj.get('paid'), 'amount': obj.get('amount'), 'id' : obj.get("id"), "perperson" : obj.get("perperson"), "numberofpeople" : obj.get("numberofpeople")})
            elif len(Cultural_Events.objects.filter(name = obj.get('event_name'), id = obj.get('event_id'))) > 0:
                unpaid['cultural_events'].append({'event_name': obj.get('event_name'), 'event_id': obj.get('event_id'), 'paid': obj.get('paid'), 'amount': obj.get('amount'), 'id' : obj.get("id"), "perperson" : obj.get("perperson"), "numberofpeople" : obj.get("numberofpeople")})
    for obj in accommodation:
        if(obj.get("paid") == "Pending Verification"):
            Apaid['Accommodation'].append({
                "user_id":obj.get('user_id'),
                "name":obj.get('name'),
                "amount":obj.get('amount'),
                "college":obj.get('college'),
                "start_date":obj.get('start_date'),
                "type":obj.get('type'),
                "include_food":obj.get('include_food'),
                "mobile_no":obj.get('mobile_no'),
                "number_of_people":obj.get('number_of_people'),
                "paid":obj.get('paid'),
            })
        elif(obj.get("paid") == "Paid"):
            Apending['Accommodation'].append({
                "user_id":obj.get('user_id'),
                "name":obj.get('name'),
                "amount":obj.get('amount'),
                "college":obj.get('college'),
                "start_date":obj.get('start_date'),
                "type":obj.get('type'),
                "include_food":obj.get('include_food'),
                "mobile_no":obj.get('mobile_no'),
                "number_of_people":obj.get('number_of_people'),
                "paid":obj.get('paid'),
                })
        else:
            Aunpaid['Accommodation'].append({
                "user_id":obj.get('user_id'),
                "name":obj.get('name'),
                "amount":obj.get('amount'),
                "college":obj.get('college'),
                "start_date":obj.get('start_date'),
                "type":obj.get('type'),
                "include_food":obj.get('include_food'),
                "mobile_no":obj.get('mobile_no'),
                "number_of_people":obj.get('number_of_people'),
                "paid":obj.get('paid'),
                })

    return JsonResponse(
        {
            'events' : {'paid': paid, 'pending_verification': pending, 'unpaid': unpaid}, 
            'accomodation' : {
                'paid':Apaid['Accommodation'],
                'pending_verification': Apending['Accommodation'],
                'unpaid': Aunpaid['Accommodation']}, 
        }
    )
    
@api_view(["GET"])
@permission_classes((IsAuthenticated, ))
def verifyUser(request):
    user = get_object_or_404(User, email=request.user)

    user = User.objects.filter(email=request.user).values()[0]

    return Response({
        'status': 'success', 
        'user_data': {
        'email': user.get('email'),
        "uuid" : user.get("uuid"),
        'first_name': user.get('first_name'),
        'last_name': user.get('last_name'),
        'mobile_num': user.get('mobile_num'),
        'college': user.get('college')
    }})

@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
def accommodation_register(request):
    received_json_data=request.data.get('data')
    # user = get_object_or_404(User, id=request.data.get('user_id'))
    user = get_object_or_404(User, email=request.user)
    # user = User.objects.filter(email=request.user).values()[0]
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("sheet.json", scope)

    client = gspread.authorize(creds)

    acc_sheet = client.open("Accomodations").sheet1
    packages = {
        1: {
            "True" : 500,
            "False": 350
        },
        2: {
            "True" : 950,
            "False": 650
        },
        3: {
            "True" : 1350,
            "False": 900
        },
        4: {
            "True" : 1750,
            "False": 1150
        }
    }
    
    for obj in received_json_data: 
        single_am = packages[int(obj['type'])].get(str(obj['include_meal']))
        p = Accommodation(
            amount=(single_am * int(obj["nop"])),
            number_of_people = obj['nop'],
            type=obj['type'],
            start_date = obj['date'],
            college = user.college,
            user_id = user.id,            
            mobile_no=user.mobile_num,
            include_food = "True" if obj['include_meal'] else "False",
            name = user.first_name +" "+user.last_name,
        )
        p.save()
        insertRow = [
            user.first_name +" "+user.last_name,
            user.college,
            user.email,
            str(obj['nop']) + " person(s)",
            str(obj['type']) + " day(s)",
            "Starting: " + str(obj['date']),
            "Food: " + "True" if obj['include_meal'] else "False",
            "Amount: " + str((single_am * int(obj["nop"]))),
            "Phone Number: " + str(user.mobile_num)]
        acc_sheet.append_row(insertRow)
    return HttpResponse('Accommodation Data Added!')
