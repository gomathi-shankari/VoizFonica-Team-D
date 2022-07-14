from rest_framework import viewsets
from VoizApp import serializers
from VoizApp.models import number, plan, account, dueamt, prepaid, postpaid, dongle, recharge


class numberVS(viewsets.ModelViewSet):
    queryset = number.objects.all()
    serializer_class= serializers.numberserial

class planVS(viewsets.ModelViewSet):
    queryset = plan.objects.all()
    serializer_class= serializers.planserial

class accountVS(viewsets.ModelViewSet):
    queryset = account.objects.all()
    serializer_class= serializers.accountserial

class dueamtVS(viewsets.ModelViewSet):
    queryset = dueamt.objects.all()
    serializer_class= serializers.dueamtserial

class prepaidVS(viewsets.ModelViewSet):
    queryset = prepaid.objects.all()
    serializer_class= serializers.prepaidserial

class postpaidVS(viewsets.ModelViewSet):
    queryset = postpaid.objects.all()
    serializer_class= serializers.postpaidserial

class dongleVS(viewsets.ModelViewSet):
    queryset = dongle.objects.all()
    serializer_class= serializers.dongleserial

class rechargeVS(viewsets.ModelViewSet):
    queryset = recharge.objects.all()
    serializer_class= serializers.rechargeserial


