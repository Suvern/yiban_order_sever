# Generated by Django 3.0.8 on 2020-07-09 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='账号')),
                ('token', models.CharField(max_length=200, verbose_name='登录令牌')),
            ],
            options={
                'verbose_name': '小程序:登录令牌(请勿修改)',
                'verbose_name_plural': '小程序:登录令牌(请勿修改)',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='账号')),
                ('password', models.CharField(editable=False, max_length=100, verbose_name='密码+盐')),
                ('name', models.CharField(blank=True, default='', max_length=20, verbose_name='姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('gender', models.CharField(blank=True, choices=[('男', '男'), ('女', '女')], default='男', max_length=10, verbose_name='性别')),
                ('unit', models.CharField(blank=True, default='', max_length=30, verbose_name='工作单位')),
                ('position', models.CharField(blank=True, default='', max_length=20, verbose_name='职务')),
                ('admin_type', models.CharField(blank=True, choices=[('普通用户', '普通用户'), ('翔工作室', '翔工作室'), ('易班', '易班'), ('指导老师', '指导老师')], default='普通用户', max_length=10, verbose_name='管理员类别')),
            ],
            options={
                'verbose_name': ('小程序:用户',),
                'verbose_name_plural': '小程序:用户',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unit', models.CharField(blank=True, default='', max_length=100, verbose_name='预约部门')),
                ('content', models.CharField(max_length=100, verbose_name='预约内容')),
                ('date', models.DateField(verbose_name='预约日期')),
                ('start_time', models.TimeField(verbose_name='开始时间')),
                ('end_time', models.TimeField(verbose_name='结束时间')),
                ('extra', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('state', models.CharField(choices=[('审核中', '审核中'), ('审核通过', '审核通过'), ('已拒绝', '已拒绝')], default='审核中', max_length=10, verbose_name='预约状态')),
                ('reason', models.TextField(blank=True, default='', verbose_name='拒绝理由')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.User', verbose_name='预约人')),
            ],
            options={
                'verbose_name': ('小程序:预约',),
                'verbose_name_plural': '小程序:预约',
            },
        ),
    ]
