#!/usr/bin/env python
"""
简化的API接口测试脚本
"""

import requests
import json

BASE_URL = "http://localhost:8000/api/v1"

def test_login():
    """测试登录接口"""
    print("测试登录接口...")
    data = {
        "code": "test_code",
        "user_info": {
            "nickName": "测试用户",
            "avatarUrl": "https://example.com/avatar.jpg"
        }
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/login/", json=data)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print("登录成功")
            return result.get('token')
        else:
            print(f"登录失败: {response.text}")
            return None
    except Exception as e:
        print(f"请求失败: {e}")
        return None

def test_profile(token):
    """测试用户信息接口"""
    print("\n测试用户信息接口...")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    
    try:
        response = requests.get(f"{BASE_URL}/auth/profile/", headers=headers)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"用户昵称: {data.get('nickname')}")
        else:
            print(f"获取用户信息失败: {response.text}")
    except Exception as e:
        print(f"请求失败: {e}")

def test_vocabulary(token):
    """测试词汇接口"""
    print("\n测试词汇接口...")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    
    try:
        response = requests.get(f"{BASE_URL}/vocabulary/", headers=headers)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"词汇数量: {len(data.get('results', []))}")
        else:
            print(f"获取词汇失败: {response.text}")
    except Exception as e:
        print(f"请求失败: {e}")

def main():
    print("API接口测试")
    print("=" * 30)
    
    # 测试登录
    token = test_login()
    
    if token:
        # 测试其他接口
        test_profile(token)
        test_vocabulary(token)
        print("\n测试完成")
    else:
        print("\n登录失败，请检查服务器是否运行")

if __name__ == '__main__':
    main() 