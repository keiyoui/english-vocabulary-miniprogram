#!/usr/bin/env python
"""
项目测试脚本
"""
import os
import sys
import django

# 添加项目路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'english_vocabulary.settings')

try:
    django.setup()
    print("✅ Django环境设置成功")
except Exception as e:
    print(f"❌ Django环境设置失败: {e}")
    sys.exit(1)

# 测试导入应用
try:
    from apps.users.models import User
    from apps.tests.models import TestRecord, Question
    from apps.vocabulary.models import Vocabulary
    from apps.ranking.models import Ranking
    print("✅ 所有模型导入成功")
except Exception as e:
    print(f"❌ 模型导入失败: {e}")

# 测试导入视图
try:
    from apps.users.views import login, profile
    from apps.tests.views import get_questions, submit_test
    from apps.vocabulary.views import get_vocabulary_list
    from apps.ranking.views import get_ranking
    from apps.statistics.views import get_statistics
    print("✅ 所有视图导入成功")
except Exception as e:
    print(f"❌ 视图导入失败: {e}")

# 测试导入序列化器
try:
    from apps.users.serializers import UserSerializer, UserProfileSerializer
    from apps.tests.serializers import QuestionSerializer, TestRecordSerializer
    from apps.vocabulary.serializers import VocabularySerializer
    from apps.ranking.serializers import RankingSerializer
    print("✅ 所有序列化器导入成功")
except Exception as e:
    print(f"❌ 序列化器导入失败: {e}")

print("\n🎉 项目结构验证完成！")
print("\n📋 项目包含以下功能模块：")
print("   - 用户管理 (users)")
print("   - 测试管理 (tests)")
print("   - 词汇管理 (vocabulary)")
print("   - 排行榜 (ranking)")
print("   - 统计分析 (statistics)")

print("\n🚀 下一步操作：")
print("   1. 安装依赖: pip install -r requirements.txt")
print("   2. 创建数据库: CREATE DATABASE fast_words;")
print("   3. 运行迁移: python manage.py makemigrations && python manage.py migrate")
print("   4. 创建超级用户: python manage.py createsuperuser")
print("   5. 初始化数据: python init_data.py")
print("   6. 启动服务: python manage.py runserver")
print("   7. 访问API文档: http://localhost:8000/swagger/") 