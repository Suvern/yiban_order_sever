from django.db import models

GENDER_TYPE = (
    ('男', '男'),
    ('女', '女')
)

ADMIN_TYPE = (
    ('普通用户', '普通用户'),
    ('翔工作室', '翔工作室'),
    ('易班', '易班'),
    ('指导老师', '指导老师')
)

ORDER_TIME_TYPE = (
    ('早上', '早上'),
    ('下午', '下午'),
    ('晚上', '晚上'),
)

ORDER_STATE_TYPE = (
    ('审核中', '审核中'),
    ('审核通过', '审核通过'),
    ('已拒绝', '已拒绝'),
)


# 用户模型
class User(models.Model):
    username = models.CharField(max_length=30, verbose_name='账号', primary_key=True)
    password = models.CharField(max_length=100, verbose_name='密码+盐', editable=False)
    name = models.CharField(max_length=20, verbose_name='姓名', blank=True, default='')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    gender = models.CharField(max_length=10, choices=GENDER_TYPE, verbose_name='性别', blank=True, default='男')
    unit = models.CharField(max_length=30, verbose_name='工作单位', blank=True, default='')
    position = models.CharField(max_length=20, verbose_name='职务', blank=True, default='')
    admin_type = models.CharField(max_length=10, choices=ADMIN_TYPE, verbose_name='管理员类别', blank=True, default='普通用户')

    class Meta:
        verbose_name = '小程序:用户',
        verbose_name_plural = '小程序:用户'

    def __str__(self):
        return self.name + '    （' + self.unit + ' - ' + self.position + ')'


# 预约模型
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='预约人')
    unit = models.CharField(max_length=100, verbose_name='预约部门', blank=True, default='')
    content = models.CharField(max_length=100, verbose_name='预约内容')
    date = models.DateField(verbose_name='预约日期')
    start_time = models.TimeField(verbose_name='开始时间')
    end_time = models.TimeField(verbose_name='结束时间')
    people = models.IntegerField(verbose_name='人数', )
    extra = models.TextField(verbose_name='备注', blank=True, null=True)
    state = models.CharField(max_length=10, choices=ORDER_STATE_TYPE, verbose_name='预约状态', default='审核中')
    reason = models.TextField(verbose_name='拒绝理由', blank=True, default='')

    class Meta:
        verbose_name = '小程序:预约',
        verbose_name_plural = '小程序:预约'

    def __str__(self):
        return f'{self.date}   {self.person.name}: {self.content}'


# 令牌模型
class Token(models.Model):
    username = models.CharField(max_length=30, verbose_name='账号', primary_key=True)
    token = models.CharField(max_length=200, verbose_name='登录令牌')

    class Meta:
        verbose_name = '小程序:登录令牌(请勿修改)'
        verbose_name_plural = '小程序:登录令牌(请勿修改)'

    def __str__(self):
        return f'{self.username}  {self.token}'
