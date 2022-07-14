from rest_framework import serializers

from VoizApp.models import number,plan,account,dueamt, postpaid, prepaid, dongle, recharge


class numberserial(serializers.ModelSerializer):
    class Meta:
        model = number
        fields = '__all__'


class planserial(serializers.ModelSerializer):
    class Meta:
        model = plan
        fields = '__all__'


class accountserial(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = '__all__'


class dueamtserial(serializers.ModelSerializer):
    class Meta:
        model = dueamt
        fields = '__all__'

class prepaidserial(serializers.ModelSerializer):
    class Meta:
        model = prepaid
        fields = '__all__'

class postpaidserial(serializers.ModelSerializer):
    class Meta:
        model = postpaid
        fields = '__all__'

class dongleserial(serializers.ModelSerializer):
    class Meta:
        model = dongle
        fields = '__all__'

class rechargeserial(serializers.ModelSerializer):
    class Meta:
        model = recharge
        fields = '__all__'