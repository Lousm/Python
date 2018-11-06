import requests

res = requests.get('https://security.kaixin001.com/login/login_post.php', verify=False)
print(res)
