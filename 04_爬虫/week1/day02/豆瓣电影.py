from urllib import request,parse
import json

def douban(start,limit):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        }

    url='https://movie.douban.com/j/chart/top_list?'
    da=parse.parse_qs('type=11&interval_id=100%3A90&action=&start=20&limit=20')
    print(da)
    data={
        "type": "11",
        "interval_id": "100:90",
        "start": str(start),
        "limit": str(limit)
    }
    new_url=url+parse.urlencode(data)
    print(new_url)
    res=request.Request(url=new_url,headers=headers,method='GET')
    content=request.urlopen(res).read().decode('utf-8')
    for item in content[0]:
        pass
    return content

def main():
    content=douban(0,20)
    print(type(content))
    print(content)
    # print(json.dumps(content).decode('utf-8'))

if __name__ == '__main__':
    main()
