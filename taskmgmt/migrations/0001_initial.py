# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flowmgmt', '0001_initial'),
        ('usermgmt', '0001_initial'),
        ('projectmgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=512)),
                ('sort_no', models.IntegerField()),
                ('product_type', models.CharField(choices=[(b'GEN', b'\xe9\x80\x9a\xe7\x94\xa8Web\xe5\xba\x94\xe7\x94\xa8\xe6\x88\x96C/S\xe6\x9e\xb6\xe6\x9e\x84\xe4\xba\xa7\xe5\x93\x81\xef\xbc\x8c\xe5\xbc\xba\xe5\x8c\x96\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe4\xbe\xa7\xe5\xae\x89\xe5\x85\xa8'), (b'CLIENT', b'PC\xe6\x88\x96\xe7\xa7\xbb\xe5\x8a\xa8\xe5\xae\xa2\xe6\x88\xb7\xe7\xab\xaf\xe5\xba\x94\xe7\x94\xa8\xef\xbc\x8c\xe5\xbc\xba\xe5\x8c\x96\xe7\xbb\x88\xe7\xab\xaf\xe5\xae\x89\xe5\x85\xa8'), (b'OTHER', b'\xe5\x85\xb6\xe5\xae\x83')], max_length=32)),
                ('flow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flow_check_items', to='flowmgmt.TaskFlow')),
            ],
        ),
        migrations.CreateModel(
            name='CheckResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(blank=True, choices=[(b'NONE', b'\xe6\x9c\xaa\xe6\xa3\x80\xe6\x9f\xa5'), (b'YES', b'\xe7\xac\xa6\xe5\x90\x88'), (b'NO', b'\xe4\xb8\x8d\xe7\xac\xa6\xe5\x90\x88'), (b'NA', b'\xe4\xb8\x8d\xe6\xb6\x89\xe5\x8f\x8a')], default=b'NONE', max_length=16, null=True)),
                ('check_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmgmt.CheckItem')),
            ],
        ),
        migrations.CreateModel(
            name='CustomCheckResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_item', models.CharField(max_length=256)),
                ('result', models.CharField(choices=[(b'NONE', b'\xe6\x9c\xaa\xe5\xae\x8c\xe6\x88\x90'), (b'YES', b'\xe5\xae\x8c\xe6\x88\x90(OK)'), (b'NO', b'\xe6\x97\xa0\xe6\xb3\x95\xe5\xae\x8c\xe6\x88\x90(\xe6\x94\xbe\xe5\xbc\x83)'), (b'NA', b'\xe4\xb8\x8d\xe6\xb6\x89\xe5\x8f\x8a(\xe4\xbd\x9c\xe5\xba\x9f)')], default=b'NONE', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, max_length=2048, null=True)),
                ('deliverable_url', models.CharField(blank=True, default=b'', max_length=1024, null=True)),
                ('plan_mandays', models.FloatField(default=1.0)),
                ('actual_mandays', models.FloatField(blank=True, default=0.0, null=True)),
                ('is_kcp', models.BooleanField(default=False)),
                ('is_subtask', models.BooleanField(default=False)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('done_time', models.DateTimeField(blank=True, null=True)),
                ('assigner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigner_tasks', to='usermgmt.User')),
                ('checklist', models.ManyToManyField(through='taskmgmt.CheckResult', to='taskmgmt.CheckItem')),
                ('current_handler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_handler_tasks', to='usermgmt.User')),
                ('done_in_project_phase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phase_tasks', to='flowmgmt.ProjectPhase')),
                ('flow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flow_tasks', to='flowmgmt.TaskFlow')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader_tasks', to='usermgmt.User')),
                ('members', models.ManyToManyField(blank=True, related_name='member_tasks', to='usermgmt.User')),
                ('parent_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='taskmgmt.Task')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_tasks', to='projectmgmt.Project')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer_tasks', to='usermgmt.User')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_tasks', to='flowmgmt.TaskStatus')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_tasks', to='usermgmt.Team')),
            ],
        ),
        migrations.CreateModel(
            name='TaskApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle_time', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.CharField(blank=True, max_length=128, null=True)),
                ('handler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_handler_approvals', to='usermgmt.User')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flowmgmt.TaskOption')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_approvals', to='taskmgmt.Task')),
                ('trustee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_trustee_approvals', to='usermgmt.User')),
            ],
        ),
        migrations.AddField(
            model_name='customcheckresult',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_checkresults', to='taskmgmt.Task'),
        ),
        migrations.AddField(
            model_name='checkresult',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_checkresults', to='taskmgmt.Task'),
        ),
    ]
