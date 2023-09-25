from .bkmodels import ApiTestModel
from rest_framework import fields, serializers

class Serializers(serializers.ModelSerializer):
        class Meta:
                model = ApiTestModel
                fields = '__all__'
