from django.db import models


class Record(models.Model):
    sId = models.CharField(max_length=3)
    sName = models.CharField(max_length=30)

    class Meta:
        db_table = "student_Record"
