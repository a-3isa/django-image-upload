from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
import os 
from rest_framework import status
from rest_framework.views import APIView

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
    queryset.delete()





