# Generated by Django 3.1.3 on 2022-08-14 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='question',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text_mark',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
        ),
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ForeignKey(default='CSE 101', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'),
        ),
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='mode',
            field=models.CharField(choices=[('AUDIT', 'Audit'), ('HONOR', 'Honor'), ('BETA', 'BETA')], default='AUDIT', max_length=5),
        ),
        migrations.AlterField(
            model_name='learner',
            name='occupation',
            field=models.CharField(choices=[('STUDENT', 'Student'), ('DEVELOPER', 'Developer'), ('DATA_SCIENTIST', 'Data Scientist'), ('DATABASE_ADMIN', 'Database Admin')], default='STUDENT', max_length=20),
        ),
    ]
