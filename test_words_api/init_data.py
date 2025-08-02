#!/usr/bin/env python
"""
初始化数据脚本
用于创建测试数据和示例数据
"""

import os
import sys
import django
from datetime import datetime, timedelta
import random

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'english_vocabulary.settings')
django.setup()

from apps.users.models import User
from apps.vocabulary.models import Vocabulary
from apps.tests.models import Question, TestRecord
from apps.ranking.models import Ranking
from apps.statistics.models import UserStatistics, DailyStatistics


def create_sample_vocabulary():
    """创建示例词汇数据"""
    print("创建示例词汇数据...")
    
    vocabulary_data = [
        # 初级词汇
        {'word': 'apple', 'phonetic': '/ˈæpəl/', 'translation': '苹果', 'difficulty': 'beginner', 'part_of_speech': 'noun', 'example_sentence': 'I eat an apple every day.', 'frequency': 100},
        {'word': 'book', 'phonetic': '/bʊk/', 'translation': '书', 'difficulty': 'beginner', 'part_of_speech': 'noun', 'example_sentence': 'I read a book before bed.', 'frequency': 95},
        {'word': 'cat', 'phonetic': '/kæt/', 'translation': '猫', 'difficulty': 'beginner', 'part_of_speech': 'noun', 'example_sentence': 'The cat is sleeping on the sofa.', 'frequency': 90},
        {'word': 'dog', 'phonetic': '/dɔːɡ/', 'translation': '狗', 'difficulty': 'beginner', 'part_of_speech': 'noun', 'example_sentence': 'The dog is running in the park.', 'frequency': 85},
        {'word': 'house', 'phonetic': '/haʊs/', 'translation': '房子', 'difficulty': 'beginner', 'part_of_speech': 'noun', 'example_sentence': 'I live in a big house.', 'frequency': 80},
        
        # 中级词汇
        {'word': 'beautiful', 'phonetic': '/ˈbjuːtɪfʊl/', 'translation': '美丽的', 'difficulty': 'intermediate', 'part_of_speech': 'adjective', 'example_sentence': 'She is a beautiful girl.', 'frequency': 75},
        {'word': 'important', 'phonetic': '/ɪmˈpɔːtənt/', 'translation': '重要的', 'difficulty': 'intermediate', 'part_of_speech': 'adjective', 'example_sentence': 'This is an important meeting.', 'frequency': 70},
        {'word': 'understand', 'phonetic': '/ˌʌndəˈstænd/', 'translation': '理解', 'difficulty': 'intermediate', 'part_of_speech': 'verb', 'example_sentence': 'I understand what you mean.', 'frequency': 65},
        {'word': 'different', 'phonetic': '/ˈdɪfərənt/', 'translation': '不同的', 'difficulty': 'intermediate', 'part_of_speech': 'adjective', 'example_sentence': 'These are different colors.', 'frequency': 60},
        {'word': 'possible', 'phonetic': '/ˈpɒsɪbəl/', 'translation': '可能的', 'difficulty': 'intermediate', 'part_of_speech': 'adjective', 'example_sentence': 'It is possible to finish on time.', 'frequency': 55},
        
        # 高级词汇
        {'word': 'accomplish', 'phonetic': '/əˈkʌmplɪʃ/', 'translation': '完成，实现', 'difficulty': 'advanced', 'part_of_speech': 'verb', 'example_sentence': 'He accomplished his goal.', 'frequency': 50},
        {'word': 'significant', 'phonetic': '/sɪɡˈnɪfɪkənt/', 'translation': '重要的，显著的', 'difficulty': 'advanced', 'part_of_speech': 'adjective', 'example_sentence': 'This is a significant discovery.', 'frequency': 45},
        {'word': 'experience', 'phonetic': '/ɪkˈspɪəriəns/', 'translation': '经验，经历', 'difficulty': 'advanced', 'part_of_speech': 'noun', 'example_sentence': 'She has rich experience in teaching.', 'frequency': 40},
        {'word': 'opportunity', 'phonetic': '/ˌɒpəˈtjuːnəti/', 'translation': '机会', 'difficulty': 'advanced', 'part_of_speech': 'noun', 'example_sentence': 'This is a great opportunity for you.', 'frequency': 35},
        {'word': 'challenge', 'phonetic': '/ˈtʃælɪndʒ/', 'translation': '挑战', 'difficulty': 'advanced', 'part_of_speech': 'noun', 'example_sentence': 'This is a big challenge for us.', 'frequency': 30},
        
        # 专业级词汇
        {'word': 'sophisticated', 'phonetic': '/səˈfɪstɪkeɪtɪd/', 'translation': '复杂的，精密的', 'difficulty': 'professional', 'part_of_speech': 'adjective', 'example_sentence': 'This is a sophisticated system.', 'frequency': 25},
        {'word': 'comprehensive', 'phonetic': '/ˌkɒmprɪˈhensɪv/', 'translation': '全面的，综合的', 'difficulty': 'professional', 'part_of_speech': 'adjective', 'example_sentence': 'We need a comprehensive plan.', 'frequency': 20},
        {'word': 'implementation', 'phonetic': '/ˌɪmplɪmenˈteɪʃən/', 'translation': '实施，执行', 'difficulty': 'professional', 'part_of_speech': 'noun', 'example_sentence': 'The implementation of this policy is difficult.', 'frequency': 15},
        {'word': 'optimization', 'phonetic': '/ˌɒptɪmaɪˈzeɪʃən/', 'translation': '优化', 'difficulty': 'professional', 'part_of_speech': 'noun', 'example_sentence': 'We need to focus on optimization.', 'frequency': 10},
        {'word': 'sustainability', 'phonetic': '/səˌsteɪnəˈbɪləti/', 'translation': '可持续性', 'difficulty': 'professional', 'part_of_speech': 'noun', 'example_sentence': 'Sustainability is important for our future.', 'frequency': 5},
    ]
    
    for data in vocabulary_data:
        Vocabulary.objects.get_or_create(
            word=data['word'],
            defaults=data
        )
    
    print(f"成功创建 {len(vocabulary_data)} 个词汇")


def create_sample_questions():
    """创建示例题目数据"""
    print("创建示例题目数据...")
    
    # 获取词汇数据
    vocabularies = Vocabulary.objects.all()
    
    question_data = []
    
    for vocab in vocabularies:
        # 选择题
        question_data.append({
            'question_type': 'choice',
            'question_text': f"What is the meaning of '{vocab.word}'?",
            'options': [
                vocab.translation,
                f"错误选项1",
                f"错误选项2", 
                f"错误选项3"
            ],
            'correct_answer': vocab.translation,
            'explanation': f"'{vocab.word}' 的意思是 '{vocab.translation}'",
            'difficulty': vocab.difficulty
        })
        
        # 填空题
        question_data.append({
            'question_type': 'fill_blank',
            'question_text': f"Please fill in the blank: The {vocab.word} is on the table.",
            'options': [vocab.word],
            'correct_answer': vocab.word,
            'explanation': f"这里需要填入单词 '{vocab.word}'",
            'difficulty': vocab.difficulty
        })
    
    for data in question_data:
        Question.objects.get_or_create(
            question_text=data['question_text'],
            defaults=data
        )
    
    print(f"成功创建 {len(question_data)} 个题目")


def create_sample_users():
    """创建示例用户数据"""
    print("创建示例用户数据...")
    
    users_data = [
        {'openid': 'openid_001', 'nickname': '张三', 'vocabulary_level': 'beginner'},
        {'openid': 'openid_002', 'nickname': '李四', 'vocabulary_level': 'intermediate'},
        {'openid': 'openid_003', 'nickname': '王五', 'vocabulary_level': 'advanced'},
        {'openid': 'openid_004', 'nickname': '赵六', 'vocabulary_level': 'professional'},
        {'openid': 'openid_005', 'nickname': '钱七', 'vocabulary_level': 'intermediate'},
    ]
    
    for data in users_data:
        user, created = User.objects.get_or_create(
            openid=data['openid'],
            defaults={
                'username': data['openid'],
                'nickname': data['nickname'],
                'vocabulary_level': data['vocabulary_level'],
                'total_tests': random.randint(0, 20),
                'average_score': random.uniform(60, 95)
            }
        )
        
        # 创建用户统计
        UserStatistics.objects.get_or_create(
            user=user,
            defaults={
                'total_study_time': random.randint(100, 1000),
                'total_words_learned': random.randint(50, 500),
                'total_tests_taken': user.total_tests,
                'average_score': user.average_score,
                'highest_score': random.uniform(80, 100),
                'consecutive_days': random.randint(1, 30),
                'last_study_date': datetime.now().date() - timedelta(days=random.randint(0, 7))
            }
        )
    
    print(f"成功创建 {len(users_data)} 个用户")


def create_sample_test_records():
    """创建示例测试记录"""
    print("创建示例测试记录...")
    
    users = User.objects.all()
    questions = Question.objects.all()
    
    for user in users:
        # 为每个用户创建一些测试记录
        for i in range(random.randint(3, 8)):
            # 随机选择题目
            selected_questions = random.sample(list(questions), min(20, questions.count()))
            
            # 计算得分
            correct_count = random.randint(10, len(selected_questions))
            score = (correct_count / len(selected_questions)) * 100
            
            # 确定词汇水平
            if score >= 90:
                vocabulary_level = 'advanced'
            elif score >= 70:
                vocabulary_level = 'intermediate'
            else:
                vocabulary_level = 'beginner'
            
            # 创建测试记录
            test_record = TestRecord.objects.create(
                user=user,
                test_type='vocabulary',
                difficulty=random.choice(['beginner', 'intermediate', 'advanced']),
                total_questions=len(selected_questions),
                correct_answers=correct_count,
                score=score,
                vocabulary_level=vocabulary_level,
                duration=random.randint(300, 1800),  # 5-30分钟
                start_time=datetime.now() - timedelta(days=random.randint(0, 30)),
                end_time=datetime.now() - timedelta(days=random.randint(0, 30))
            )
    
    print("成功创建测试记录")


def create_sample_rankings():
    """创建示例排行榜数据"""
    print("创建示例排行榜数据...")
    
    users = User.objects.all()
    today = datetime.now().date()
    
    # 创建周榜数据
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    
    for i, user in enumerate(users):
        Ranking.objects.get_or_create(
            user=user,
            ranking_type='weekly',
            period_start=week_start,
            period_end=week_end,
            defaults={
                'score': random.uniform(70, 100),
                'vocabulary_level': user.vocabulary_level,
                'rank_position': i + 1,
                'test_count': random.randint(1, 10)
            }
        )
    
    print("成功创建排行榜数据")


def main():
    """主函数"""
    print("开始初始化数据...")
    
    try:
        create_sample_vocabulary()
        create_sample_questions()
        create_sample_users()
        create_sample_test_records()
        create_sample_rankings()
        
        print("数据初始化完成！")
        print("可以访问以下地址：")
        print("- 后台管理: http://localhost:8000/admin/")
        print("- API文档: http://localhost:8000/swagger/")
        
    except Exception as e:
        print(f"初始化数据时出错: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main() 