def change(str):
    result = {}  # 初始化返回结果
    str_new = str.replace(': ', ':').replace('    ', '')  # 第一步，将里面的冒号空格转换为冒号,然后消掉tab
    str_list = str_new.split('\n')  # 第二部，将字符串按行分割，可能会出现列表的第一个元素和最后一个元素为空字符串的情况
    for i in str_list:
        if i:  # 做个筛选，过滤掉空字符串
            # 此时的i是字符串，现在要将它转为键值对
            temp = i.split(':')
            key = temp[0]
            value =':'.join(temp[1:])
            result[key] = value  # 将键值对赋值给字典
    # for i,j in result.items():
    #     print(i + ':' + j)
    return result


if __name__ == '__main__':

    str_header = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate
    Accept-Language: zh,zh-CN;q=0.9
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: traceId=3715; traceId=6604; uuid=6355634fc033e3f2d97c37ff6eb16890; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216503435c1463e-05e7570e350e28-68151275-100200-16503435c154f6%22%7D; analytics=GA1.2.1251620559.1533358075; did=web_jkR3UZgPQW~BIHRRQZcRZxfx0tXr; ac_username=%E7%A2%87%E6%BA%90%E6%B8%A1%E8%BE%B9%E8%8F%8C; auth_key=168108; auth_key_ac_sha1=-741510933; auth_key_ac_sha1_=kONnPqU+K5tet4IzCs1g0BIq5rM=; checkReal=1; isOneVisit=false; ac_userimg=http%3A%2F%2Fcdn.aixifan.com%2Fdotnet%2Fartemis%2Fu%2Fcms%2Fwww%2F201210%2F201759065np9.jpg; did=web_jkR3UZgPQW~BIHRRQZcRZxfx0tXr; _did=web_961520416E243CC0; session_id=5703083957C85252; cur_req_id=4365793447609F3_self_74b76dad2e3d41dd05bc5c996f67fdcf; cur_group_id=4365793447609F3_self_74b76dad2e3d41dd05bc5c996f67fdcf_0; clientlanguage=zh_CN; Hm_lvt_2af69bc2b378fb58ae04ed2a04257ed1=1536630381,1536750284,1536848893,1537065522; stochastic=cmlidXBjN3lzcmM%3D; ac__avi=1010398331472596902fd07758a2463b2996652c5b15rpcx7e49962a7378ecb840f20aacca2384bb; online_status=1200; userLevel=25; userGroupLevel=1; checkMobile=1; checkEmail=1; Hm_lpvt_2af69bc2b378fb58ae04ed2a04257ed1=1537066970
    Host: www.acfun.cn
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36
    '''
    for i, j in change(str_header).items():
        print(i + ':' + j)
