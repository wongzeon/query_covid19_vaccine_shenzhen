# query_covid19_vaccine_shenzhen
通过“深圳疾控”公众号查询新冠疫苗供应情况，并将可以预约的社康信息推送至微信。

# 一起苗苗苗苗苗！
虽然中国面对新冠疫情已经处理得很好了，现阶段没打疫苗的，想打的应当尽早，这样才安全。

碍于不能总是盯着手机看放号情况，便写了这个简单的程序，让它定时执行并汇报至微信，可预约时就快速进行预约。

![zx2.png](http://ww1.sinaimg.cn/large/001NakGngy1gr0sdqczx3j60gp0c1dg602.jpg)

# 使用条件
✅ 关注 `深圳疾控` 微信公众号，并建立个人档案；

✅ 电脑端安装Fiddler或其他的抓包工具，并登录PC微信，打开Fiddler后，打开疫苗预约页面，完成登录抓包。

✅ 抓包后，请将程序内的`抓包获取`替换成对应参数，实测仅需抓如下两个链接：

得到Cookie和Header中的token
`https://imm.szcdc.net//miWeixin/?appId=XXXXX`

获得POST传送的数据
`https://imm.szcdc.net/miWeixin/wx/reservation/getReservationAddr`

✅ Python版本 >= 3.6，需要requests库，没有的请执行 `pip install requests`

✅ 注册企业微信，并新建一个应用，获取其编号和secret。[官方文档](https://work.weixin.qq.com/api/doc/90000/90135/90248)

企业微信注册链接：[注册](https://work.weixin.qq.com/wework_admin/register_wx?from=myhome_openApi)

注册后直接在网页创建应用即可，无需下载APP

# 说明
⚠ 项目仅用于学习交流，不可用于商业用途

💡 项目仅是查询信息，不自动执行预约操作（免得预约的社康位置不合适）
PS. 提交和padID有关，可以请求对应的可预约的社康。

# 实际测试

⏰`最新可用测试时间：2021年5月30日`

![zx3](http://ww1.sinaimg.cn/large/001NakGngy1gr0sw83jjvj60u010xtee02.jpg)

![zx4](http://ww1.sinaimg.cn/large/001NakGngy1gr0sy89j7ij60tp0y1gpq02.jpg)

打完了，科兴的，目前没啥反应，一切正常。

![result.jpg](http://ww1.sinaimg.cn/large/001NakGngy1gr1s4xwqilj60u0140q6602.jpg)
