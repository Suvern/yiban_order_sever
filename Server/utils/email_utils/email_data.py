adminEmails = [
    '821589498@qq.com',  # 王昭君
    '1337612820@qq.com',  # 管永富
    '1959384595@qq.com',  # 李红蓉
]

newOrderEmailTemplate = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
<div>
    <h1>易班大厅预约 - 新增预约</h1>
    <p><b>预约人</b>：{{ order.person.name }}</p>
    <p><b>预约部门</b>：{{ order.unit }}</p>
    <p><b>预约内容</b>：{{ order.content }}</p>
    <p><b>预约日期</b>：{{ order.date }}</p>
    <p><b>开始时间</b>：{{ order.start_time }}</p>
    <p><b>结束时间</b>：{{ order.end_time }}</p>
    <p><b>人数</b>：{{ order.people }} </p>
    <p><b>备注</b>：{{ order.extra }}</p>
</div>

<a href="http://yibanorder.91cumt.com/admin/Server/order/{{ order.id }}/change/">
    <button>去审核</button>
</a>

<p>中国矿业大学 - 翔工作室</p>
</body>
</html>
'''

orderOrderedTemplate = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
<div style="">
    <h1>易班大厅预约 - 预约成功</h1>
    <p>您已成功预约易班大厅<b>{{ order.person.name }}</b>在<b>{{ order.data }}</b>的<b>{{ order.content }}</b>活动。</p>
    <p>请耐心等待管理员审核，请联系管理员并关注小程序【易班大厅预约】查看审核结果</p>

    <p>
        如有疑问请联系管理员：<br>
        &nbsp;&nbsp;&nbsp;&nbsp;管永富(站长) 13033530023
        <br>
        &nbsp;&nbsp;&nbsp;&nbsp;李红蓉(副站) 17712150137
        <br>
        &nbsp;&nbsp;&nbsp;&nbsp;陈玉国(指导老师) 15162137942
    </p>
</div>

<p>中国矿业大学 - 翔工作室</p>
</body>
</html>
'''

orderAcceptTemplate = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
<div style="">
    <h1>易班大厅预约 - 审核通过</h1>
    <p>您的预约：<b>{{ order.person.name }}</b>在<b>{{ order.data }}</b>的<b>{{ order.content }}</b>活动。已审核通过！</p>
    <p>请负责人提前15分钟到场</p>

    <p>
        如有疑问请联系管理员：<br>
        &nbsp;&nbsp;&nbsp;&nbsp;管永富(站长) 13033530023
        <br>
        &nbsp;&nbsp;&nbsp;&nbsp;李红蓉(副站) 17712150137
        <br>
        &nbsp;&nbsp;&nbsp;&nbsp;陈玉国(指导老师) 15162137942
    </p>
</div>

<p>中国矿业大学 - 翔工作室</p>
</body>
</html>
'''


orderRejectedTemplate = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
<div style="">
    <h1>易班大厅预约 - 审核结果</h1>
    <p>很遗憾，您的预约：<b>{{ order.person.name }}</b>在<b>{{ order.data }}</b>的<b>{{ order.content }}</b>活动，已被拒绝</p>
    <p>拒绝理由：{{ order.reason }}</p>
    <p>
        如有疑问请联系管理员：<br>
        &nbsp;&nbsp;&nbsp;&nbsp;管永富(站长) 13033530023
        <br>
        &nbsp;&nbsp;&nbsp;&nbsp;李红蓉(副站) 17712150137
        <br>
        &nbsp;&nbsp;&nbsp;&nbsp;陈玉国(指导老师) 15162137942
    </p>
</div>

<p>中国矿业大学 - 翔工作室</p>
</body>
</html>
'''