import code
from http import client
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import os, random, string, requests

# Functions
def randStr(digits=8):
    ''' Random string with length 
    Args:
        digits: (int) length of string
    Returns:
        rstr: (str) random string
    '''
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(digits))


def authorizeUrl():
    ''' Return Line Login authorization (code-flow) url
    '''
    client_id = os.getenv('LOGIN_CLIENT')
    redirect_uri = "https://azetry-linenotify.herokuapp.com/login/callback"
    state = randStr()
    scope = "profile%20openid_connect%20oc_email"
    nonce = randStr()

    auth_url = "https://access.line.me/oauth2/v2.1/authorize"
    auth_url = auth_url + \
                f"?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&state={state}&scope={scope}&nonce={nonce}"
    return auth_url


def accessToken(code):
    ''' Access bearer token'''

    token_url = "https://api.line.me/oauth2/v2.1/token"
    params = {
        'code': code,
        'grant_type': "authorization_code",
        'redirect_uri': "https://azetry-linenotify.herokuapp.com/login/callback",
        'client_id': os.getenv("LOGIN_CLIENT"),
        'client_secret': os.getenv("LOGIN_SECRET")
    }
    res = requests.post(token_url, json = params)


    return res

# Create your views here.
def test(request):
    return HttpResponse("Hello")


# Line Login
def login(request):
    auth_url = authorizeUrl()

    return redirect(auth_url)



def callback(request):
    res = request.GET.dict()

    infos = accessToken(res['code'])
    print(res['code'])
    print(infos.text)
    
    return JsonResponse({'infos': "Done"})