from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse,loader
from rest_framework.response import Response
from django.urls import reverse
# Create your views here.
from rest_framework import generics
from .models import JAN, Manager,Employee,Machine,MaterialFinish,predict_Machine,packing,place_order
from .serializers import JANSerializer, ManagerSerializer,EmployeeSerializer,MachineSerializer,MaterialFinishSerializer,predict_MachineSerializer,packingSerializer,place_orderSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.db.models import  Subquery
from django_pandas.io import read_frame
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.linear_model import LinearRegression



class JANAPIView(generics.ListCreateAPIView):
    queryset = JAN.objects.all()
    df = read_frame(queryset)
    serializer_class = JANSerializer


class EmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class packingAPIView(generics.ListCreateAPIView):
    queryset = packing.objects.all()
    df3 = read_frame(queryset)
    serializer_class = packingSerializer



class predict_MachineAPIView(generics.ListCreateAPIView):
    queryset = predict_Machine.objects.all()
    df2 = read_frame(queryset)
    serializer_class = predict_MachineSerializer


class MachineAPIView(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class place_orderAPIView(generics.ListCreateAPIView):
    queryset = place_order.objects.all()
    serializer_class = place_orderSerializer



class MaterialFinishAPIView(generics.ListCreateAPIView):
    queryset = MaterialFinish.objects.all()
    df1 = read_frame(queryset)
    serializer_class = MaterialFinishSerializer


class ManagerAPIView(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    @csrf_exempt
    def post(self, request):
        try:
            mail=request.data.get("manager_mailid");
            pwd=request.data.get("manager_password");
            print(mail);
            print(pwd);
            queryset = Manager.objects.filter(Manager_mail=mail,
                                                    Manager_pwd=pwd)
            print(queryset.query)
            # print(queryset[0].admin_name)
            resp_list = []
            if queryset.exists():
                print("yes")
                return HttpResponse('success')

            else:
                resp_list.append("error")
                resp_list.append("error")
                return HttpResponse('invalid credentials')

            #return HttpResponseRedirect('adminpage')
            #return redirect('http://localhost:8000/Manager')
            #return HttpResponse('success')






        except Manager.DoesNotExist:

            # return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
            return Response(resp_list)



@csrf_exempt
def index(request):
    return render(request,'index.html')

@csrf_exempt
def adminpage(request):
    return render(request,'adminpage.html')

@csrf_exempt
def dashboard(request):
    return render(request,'dashboard.html')


@csrf_exempt
def order(request):
    return render(request,'order.html')

@csrf_exempt
def Predtime_page(request):
    return render(request, 'form-wizard.html')

@csrf_exempt
def Machine(request):
    return render(request,'Machine.html')



@csrf_exempt
def labour(request):
    return render(request,'jqgrid.html')

@csrf_exempt
def first_machine(request):
    return render(request,'first_machine.html')


@csrf_exempt
def packing(request):
    return render(request,'packing.html')



@csrf_exempt
@api_view(('GET',))
def Get_samp(request):
    p = 0
    q = 0
    w1 = 0
    w0 = 0
    xa = 0
    ya = 0
    print(JANAPIView.df.iloc[1])
    listx = []
    listy = []
    for row in JANAPIView.df.itertuples(index=True, name='Pandas'):
        listx.append(getattr(row, "Total_Order"))
        listy.append(getattr(row, "priority_count"))
    print("l1:", listx)
    print("l2:", listy)
    #listx.pop(0)
    #listy.pop(0)
    #print("l1:", listx)
    #print("l2:", listy)
    for i in listx:
        i = int(i)
        xa = xa + i
    xa = xa / len(listx)
    print("x:", xa)
    for j in listy:
        j = int(j)
        ya = ya + j
    ya = ya / len(listy)
    print("y:", ya)
    for (a, b) in zip(listx, listy):
        m = float(a) - xa;
        n = float(b) - ya;
        p = p + (m * n)
    print(p)
    for i in listx:
        i = int(i)
        q = q + (i - xa) ** 2
    print(q)
    w1 = p / q
    print("w1:", w1)
    w0 = ya - (w1 * xa)
    print("w0:", w0)
    y_pred=w0 + (w1 * 453)
    print("y_pred:", y_pred)
    return Response(y_pred)

@csrf_exempt
@api_view(('GET',))
def Get_Predtime(request):
    #ManagerAPIView.df1 = MaterialFinishAPIView.df1.iloc[0:, ].reindex()
    #df1 = df1[:-1]

    number = LabelEncoder()
    MaterialFinishAPIView.df1['Material'] = MaterialFinishAPIView.df1['Material'].apply(lambda x: x.split('-')[0])
    MaterialFinishAPIView.df1['Material'] = number.fit_transform(MaterialFinishAPIView.df1['Material'].astype('str'))
    reg = linear_model.LinearRegression()

    reg.fit(MaterialFinishAPIView.df1[['Material', 'Target_qty']], MaterialFinishAPIView.df1.wp_h)

    reg.coef_

    c = reg.intercept_
    print("Itercept:", c)
    l = reg.predict([[0, 38.461]])

    print("output:", l)

    return Response(l)




@csrf_exempt
@api_view(('GET',))
def Get_machine(request):
    p = 0
    q = 0
    w1 = 0
    w0 = 0
    xa = 0
    ya = 0
    s = 0
    t = 0
    r = 0
    print("IMPLEMENTATION OF LINEAR REGRESSION")
    data = predict_MachineAPIView.df2[['time']]
    data1 = predict_MachineAPIView.df2[['machine']]

    listx = []
    listy = []
    test = []
    for row in predict_MachineAPIView.df2.itertuples(index=True, name='Pandas'):
        test.append(getattr(row, "machine"))
        listx.append(getattr(row, "totallots"))
        listy.append(getattr(row, "time"))

    print(test)
    print(listx)
    print(listy)
    #listx.pop(0)
    #listy.pop(0)

    for i in data:
        li = data[i]
        l = (list(li))
    test_list = list(map(int, l))

    for i in data1:
        lj = data1[i]
        v = (list(lj))
    test_list1 = list(map(int, v))

    for i in listx:
        i = int(i)
        xa = xa + i
    xa = xa / len(listx)

    for j in listy:
        j = int(j)
        ya = ya + j
    ya = ya / len(listy)

    for (a, b) in zip(listx, listy):
        m = float(a) - xa;
        n = float(b) - ya;
        p = p + (m * n)

    for i in listx:
        i = int(i)
        q = q + (i - xa) ** 2

    w1 = p / q
    w0 = ya - (w1 * xa)
    Op = []
    h = w0 + (w1 * 7)
    d = int(h)
    y = len(data)
    for i in range(y):
        if l[i] <= d:
            k = i
            o = v[k]
            m = str(o)
            Op.append(m)

    return Response(Op)

@api_view(('GET',))
@csrf_exempt
def Get_packing(request):
    reg = linear_model.LinearRegression()
    reg.fit(packingAPIView.df3[['packing_needed','Month']], packingAPIView.df3.packing_consumption)

    reg.coef_

    c = reg.intercept_
    print("Itercept:", c)
    l = reg.predict([[0, 38.461]])

    print("output:", l)


    return  Response(l)


@api_view(('GET',))
@csrf_exempt
def Get_attendance(request):
    emp=[]
    emp_tb=Employee.objects.all()
   # print(id)

    wid=Machine.objects.filter(EmpID__in=Subquery(emp_tb.values('EmpID'))).count()
    print(wid)
    val1=str(wid)
    emp.append(val1)
    val1=str(Employee.objects.count()-wid)
    emp.append(val1)
    return Response(emp)

