import json
import base64
import hashlib

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import UserModel, ProductModel, TransactionModel

private_key = 'p@kg@)@_aD_klpk_'
def generate_token(user_id):
    try:
        query_user = UserModel.objects.get(pk = user_id)
        username = query_user.getQuery()['user_username']
        base64_username = base64.b64encode(bytes(username, 'utf-8')).decode('utf-8')
        hash_username = hashlib.sha512(bytes(base64_username + private_key, 'utf-8')).hexdigest()

        return base64_username + '.' + hash_username

    except:
        raise Exception()

def verify_token(token):
    splited_token = token.split('.')
    hash_username = hashlib.sha512(bytes(splited_token[0] + private_key, 'utf-8')).hexdigest()

    if hash_username != splited_token[1]:
        raise Exception()

def get_username_from_token(token):
    splited_token = token.split('.')
    return base64.b64decode(bytes(splited_token[0], 'utf-8')).decode('utf-8')

@csrf_exempt
def product(request):
    if len(request.body) == 0:
        return JsonResponse({"data": "400"})

    input = json.loads(request.body)
    try:
        verify_token(input['token'])
    except:
        return JsonResponse({"data": "401"})

    if request.method == 'GET':
        return product_get_method(input)
    
    if request.method == 'POST':
        return product_post_method(input)

    if request.method == 'PUT':
        return product_put_method(input)

    if request.method == 'DELETE':
        return product_delete_method(input)

@csrf_exempt
def user(request):
    if len(request.body) == 0:
        return JsonResponse({"data": "400"})

    input = json.loads(request.body)
    try:
        if request.method != 'POST':
            verify_token(input['token'])
    except:
        return JsonResponse({"data": "401"})

    if request.method == 'GET':
        return user_get_method(input)
    
    if request.method == 'POST':
        return user_post_method(input)

    if request.method == 'PUT':
        return user_put_method(input)

@csrf_exempt
def transaction(request):
    if len(request.body) == 0:
        return JsonResponse({"data": "400"})

    input = json.loads(request.body)
    try:
        verify_token(input['token'])
    except:
        return JsonResponse({"data": "401"})

    if request.method == 'GET':
        return transaction_get_method(input)
    
    if request.method == 'POST':
        return transaction_post_method(input)


def product_get_method(input):
    product_result = []
    try:
        product_query = ProductModel.objects.get(pk = input['product_id'])
        product_result.append(product_query.getQuery())
    except:
        product_query = ProductModel.objects.all()
        for product in product_query:
            product_result.append(product.getQuery())

    return JsonResponse({"data": product_result})

def product_post_method(input):
    try:
        ProductModel.objects.create(
            product_name = input['product_name'],
            product_price = input['product_price'],
            product_img = input['product_img']
        )
    except:
        return JsonResponse({"data": "500"})

    return JsonResponse({"data": "200"})

def product_put_method(input):
    try:
        ProductModel.objects.filter(
            pk = input['product_id']
        ).update(
            product_name = input['product_name'],
            product_price = input['product_price'],
            product_img = input['product_img'] 
        )
    except:
        return JsonResponse({"data": "500"})

    return JsonResponse({"data": "200"})

def product_delete_method(input):
    try:
        product_query = ProductModel.objects.get(pk = input['product_id'])
        product_query.delete()
    except:
        return JsonResponse({"data": "500"})

    return JsonResponse({"data": "200"})

def user_get_method(input):
    try:
        user_query = UserModel.objects.get(pk = input['user_id'])
        return JsonResponse({"data": {
            "user_username": user_query.getQuery()['user_username'],
            "user_password": user_query.getQuery()['user_password']
        }})
    except:
        return JsonResponse({"data": "500"})

def user_post_method(input):
    try:
        user_query = UserModel.objects.get(
            user_username = input['user_username'],
            user_password = input['user_password']
        )
        user_id = user_query.getQuery()['user_id']
    except:
        return JsonResponse({"data": "404"})

    return JsonResponse({"data": generate_token(user_id)})

def user_put_method(input):
    try:
        UserModel.objects.filter(
            user_username = get_username_from_token(input['token']),
        ).update(
            user_username = input['user_username'],
            user_password = input['user_password']
        )
    except:
        return JsonResponse({"data": "500"})

    return JsonResponse({"data": "200"})

def transaction_get_method(input):
    try:
        transaction_query = TransactionModel.objects.all()
        transaction_result = []

        for transaction in transaction_query:
            transaction_result.append(transaction.getQuery())
        
        return JsonResponse({"data": transaction_result})
    except:
        return JsonResponse({"data": "500"})

def transaction_post_method(input):
    try:
        TransactionModel.objects.create(
            product_id = input['product_id'],
            user_id = input['user_id'],
            transaction_amount = input['transaction_amount']
        )
    except:
        return JsonResponse({"data": "500"})

    return JsonResponse({"data": "201"})