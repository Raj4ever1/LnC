import json

# from eventManagerServer.api.authentication.models import User as authUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
# from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Role

User = get_user_model()

from .forms import UserForm


def createUserForm(request):
    form = UserForm()
    return render(request, 'name.html', {'form': form})


@csrf_exempt
def createUser(request):
    errorMsg = 'User with this Email already exists.'
    response = HttpResponse()
    response.status_code = status.HTTP_405_METHOD_NOT_ALLOWED
    if request.method == 'POST':
        response.status_code = status.HTTP_400_BAD_REQUEST
        if request.body:
            received_json_data = json.loads(request.body.decode())
            form = UserForm(received_json_data)
            if form.is_valid():
                User.objects.create_user(received_json_data["email"], received_json_data['password'],
                                         received_json_data["first_name"], received_json_data["last_name"])
                response.status_code = status.HTTP_201_CREATED
            else:
                if errorMsg in str(form.errors):
                    response.status_code = status.HTTP_409_CONFLICT
                    response.content = json.dumps({
                        "message": errorMsg
                    })

    # return HttpResponse(content= response, content_type='application/json')
    return response


@csrf_exempt
def loginUser(request):
    response = HttpResponse()
    response.status_code = status.HTTP_405_METHOD_NOT_ALLOWED
    if request.method == 'POST':
        response.status_code = status.HTTP_400_BAD_REQUEST
        received_json_data = json.loads(request.body.decode())
        user = authenticate(email=received_json_data['email'], password=received_json_data['password'])
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            response.status_code = status.HTTP_200_OK
            response.content = json.dumps({
                "token": token.key,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role.pk if user.role else 4,
                "email": user.email
            })
        else:
            response.status_code = status.HTTP_403_FORBIDDEN
    return response

@csrf_exempt
def logoutUser(request):
    response = HttpResponse()
    response.content = json.dumps({'data':'user logout Failed'})
    response.content_type = 'application/json'
    response.status_code = status.HTTP_403_FORBIDDEN
    if request.method == 'POST':
        try:
            token = Token.objects.get(key=request.headers["token"])
        except:
            token = None
        if token is not None:
            logout(request)
            token.delete()
            response.status_code = status.HTTP_200_OK
            response.content = json.dumps({'data': 'user logout success'})
    return response
