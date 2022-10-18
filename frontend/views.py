from http import client
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import os
import random, string

# Functions
def randStr(digits=8):
    ''' Random string with length 
    Args:
        digits: (int) length of string
    Returns:
        rstr: (str) random string
    '''
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(digits))

# Create your views here.
def test(request):
    return HttpResponse("Hello")


# Line Login
def authorize(request):
    ''' Line Login authorization (code-flow)
    '''
    client_id = os.getenv('LOGIN_CLIENT')
    redirect_uri = "https://azetry-linenotify.herokuapp.com/login/callback"
    state = randStr()
    scope = "profile%20openid_connect%20oc_email"
    nonce = randStr()

    auth_url = "https://access.line.me/oauth2/v2.1/authorize"
    auth_url = auth_url + \
                f"?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&state={state}&scope={scope}&nonce={nonce}"
    return redirect(auth_url)


def callback(request):
    return JsonResponse(request.GET.dict())