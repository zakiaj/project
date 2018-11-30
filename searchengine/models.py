from django.db import models


class Curriculum(models.Model):
    cid = models.TextField(db_column='CID')  # Field name made lowercase.
    mid = models.CharField(db_column='MID', max_length=100)  # Field name made lowercase.
    modulename = models.TextField(db_column='ModuleName')  # Field name made lowercase.
    querystring = models.CharField(db_column='QueryString', primary_key=True, max_length=8)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    goal = models.TextField(db_column='Goal')  # Field name made lowercase.
    subjectl3 = models.TextField(db_column='SUBJECTL3', blank=True, null=True)  # Field name made lowercase.
    subjectl2 = models.TextField(db_column='SUBJECTL2', blank=True, null=True)  # Field name made lowercase.
    subjectl1 = models.TextField(db_column='SUBJECTL1', blank=True, null=True)  # Field name made lowercase.
    graphics = models.TextField(db_column='Graphics', blank=True, null=True)  # Field name made lowercase.
    lessontags = models.TextField(db_column='LessonTags', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'curriculum'
        unique_together = ('querystring', 'mid')


class Parents(models.Model):
    family_ip_address = models.TextField(db_column='FAMILY_ip_address', blank=True, null=True)  # Field name made lowercase.
    parentname = models.TextField(db_column='ParentName')  # Field name made lowercase.
    parentpass = models.TextField(db_column='ParentPass')  # Field name made lowercase.
    parentemail = models.CharField(db_column='ParentEmail', unique=True, max_length=100)  # Field name made lowercase.
    parent_students = models.CharField(db_column='Parent_Students', max_length=50)  # Field name made lowercase.
    parentid = models.CharField(db_column='ParentID', primary_key=True, max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'parents'


class Students(models.Model):
    studentid = models.ForeignKey(Parents, models.CASCADE, db_column='StudentID', primary_key=True)  # Field name made lowercase.
    studentname = models.TextField(db_column='StudentName')  # Field name made lowercase.
    studentpass = models.TextField(db_column='StudentPass')  # Field name made lowercase.
    gradelevel = models.CharField(db_column='GradeLevel', max_length=2, blank=True, null=True)  # Field name made lowercase.
    currentsubjects = models.TextField(db_column='CurrentSubjects')  # Field name made lowercase.
    curriculum = models.TextField(db_column='Curriculum', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'students'

