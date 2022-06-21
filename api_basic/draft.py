#############views.py#########
# from django.shortcuts import render
# from django.http import HttpResponse , JsonResponse
# from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import viewsets
# from rest_framework.generics import ListAPIView
import os 
# from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# from rest_framework import permissions
# # from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

# Create your views here.
# @api_view(['GET','POST'])
# def View(request):

#     if request.method == 'GET':

#         articles=Article.objects.all()
#         # print(articles[0])
#         serializer =ArticleSerializer(articles,many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         image=request.data['image']
#         style=request.data['style']
#         # print(request.data['title'])
#         os.system(f'style-transfer  {image} {style}')

#         #os.system(f'python t.py {image} {style}')
#         return Response({"Status":True})

    # parser_classes = [MultiPartParser, FormParser]
    # permission_classes = [IsAuthenticated]
    # def get(self,request):
    #     articles=Article.objects.all()
    #     serializer =ArticleSerializer(articles,many=True)
    #     return Response(serializer.data)
    # def post(self, request, format=None):
    #     serializer = ArticleSerializer(data=request.data, instance=request.user)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    # articles=Article.objects.all()
    # serializer =ArticleSerializer(articles,many=True)

    # def get(self,request):
    # # if request.method == 'GET':
    #     return Response(serializer.data)

    # def post (self,request):
    # # if request.method == 'POST':
    #     serializer =ArticleSerializer(data=request.data)
    #     serializer_class = ArticleSerializer

    #     # # message = ArticleSerializer(data=request.data)
    #     image=request.data['image']
    #     style=request.data['image']
    #     # print(request.data['title'])
    #     os.system(f'style-transfer  {image} {style}')

    #     #os.system(f'python t.py {image} {style}')
    #     return Response(
    #         {
    #             "Status":True
    #         }
    #     )
# @api_view(['GET','POST'])
########################################
class Images(APIView):

    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        image = Article.objects.values_list('image', flat = True)[0]
        print(image)
        style = Article.objects.values_list('style', flat = True)[0]
        print(style)

        os.system(f'style-transfer D:/dream/dreamwalker/media/{image} D:/dream/dreamwalker/media/{style}')
        queryset=Article.objects.all()
        queryset.delete()
        return Response({"status": "success", "data": "D:/dream/dreamwalker/artwork.png"}, status=status.HTTP_200_OK)


    queryset=Article.objects.all()
    serializer_class = ArticleSerializer
    # image = Article.objects.values_list('image', flat = True)[1]
    # print(image)
    # style = Article.objects.values_list('style', flat = True)[0]
    # print(style)
    queryset.delete()
#################################
# class Test(APIView):
#     def get(self, request, id=None):

#         items = Article.objects.all()
#         serializer = ArticleSerializer(items, many=True)
#         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

#     def post(self, request, id=None):
#         print('a7a')
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)










########################################
    # queryset=Article.objects.all()
    
    # def post(request):
    #     if request.method=='post':

    #         os.system(f'style-transfer {image} {style}')
    



    




# @api_view(['GET','POST'])
# def article_list(request):
	
# 	if request.method == 'GET':
# 		articles=Article.objects.all()
# 		serializer =ArticleSerializer(articles,many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':
# 		serializer= ArticleSerializer(data=request.data)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data,status=status.HTTP_201_CREATED)

# 		return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def article_detial(request,pk):
# 	try:
# 		article =Article.objects.get(pk=pk)

# 	except Article.DoesNotExist:
# 		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

# 	if request.method=='GET':
# 		serializer =ArticleSerializer(article)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		serializer= ArticleSerializer(article, data=request.data)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)

# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		article.delete()
# 		return HttpResponse(status=status.HTTP_204_NO_CONTENT)
######################################################################




##########serializer.py#################
from rest_framework import serializers
from .models import Article

# class Base64ImageField(serializers.ImageField):
#     """
#     A Django REST framework field for handling image-uploads through raw post data.
#     It uses base64 for encoding and decoding the contents of the file.

#     Heavily based on
#     https://github.com/tomchristie/django-rest-framework/pull/1268

#     Updated for Django REST framework 3.
#     """

#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid

#         # Check if this is a base64 string
#         if isinstance(data, six.string_types):
#             # Check if the base64 string is in the "data:" format
#             if 'data:' in data and ';base64,' in data:
#                 # Break out the header from the base64 content
#                 header, data = data.split(';base64,')

#             # Try to decode the file. Return validation error if it fails.
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')

#             # Generate file name:
#             file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)

#             complete_file_name = "%s.%s" % (file_name, file_extension, )

#             data = ContentFile(decoded_file, name=complete_file_name)

#         return super(Base64ImageField, self).to_internal_value(data)

#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr

#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension

#         return extension

class ArticleSerializer(serializers.ModelSerializer):
    # image=Base64ImageField(max_length=None, use_url=True,)
    # style=Base64ImageField(max_length=None, use_url=True,)
    #artwork=Base64ImageField(max_length=None, use_url=True,)

    class Meta:
        model = Article
        fields = ['image','style']#'image','style'





############################################################

