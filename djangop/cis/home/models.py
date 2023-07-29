from django.db import models

class Department(models.Model):
    # dptId = models.IntegerField
    name = models.CharField(max_length=100)
    headOfDepartment = models.CharField(max_length=50)

    def _str_(self):
        return self.name


class Student(models.Model):
    stdId = models.IntegerField
    name = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=12)
    displayPhNo = models.BooleanField()
    emailId = models.CharField(max_length=50)
    yearOfAddmission = models.IntegerField()
    yearOfPassOut = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    remarks = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class Faculty(models.Model):
    facultyId = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=12)
    emailId = models.CharField(max_length=50)
    department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name_plural = "Faculties"

    def _str_(self):
        return self.name

# class Teaches(models.Model):
#     faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)