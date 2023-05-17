from rest_framework import serializers
from user.models import *
class Studentserializers (serializers.modelserializer):
  class meta:
    model=students
    fields="__all__"

