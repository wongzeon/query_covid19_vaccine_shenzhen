# -*- coding: utf-8 -*-
import requests,time
from urllib.parse import parse_qs, urlencode, urlparse
#获取effectiveToken
get_effective_headers = {
    "Host" :"imm.szcdc.net",
    "Connection" :"keep-alive",
    "Upgrade-Insecure-Requests" :"1",
    "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)",
    "Accept" :"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer" :"https://imm.szcdc.net/miWeixin/",
    "Accept-Encoding" :"gzip, deflate",
    "Accept-Language" :"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
    "Cookie" :抓包获取
}
get_effective_token = 'https://imm.szcdc.net/api/wx/getEffectiveToken?appId=抓包获取'
effective_data = requests.get(get_effective_token,headers=get_effective_headers).json()['forwardUrl']
effective_token_is = str(parse_qs(urlparse(effective_data).query)['effectiveToken']).replace('[',"").replace(']',"").replace("'","")
#获取签名页
reservation_headers = {
    "Host" :"imm.szcdc.net",
    "Connection" :"keep-alive",
    "Content-Length" :"355",
    "effectiveToken" :effective_token_is,
    "Origin" :"https://imm.szcdc.net",
    "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)",
    "Content-Type" :"application/json;charset=UTF-8",
    "Accept" :"application/json, text/plain, */*",
    "Cache-Control" :"no-store",
    "appId" :"抓包获取",
    "token" :"抓包获取",
    "Referer" :"https://imm.szcdc.net/miWeixin/?appId=抓包获取&effectiveToken={}".format(effective_token_is),
    "Accept-Encoding" :"gzip, deflate",
    "Accept-Language" :"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
    "Cookie" :"抓包获取"
}
reservation_data = {
  "userInfoId": "抓包获取",
  "name": "抓包获取",
  "idType": "抓包获取",
  "registerTime": "抓包获取",
  "registerFlag": "false",
  "inocStatus": 0,
  "approvalStatus": 1,
  "persCountryCode": "抓包获取",
  "openId": "抓包获取",
  "unionId": "抓包获取",
  "persRegion": "抓包获取",
  "personageType": "1",
  "ids": [
    "抓包获取",
    "抓包获取",
    "抓包获取",
    "抓包获取",
    "抓包获取"
  ]
}
reservation_url = 'https://imm.szcdc.net/miWeixin/wx/reservation/getReservationAddr'
fast_access_url_is = requests.post(reservation_url,json=reservation_data,headers=reservation_headers).json()['data']
reservation_token_is = str(parse_qs(urlparse(fast_access_url_is).query)['reservationToken']).replace('[',"").replace(']',"").replace("'","")
#获取社康页
fast_access_url = '"{}"'.format(fast_access_url_is)
print(fast_access_url)
data_headers = {
    "Host" :"imm.szcdc.net",
    "Connection" :"keep-alive",
    "Content-Length" :"108",
    "Origin" :"https://imm.szcdc.net",
    "selfAppId" :"抓包获取",
    "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)",
    "Content-Type" :"application/x-www-form-urlencoded",
    "Accept" :"application/json, text/plain, */*",
    "appId" :"抓包获取",
    "token" :"抓包获取",
    "reservationToken" :reservation_token_is,
    "Referer" :"https://imm.szcdc.net/crmobile/?appId=抓包获取&token=抓包获取&cardNo=抓包获取&reservationToken={}&vaccineCode=5601&selfAppId=抓包获取".format(reservation_token_is),
    "Accept-Encoding" :"gzip, deflate",
    "Accept-Language" :"zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
    "Cookie" :"抓包获取"
}
data_url = 'https://imm.szcdc.net/crmobile/outpatient/nearby'
#查询“罗湖、福田、南山”数据
#440303 罗湖；440304福田；440305南山；440306宝安；440307龙岗；440308盐田；440309龙华；440310坪山；440311光明；440312大鹏。
for areacode in (440303,440304,440305):
    queryStr = urlencode({
        "pageNum":1,
        "numPerPage":"10",
        "areaCode":areacode,
        "bactCode":"5601",
        "outpName":"",
        "outpMapLongitude":"",
        "outpMapLatitude":"",
        "corpCode":""
    })
    shenzhen_data = json.loads(requests.post(data_url,data=queryStr,headers=data_headers).content)
    data_base = shenzhen_data['data']['list']
    total_in_page = len(data_base)
    wx_push_access_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=企业微信企业ID&corpsecret=企业微信应用secret'
    wx_push_token = requests.post(wx_push_access_url,data="").json()['access_token']
#解析页面数据
    for j in range(0,total_in_page+1):
        try:
            if data_base[j]['nums']>0 and data_base[j]['stock']>0 and int(data_base[j]['status']) == 1:
                hospital_name = data_base[j]['outpName']
                try:
                    vcin_name = data_base[j]['corpName']
                except:
                    vcin_name = ""
                try:
                    service_time = data_base[j]['outpServiceTime']
                except:
                    service_time = ""
                try:
                    service_day = data_base[j]['outpDay']
                except:
                    service_day = ""
                try:
                    hospital_addr = data_base[j]['outpAddress']
                except:
                    hospital_addr = ""
                wx_push_access_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=企业微信企业ID&corpsecret=企业微信应用secret'
                wx_push_token = requests.post(wx_push_access_url,data="").json()['access_token']
                time.sleep(1)
                wx_push_data = {
                        "agentid":企业微信应用ID,
                        "msgtype":"text",
                        "touser":"@all",
                        "text":{
                            "content":"*********疫苗可预约提醒*********\n"+
                            "区域：{}\n".format(areacode)+
                            "社康名称：{}\n".format(hospital_name)+
                            "疫苗厂商：{}\n".format(vcin_name)+
                            "可打日期：{}\n".format(service_day)+
                            "可打时间：{}\n".format(service_time)+
                            "社康地址：{}\n".format(hospital_addr)+
                            "立即预约：<a href={}>戳我</a>".format(fast_access_url)
                        },
                        "safe":0
                    }
                wx_push = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(wx_push_token),json=wx_push_data)
                print(time.strftime("%Y-%m-%d %X"),hospital_name,"可预约|","状态：",data_base[j]['status'],"库存：",data_base[j]['stock'],"Nums：",data_base[j]['nums'])
            elif data_base[j]['nums'] < 0 or data_base[j]['stock'] == 0:
                print(time.strftime("%Y-%m-%d %X"),data_base[j]['outpName']+"未放号")
            else:
                print(time.strftime("%Y-%m-%d %X"),data_base[j]['outpName']+"已约满")
        except Exception:
            continue
