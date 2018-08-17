def a(s):
    if '0' <= s[0] <= '9':
        print('变量名不能以数字开头！')
        return
    for i in s:
        if not('a' <= i <= 'z')and not('A' <= i <= 'Z') and i != '_' and not('0' <= i <= '9'):
            print('变量名包含特殊字符！')   
            return
    print('符合变量名命名规则')
    return

a('g53d_jdsfjkk__544')
