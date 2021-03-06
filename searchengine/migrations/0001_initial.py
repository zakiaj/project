# Generated by Django 2.1.2 on 2018-11-30 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('cid', models.TextField(db_column='CID')),
                ('mid', models.CharField(db_column='MID', max_length=100)),
                ('modulename', models.TextField(db_column='ModuleName')),
                ('querystring', models.CharField(db_column='QueryString', max_length=8, primary_key=True, serialize=False)),
                ('description', models.TextField(db_column='Description')),
                ('goal', models.TextField(db_column='Goal')),
                ('subjectl3', models.TextField(blank=True, db_column='SUBJECTL3', null=True)),
                ('subjectl2', models.TextField(blank=True, db_column='SUBJECTL2', null=True)),
                ('subjectl1', models.TextField(blank=True, db_column='SUBJECTL1', null=True)),
                ('graphics', models.TextField(blank=True, db_column='Graphics', null=True)),
                ('lessontags', models.TextField(blank=True, db_column='LessonTags', null=True)),
            ],
            options={
                'db_table': 'curriculum',
            },
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('family_ip_address', models.TextField(blank=True, db_column='FAMILY_ip_address', null=True)),
                ('parentname', models.TextField(db_column='ParentName')),
                ('parentpass', models.TextField(db_column='ParentPass')),
                ('parentemail', models.CharField(db_column='ParentEmail', max_length=100, unique=True)),
                ('parent_students', models.CharField(db_column='Parent_Students', max_length=50)),
                ('parentid', models.CharField(db_column='ParentID', max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'parents',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('studentid', models.ForeignKey(db_column='StudentID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='searchengine.Parents')),
                ('studentname', models.TextField(db_column='StudentName')),
                ('studentpass', models.TextField(db_column='StudentPass')),
                ('gradelevel', models.CharField(blank=True, db_column='GradeLevel', max_length=2, null=True)),
                ('currentsubjects', models.TextField(db_column='CurrentSubjects')),
                ('curriculum', models.TextField(blank=True, db_column='Curriculum', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.AlterUniqueTogether(
            name='curriculum',
            unique_together={('querystring', 'mid')},
        ),
    ]
