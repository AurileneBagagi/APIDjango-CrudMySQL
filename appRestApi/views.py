from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from appRestApi.models import PosterDados
from appRestApi.serializers import PosterDadosSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def appRestApi_list(request):
    # OBTER lista de appRestApi, POSTAR um novo appRestApi, EXCLUIR todos os appRestApi
    if request.method == 'GET': #Recuperar todos os appRestApi/encontrar descricao do banco de dados MySQL:
        appRestApi = PosterDados.objects.all()
        
        descricao = request.GET.get('descricao', None)
        if descricao is not None:
            appRestApi = appRestApi.filter(descricao__icontains=descricao)
        
        appRestApi_serializer = PosterDadosSerializer(appRestApi, many=True)
        return JsonResponse(appRestApi_serializer.data, safe=False)
    
    elif request.method == 'POST': # Crie e salve um novo appRestAPI
        appRestApi_data = JSONParser().parse(request)
        appRestApi_serializer = PosterDadosSerializer(data=appRestApi_data)

        if appRestApi_serializer.is_valid():
            appRestApi_serializer.save()
            return JsonResponse(appRestApi_serializer.data, status=status.HTTP_201_CREATED) 
        
        return JsonResponse(appRestApi_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': #Exclua todos os appRestApi do banco de dados:
        count = PosterDados.objects.all().delete()
        return JsonResponse({'message': '{} AppRestApu were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def appRestApi_detail(request, pk):
    # find appRestApi by pk (id) (encontrar por pk)
    try: 
        appRestApi = PosterDados.objects.get(pk=pk)
        
    except: 
        return JsonResponse({'message': 'The appRestApi {} does not exist'.format(pk)}) 
    
    if request.method == 'GET': # Recupere um appRestApi pelo id na solicitação:
            appRestApi_serializer = PosterDadosSerializer(appRestApi) 
            return JsonResponse(appRestApi_serializer.data)  
        
    elif request.method == 'PUT': # Atualize um appRestApi pelo id na solicitação:
        appRestApi_data = JSONParser().parse(request) 
        appRestApi_serializer = PosterDadosSerializer(appRestApi, data=appRestApi_data)

        if appRestApi_serializer.is_valid(): 
            appRestApi_serializer.save() 
            return JsonResponse(appRestApi_serializer.data) 
            
        return JsonResponse(appRestApi_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE': # Apague um appRestApi pelo id na solicitação:
        appRestApi.delete() 

        return JsonResponse({'message': 'appRestApi was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
 
    # GET / PUT / DELETE appRestApi
    
        
@api_view(['GET'])
def appRestApi_list_published(request):
    # GET all published appRestApis (obtenha todos as appRestApi publicados)
    appRestApi = PosterDados.objects.filter(published=True)
        
    if request.method == 'GET':  #Encontre todos os tutoriais com published = True:
        appRestApi_serializer = PosterDadosSerializer(appRestApi, many=True)
        return JsonResponse(appRestApi_serializer.data, safe=False)
