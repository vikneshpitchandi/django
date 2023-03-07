from rest_framework import serializers

from .models import JAN, Manager, Employee, Machine,MaterialFinish,predict_Machine,packing,place_order


class JANSerializer(serializers.ModelSerializer):
    class Meta:
        model = JAN
        fields = "__all__"


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = "__all__"



class MaterialFinishSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialFinish
        fields = "__all__"

class predict_MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = predict_Machine
        fields = "__all__"


class packingSerializer(serializers.ModelSerializer):
    class Meta:
        model = packing
        fields = "__all__"

class place_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = place_order
        fields = "__all__"