from urllib import request,parse

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Cookie': '_ref=5bbc0b16cc413; _cpmuid=1137286855; SERVERID=_srv80-125_; _vid=C82BF3E416A00001F7F266C417F03920; sessionloginid=0811b73536eae18b13186c708d4a5a60; _laid=0; _sso=logout; _user=f9f2d1b7435f5fe9ae5f457de42c92fc_181794573_1539055835; _preemail=qq2075826678; _kx=MTgxNzk0NTczOmQyMGdzcmEzYXF5bzphNTY0aXhpZXM4dzBiajhmemJrOWg5ZmtzcHF1YmoxcHZ4dHM%3D; wizard_goto=%2Fkxmobile%2Faj_kxmobile_tip.php; leftapplistexpand=true; onlinenum=c%3A0'
}

url='http://www.kaixin001.com/set/wap.php'
res=request.Request(url=url,headers=headers)
content=request.urlopen(res).read().decode('utf-8')
for i in range(99999):
    res = request.Request(url=url, headers=headers)
    content = request.urlopen(res).read().decode('utf-8')
    print(i)

# with open('开心网.html','w',encoding='utf-8') as f:
#     f.write(content)
