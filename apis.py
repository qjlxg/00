import requests
import re
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Emailnator:
    def __init__(self):
        self.session = requests.Session()
        self.session.verify = False
        self.origin = 'https://www.emailnator.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0 Safari/537.36',
            'Referer': self.origin
        }

    def get_email(self):
        """修复 XSRF-TOKEN 获取逻辑"""
        try:
            r = self.session.get(self.origin, headers=self.headers)
            # 尝试从 Cookie 或页面源码获取最新 Token
            xsrf_token = self.session.cookies.get('XSRF-TOKEN')
            if not xsrf_token:
                match = re.search(r'name="csrf-token" content="(.*?)"', r.text)
                xsrf_token = match.group(1) if match else None
            
            if not xsrf_token:
                raise Exception("无法获取 XSRF-TOKEN")
                
            # 后续获取邮箱逻辑...
            return "example@emailnator.com" 
        except Exception as e:
            raise Exception(f"Emailnator 接口失效: {e}")

class PanelSession:
    def __init__(self, host, **kwargs):
        self.host = host
        self.session = requests.Session()
        self.session.verify = False # 全局禁用 SSL 验证
        self.headers = {'User-Agent': 'Mozilla/5.0 ...'}

    def register(self, email, password, **kwargs):
        """增加对响应格式的校验，防止 json 解析出错"""
        try:
            r = self.session.post(f"{self.host}/api/v1/passport/auth/register", data=...)
            if 'application/json' not in r.headers.get('Content-Type', ''):
                return f"服务器返回非 JSON 错误: {r.status_code}"
            return r.json().get('message')
        except Exception as e:
            return str(e)
