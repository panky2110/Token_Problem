from token_app.serilizer import *
from token_app.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
import random
import string
import datetime
import time
import threading
from django.db.models import Q

def get_random_token():
    random_source = string.ascii_letters + string.digits + string.punctuation
    token = random.choice(string.ascii_lowercase)
    token += random.choice(string.ascii_uppercase)
    token += random.choice(string.digits)
    token += random.choice(string.punctuation)
    for i in range(32):
        token += random.choice(random_source)
    token_list = list(token)
    random.SystemRandom().shuffle(token_list)
    token = ''.join(token_list)
    return token

def delete_token_five_min(tid):
    time.sleep(300)
    print(f'Delete {tid} in five minute is running')
    token = Token.objects.get(id=int(tid))
    if token and token.is_alive==False:
        token.delete()

def release_token_in_sixty_sec(tid):
    time.sleep(60)
    print(f'Release token in sixty_sec {tid} is running')
    token=Token.objects.get(id=int(tid))
    if token and token.is_alive ==False:
        token.is_assigned = False
        token.save()

def unblock_token(tid):
    print(f'Ublocked token is running')
    token = Token.objects.get(id=int(tid))
    #time.sleep(120)
    if token and token.is_assigned == True:
        token.is_assigned = False
        token.save()

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_all_token(req,):
    tokens = Token.objects.all()
    if tokens:
        tokens = TokenSer(tokens, many=True)
        return Response(tokens.data)
    return Response("No tokens Availble..! Generate new token")

@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def generate_token(req,):
    if req.method == 'POST':
        jsondata = req.data
        print(jsondata)
        token = get_random_token()
        token_obj = Token(token_name=str(token))
        token_obj.save()
        token_obj.refresh_from_db()
        threading.Thread(target=delete_token_five_min,args=[token_obj.id]).start()
    return Response(f'ststus:     ---tokenid-{token_obj.id}-is generate successfully  ' )

@api_view(['PUT'])
@renderer_classes((JSONRenderer,))
def assign_token(req,):
    if req.method=='PUT':
        if Token.objects.filter(is_assigned = False,is_alive=False):
            token = Token.objects.filter(is_assigned = False).first()
            token.is_assigned = True
            token.assigned_at = datetime.datetime.now()
            token.save()
            tid=token.id
            threading.Thread(target=release_token_in_sixty_sec,args=[tid]).start()
            return Response(f'status :   token {tid} assigned successfully',)

        return Response('bad request!', 404)
    return Response('bad request!', 404)

@api_view(['PUT'])
@renderer_classes((JSONRenderer,))
def unassign_token(req,tid):
    if req.method=='PUT':
        token = Token.objects.filter(id=tid).first()
        if token:
            token.is_assigned=False
            token.save()
            ide=token.id
            #threading.Thread(target=unblock_token, args=[ide]).start()
            return Response(f'status : token {ide} unassigned successfully',)
        return Response('bad request!', 404)
    return Response('bad request!', 404)

@api_view(['DELETE'])
@renderer_classes((JSONRenderer,))
def delete_token(req, tid):
    if req.method == 'DELETE':
        jsondata = req.data
        print(jsondata)
        tokens = Token.objects.filter(id=tid).first()
        if tokens:
            tokens.delete()
            return Response(f'status:  token {tid} deleted sucessfully')
        return Response('bad request!', 404)
    return Response('bad request!', 404)

@api_view(['PUT'])
@renderer_classes((JSONRenderer,))
def keep_alive_token(req,tid):
    if req.method == 'PUT':
        jsondata = req.data
        print(jsondata)
        token = Token.objects.filter(id=tid).first()
        if token:
            token.created_time = datetime.datetime.now()
            token.is_alive = True
            token.save()
            return Response(f'status:   token id {tid} is alive')
        return Response('bad request!', 404)
    return Response('bad request!', 404)

@api_view(['PUT'])
@renderer_classes((JSONRenderer,))
def keep_assign_alive_token(req,tid):
    if req.method == 'PUT':
        jsondata = req.data
        print(jsondata)
        token = Token.objects.filter(id=int(tid)).first()
        if token:
            token.assigned_alive = True
            token.save()
            return Response(f'status:   token  {tid} is assigned alive')
        return Response('bad request!', 404)
    return Response('bad request!', 404)
