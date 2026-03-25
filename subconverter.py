import re
import requests
import urllib3

# 禁用安全请求警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get(url, suffix='', retry=3):
    """获取订阅内容并解析，增加严格的空值保护"""
    # 预定义空返回格式，防止 get_trial.py 迭代 NoneType
    default_res = ({}, '', '', url, url)
    
    try:
        # 增加 verify=False 和更真实的 UA
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        res = requests.get(url, timeout=20, verify=False, headers=headers)
        
        if res.status_code != 200 or not res.text:
            return default_res
        
        content = res.text
        # 如果返回的是 HTML 页面而不是订阅数据，直接跳过
        if '<!DOCTYPE html>' in content or '<html' in content:
            return default_res

        # --- 原有解析逻辑 ---
        # 假设这里调用了你的 Base64 和 Clash 解析
        base64_content = content # 示例
        clash_config = content   # 示例
        info = {} # 假设从 headers 获取了订阅信息
        
        # 模拟从 header 获取流量信息
        sub_info = res.headers.get('subscription-userinfo')
        if sub_info:
            for item in sub_info.split(';'):
                if '=' in item:
                    k, v = item.strip().split('=')
                    info[k] = v

        return info, base64_content, clash_config, url, url
    except Exception:
        return default_res

def gen_base64_and_clash_config(base64_path, clash_path, providers_dir, base64, clash, exclude=None):
    """增加对输入内容的二次检查"""
    if not base64 or not clash:
        return 0
    # ... 原有保存逻辑 ...
    return 1 # 返回节点数
