from django.db import models


# Create your models here.
class JAN(models.Model):
    Total_Order=models.IntegerField(primary_key=True)
    priority_count=models.IntegerField()

    #class Meta:
        #app_label = ''
    def __str__(self):
        return self.Total_Order

    def __str__(self):
        return self.priority_count


class  packing(models.Model):
    packing_consumption = models.IntegerField(primary_key=True)
    packing_needed = models.IntegerField()
    Month = models.IntegerField()

    #class Meta:
        #app_label = ''
    def __str__(self):
        return self.packing_consumption

    def __str__(self):
        return self.packing_needed

    def __str__(self):
        return self.Month


class predict_Machine(models.Model):
    machine = models.IntegerField(primary_key=True)
    totallots = models.IntegerField()
    time = models.IntegerField()

        # class Meta:
        # app_label = ''
    def __str__(self):
        return self.machine

    def __str__(self):
        return self.totallots

    def __str__(self):
        return self.time

class place_order(models.Model):
    ORDER_NUMBER = models.IntegerField(primary_key=True)
    ORDER_STARTED = models.CharField(max_length=50)
    ORDER_COMPLETED = models.CharField(max_length=50)

        # class Meta:
        # app_label = ''
    def __str__(self):
        return self.ORDER_NUMBER

    def __str__(self):
        return self.ORDER_STARTED

        def __str__(self):
            return self.ORDER_COMPLETED

    # Create your models here.

class Employee(models.Model):
    Employee_Name = models.CharField(max_length=50)
    EmpID = models.IntegerField(primary_key=True)
    MarriedID = models.IntegerField()
    MaritalStatusID = models.IntegerField()
    GenderID = models.IntegerField()
    DeptID = models.IntegerField()
    State = models.CharField(max_length=50)
    Zip = models.IntegerField()
    DOB = models.CharField(max_length=50)
    Sex = models.CharField(max_length=50)
    MaritalDesc = models.CharField(max_length=50)
    CitizenDesc = models.CharField(max_length=50)


    def __str__(self):
        return self.Employee_Name

    def __str__(self):
        return self.EmpID

    def __str__(self):
        return self.MarriedID

    def __str__(self):
        return self.MaritalStatusID

    def __str__(self):
        return self.GenderID

    def __str__(self):
        return self.State

    def __str__(self):
        return self.Zip

    def __str__(self):
        return self.DOB

    def __str__(self):
        return self.Sex

    def __str__(self):
        return self.MaritalDesc

    def __str__(self):
        return self.CitizenDesc




class Manager(models.Model):
    Manager_id = models.IntegerField(primary_key=True)
    Manager_Name = models.CharField(max_length=50)
    Manager_mail = models.CharField(max_length=50)
    Manager_pwd = models.CharField(max_length=50)

    # class Meta:
    # app_label = ''
    def __str__(self):
        return self.Manager_id

    def __str__(self):
        return self.Manager_Name

    def __str__(self):
        return self.Manager_mail

    def __str__(self):
        return self.Manager_pwd

class Machine(models.Model):
    Machine = models.CharField(max_length=50,primary_key=True)
    OEF = models.CharField(max_length=50)
    Work_Time = models.CharField(max_length=50)
    Stop_Time = models.CharField(max_length=50)
    Change_batch = models.IntegerField()
    Production_real = models.CharField(max_length=50)
    Production_Real_per_h = models.CharField(max_length=50)
    Doffing_number = models.IntegerField()
    Doffing_avg_time = models.CharField(max_length=50)
    Ongoing_br = models.IntegerField()
    On_going_sph = models.FloatField()
    Low_twist_alarms = models.IntegerField()
    UKG = models.FloatField()
    EmpID = models.IntegerField()

    def __str__(self):
        return self.Machine

    def __str__(self):
        return self.OEF

    def __str__(self):
        return self.Work_Time

    def __str__(self):
        return self.Stop_Time

    def __str__(self):
        return self.Change_batch

    def __str__(self):
        return self.Production_real

    def __str__(self):
        return self.Production_Real_per_h

    def __str__(self):
        return self.Doffing_number

    def __str__(self):
        return self.Doffing_avg_time

    def __str__(self):
        return self.On_going_br

    def __str__(self):
        return self.On_going_br__100sph_

    def __str__(self):
        return self.Low_twist_alarms

    def __str__(self):
        return self.UKG

    def __str__(self):
        return self.EmpID


class MaterialFinish(models.Model):
    Material = models.CharField(max_length=50,primary_key=True)
    Release = models.DateTimeField(auto_now_add=True)
    wpcnfdate = models.DateTimeField(auto_now_add=True)
    wpcnftime = models.DateTimeField(auto_now_add=True)
    Actual_end = models.DateTimeField(auto_now_add=True)
    Act_finish = models.DateTimeField(auto_now_add=True)
    Target_qty = models.FloatField()
    Del_qty = models.IntegerField()
    Rel_to_Fin = models.FloatField()
    QLead = models.FloatField()
    wp_h = models.FloatField()
    Department_fault = models.CharField(max_length=50)

    # class Meta:
    # app_label = ''
    def __str__(self):
        return self.Material

    def __str__(self):
        return self.Release

    def __str__(self):
        return self.wpcnfdate

    def __str__(self):
        return self.wpcnftime

    def __str__(self):
        return self.Actual_end

    def __str__(self):
        return self.Act_finish

    def __str__(self):
        return self.Target_qty


    def __str__(self):
        return self.Del_qty

    def __str__(self):
        return self.Rel_to_Fin

    def __str__(self):
        return self.QLead

    def __str__(self):
        return self.wp_h

    def __str__(self):
        return self.Department_fault








