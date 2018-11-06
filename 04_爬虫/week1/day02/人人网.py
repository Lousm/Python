from urllib import request,parse

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Cookie': 'anonymid=jn11ckax-5saoi4; depovince=BJ; _r01_=1; JSESSIONID=abcr_Z51k23Mk-iAMzwzw; ick_login=17732888-1838-42b0-b3bb-ffee661bf91b; ick=12f8c7d3-79c5-4540-a42b-53b0c5d71fa2; t=3812d1d87b83dee66ca337b301e610e03; societyguester=3812d1d87b83dee66ca337b301e610e03; id=968293383; xnsid=a9983fc4; XNESSESSIONID=bc8ee00fcdbf; WebOnLineNotice_968293383=1; jebe_key=01ca0335-3790-46e0-afe7-0b6a2c931b2c%7C74d982bf46767ed7ea3eaafd5df81a8c%7C1539048097462%7C1%7C1539048101816; wp_fold=0; jebecookies=668e3430-d241-4458-8f32-03bb064a0d5a|||||'
}

url='http://www.renren.com/968293383/profile'
res=request.Request(url=url,headers=headers)
content=request.urlopen(res).read().decode('utf-8')
with open('人人网.html','w',encoding='utf-8') as f:
    f.write(content)
