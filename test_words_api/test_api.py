#!/usr/bin/env python
"""
API接口测试脚本
用于测试各个API接口的功能
"""

import requests
import json
import time

# API基础URL
BASE_URL = "http://localhost:8000/api/v1"

def test_auth_apis():
    """测试认证相关接口"""
    print("=" * 50)
    print("测试认证相关接口")
    print("=" * 50)
    
    # 测试登录接口
    print("\n1. 测试登录接口...")
    login_data = {
        "code": "test_code_123",
        "user_info": {
            "nickName": "测试用户",
            "avatarUrl": "https://example.com/avatar.jpg"
        }
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/login/", json=login_data)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"登录成功，用户ID: {data.get('user', {}).get('id')}")
            return data.get('token')  # 返回token用于后续测试
        else:
            print(f"登录失败: {response.text}")
            return None
    except Exception as e:
        print(f"登录请求失败: {e}")
        return None

def test_user_apis(token):
    """测试用户相关接口"""
    print("\n" + "=" * 50)
    print("测试用户相关接口")
    print("=" * 50)
    
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    
    # 测试获取用户信息
    print("\n1. 测试获取用户信息...")
    try:
        response = requests.get(f"{BASE_URL}/auth/profile/", headers=headers)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"用户信息: {data.get('nickname')}")
        else:
            print(f"获取用户信息失败: {response.text}")
    except Exception as e:
        print(f"获取用户信息请求失败: {e}")
    
    # 测试更新用户信息
    print("\n2. 测试更新用户信息...")
    update_data = {
        "nickname": "更新后的昵称",
        "phone": "13800138000"
    }
    try:
        response = requests.put(f"{BASE_URL}/auth/profile/", json=update_data, headers=headers)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"更新成功: {data.get('nickname')}")
        else:
            print(f"更新用户信息失败: {response.text}")
    except Exception as e:
        print(f"更新用户信息请求失败: {e}")

def test_vocabulary_apis(token):
    """测试词汇相关接口"""
    print("\n" + "=" * 50)
    print("测试词汇相关接口")
    print("=" * 50)
    
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    
    # 测试获取词汇列表
    print("\n1. 测试获取词汇列表...")
    try:
        response = requests.get(f"{BASE_URL}/vocabulary/", headers=headers)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"词汇数量: {len(data.get('results', []))}")
            if data.get('results'):
                print(f"第一个词汇: {data['results'][0].get('word')}")
        else:
            print(f"获取词汇列表失败: {response.text}")
    except Exception as e:
        print(f"获取词汇列表请求失败: {e}")
    
    # 测试获取词汇详情
    print("\n2. 测试获取词汇详情...")
    try:
        response = requests.get(f"{BASE_URL}/vocabulary/apple/", headers=headers)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"词汇详情: {data.get('word')} - {data.get('translation')}")
        else:
            print(f"获取词汇详情失败: {response.text}")
    except Exception as e:
        print(f"获取词汇详情请求失败: {e}")

def test_test_apis(token):
    """测试测试相关接口"""
    print("\n" + "=" * 50)
    print("测试测试相关接口")
    print("=" * 50)
    
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    
    # 测试获取测试题目
    print("\n1. 测试获取测试题目...")
    try:
        response = requests.get(f"{BASE_URL}/tests/questions/?test_type=vocabulary&difficulty=intermediate&question_count=5", headers=headers)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"题目数量: {len(data.get('questions', []))}")
            test_id = data.get('test_id')
            print(f"测试ID: {test_id}")
            
            # 如果有题目，测试提交答案
            if data.get('questions'):
                print("\n2. 测试提交测试答案...")
                answers = []
                for i, question in enumerate(data['questions']):
                    answers.append({
                        "question_id": question['id'],
                        "answer": "A"  # 模拟答案
                    })
                
                submit_data = {
                    "test_id": test_id,
                    "answers": answers,
                    "duration": 300
                }
                
                try:
                    response = requests.post(f"{BASE_URL}/tests/submit/", json=submit_data, headers=headers)
                    print(f"状态码: {response.status_code}")
                    if response.status_code == 201:
                        data = response.json()
                        print(f"提交成功，得分: {data.get('score')}")
                    else:
                        print(f"提交答案失败: {response.text}")
                except Exception as e:
                    print(f"提交答案请求失败: {e}")
        else:
            print(f"获取测试题目失败: {response.text}")
    except Exception as e:
        print(f"获取测试题目请求失败: {e}")

def test_ranking_apis(token):
    """测试排行榜相关接口"""
    print("\n" + "=" * 50)
    print("测试排行榜相关接口")
    print("=" * 50)
    
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    
    # 测试获取排行榜
    print("\n1. 测试获取排行榜...")
    try:
        response = requests.get(f"{BASE_URL}/ranking/?ranking_type=weekly", headers=headers)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"排行榜数量: {len(data.get('rankings', []))}")
        else:
            print(f"获取排行榜失败: {response.text}")
    except Exception as e:
        print(f"获取排行榜请求失败: {e}")
    
    # 测试获取用户排名
    print("\n2. 测试获取用户排名...")
    try:
        response = requests.get(f"{BASE_URL}/ranking/user-rank/?ranking_type=weekly", headers=headers)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"用户排名: {data.get('rank_position')}")
        else:
            print(f"获取用户排名失败: {response.text}")
    except Exception as e:
        print(f"获取用户排名请求失败: {e}")

def test_statistics_apis(token):
    """测试统计相关接口"""
    print("\n" + "=" * 50)
    print("测试统计相关接口")
    print("=" * 50)
    
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    
    # 测试获取学习统计
    print("\n1. 测试获取学习统计...")
    try:
        response = requests.get(f"{BASE_URL}/history/statistics/", headers=headers)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"总测试次数: {data.get('total_tests')}")
            print(f"平均分数: {data.get('average_score')}")
        else:
            print(f"获取学习统计失败: {response.text}")
    except Exception as e:
        print(f"获取学习统计请求失败: {e}")
    
    # 测试获取历史记录统计
    print("\n2. 测试获取历史记录统计...")
    try:
        response = requests.get(f"{BASE_URL}/history/statistics/detail/?test_type=vocabulary", headers=headers)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"总记录数: {data.get('total_records')}")
            print(f"平均分数: {data.get('average_score')}")
        else:
            print(f"获取历史记录统计失败: {response.text}")
    except Exception as e:
        print(f"获取历史记录统计请求失败: {e}")

def main():
    """主测试函数"""
    print("英语单词量测试小程序 API 接口测试")
    print("注意: 请确保Django服务器正在运行 (python manage.py runserver)")
    print("=" * 50)
    
    # 测试认证接口
    token = test_auth_apis()
    
    if token:
        # 测试其他接口
        test_user_apis(token)
        test_vocabulary_apis(token)
        test_test_apis(token)
        test_ranking_apis(token)
        test_statistics_apis(token)
    else:
        print("\n由于登录失败，跳过其他接口测试")
        print("请检查:")
        print("1. Django服务器是否正在运行")
        print("2. 数据库是否已迁移")
        print("3. 是否有测试数据")
    
    print("\n" + "=" * 50)
    print("API测试完成")
    print("=" * 50)

if __name__ == '__main__':
    main() 