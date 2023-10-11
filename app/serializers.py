from rest_framework import serializers

from app.models import Skin

class SkinSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer de skin"""
    class Meta:
        model = Skin
        fields = ('arma',
                  'nome',
                  'preco',
                  'float',
                  'desgaste',
                  'adesivado',
                  'proprietario')