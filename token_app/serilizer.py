from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from token_app.models import Token



class TokenSer(ModelSerializer):

    class Meta:
        model=Token
        fields = '__all__'




