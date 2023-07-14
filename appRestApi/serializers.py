from rest_framework import serializers 
from appRestApi.models import PosterDados
 
 
class PosterDadosSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = PosterDados
        fields = ('id',
                  'autor',
                  'titulo',
                  'descricao',
                  'datapublicacao',
                  'published')