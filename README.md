# query_covid19_vaccine_shenzhen
通过“深圳疾控”公众号查询新冠疫苗供应情况，并将可以预约的社康信息推送至微信。

❗ 2021-6-4 各类参数已做加密，项目已失效。

# 一起苗苗苗苗苗！
虽然中国面对新冠疫情已经处理得很好了，现阶段没打疫苗的，想打的应当尽早，这样才安全。

碍于不能总是盯着手机看放号情况，便写了这个简单的程序，让它定时执行并汇报至微信，可预约时就快速进行预约。

![zx2.png](http://ww1.sinaimg.cn/large/001NakGngy1gr0sdqczx3j60gp0c1dg602.jpg)

🔺 Stock 信息不是真实库存，只是状态信息。

获取到可预约的社康depaId（社康ID），可通过社康编号Get网址，获得真实库存信息。

`https://xgsz.szcdc.net/crmobile/reservationStock/timeNumber?depaId=社康编号&date=2021-06-01&vaccCode=5601`

restSum是总库存，restSurplus则是剩余库存，选择后提交即可。

tips：有可预约的时候，在选择时间的时候，也可能被预约完了，所以下手要快一些~

# 使用条件
✅ 关注 `深圳疾控` 微信公众号，并建立个人档案；

✅ 电脑端安装Fiddler或其他的抓包工具，并登录PC微信，打开Fiddler后，打开疫苗预约页面，完成登录抓包。

✅ 抓包后，请将程序内的`抓包获取`替换成对应参数，实测仅需抓如下两个链接：

得到Cookie和Header中的token
`https://imm.szcdc.net//miWeixin/?appId=XXXXX`

获得POST传送的数据
`https://imm.szcdc.net/miWeixin/wx/reservation/getReservationAddr`

✅ Python版本 >= 3.6，需要requests库，没有的请执行 `pip install requests`

✅ 注册企业微信，并新建一个应用，获取其编号和secret。[官方文档](https://work.weixin.qq.com/api/doc/90000/90135/90236#%E6%96%87%E6%9C%AC%E6%B6%88%E6%81%AF)

企业微信注册链接：[注册](https://work.weixin.qq.com/wework_admin/register_wx?from=myhome_openApi)

注册后直接在网页创建应用即可，无需下载APP

# 说明
⚠ 项目仅用于学习交流，不可用于商业用途

💡 项目仅是查询信息，不自动执行预约操作（免得预约的社康位置不合适）

💡 项目只查询每个区域的第一页，有号放出来的都会自动排在第一页，多次测试都没超过两页，并且号很快就被抢完了。

# 实际测试

⏰`最新可用测试时间：2021年5月30日`

![zx3](http://ww1.sinaimg.cn/large/001NakGngy1gr0sw83jjvj60u010xtee02.jpg)

## 接种完成

打完了，科兴的，目前没啥反应，一切正常。

打针一点感觉都没有，还没蚊子叮得有感觉😂，如果担心打针痛的，这点可以不用担心了
