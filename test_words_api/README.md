# 英语单词量测试小程序后端API

## 项目简介

这是一个基于Django 4.2 + DRF的英语单词量测试小程序后端API服务，为微信小程序提供完整的后端支持。

## 技术栈

- **后端框架**: Django 4.2
- **API框架**: Django REST Framework 3.14
- **数据库**: MySQL 8.0
- **认证**: JWT (Simple JWT)
- **后台管理**: Django Admin + SimpleUI
- **缓存**: Redis
- **API文档**: drf-yasg (Swagger)

## 项目结构

```
test_words_api/
├── manage.py                          # Django管理脚本
├── requirements.txt                   # 项目依赖
├── english_vocabulary/               # 项目主目录
│   ├── __init__.py
│   ├── settings.py                   # 配置文件
│   ├── urls.py                      # 主URL配置
│   ├── wsgi.py                      # WSGI配置
│   └── asgi.py                      # ASGI配置
├── apps/                            # 应用目录
│   ├── users/                       # 用户管理
│   ├── tests/                       # 测试管理
│   ├── vocabulary/                  # 词汇管理
│   ├── ranking/                     # 排行榜
│   └── statistics/                  # 统计分析
└── README.md                        # 项目说明
```

## 数据库配置

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fast_words',
        'USER': 'root',
        'PASSWORD': 'asdasd',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

## 主要功能模块

### 1. 用户管理 (users)
- 微信授权登录
- 用户信息管理
- JWT认证

### 2. 测试功能 (tests)
- 获取测试题目
- 提交测试答案
- 测试结果分析
- 测试历史记录

### 3. 词汇库 (vocabulary)
- 词汇列表查询
- 词汇详情查看
- 按难度分类
- 搜索功能

### 4. 排行榜 (ranking)
- 日榜/周榜/月榜/总榜
- 用户排名查询
- 实时排名更新

### 5. 统计分析 (statistics)
- 学习数据统计
- 历史记录分析
- 进度跟踪

## API接口列表

### 认证接口
- `POST /api/v1/auth/login/` - 用户登录
- `GET /api/v1/auth/profile/` - 获取用户信息
- `PUT /api/v1/auth/profile/` - 更新用户信息

### 测试接口
- `GET /api/v1/tests/questions/` - 获取测试题目
- `POST /api/v1/tests/submit/` - 提交测试答案
- `GET /api/v1/tests/result/{id}/` - 获取测试结果
- `GET /api/v1/tests/history/` - 获取测试历史

### 词汇接口
- `GET /api/v1/vocabulary/` - 获取词汇列表
- `GET /api/v1/vocabulary/{word}/` - 获取词汇详情

### 排行榜接口
- `GET /api/v1/ranking/` - 获取排行榜
- `GET /api/v1/ranking/user-rank/` - 获取用户排名

### 统计接口
- `GET /api/v1/history/statistics/` - 获取学习统计
- `GET /api/v1/history/statistics/detail/` - 获取详细统计

## 安装和运行

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 数据库迁移：
```bash
python manage.py makemigrations
python manage.py migrate
```

3. 创建超级用户：
```bash
python manage.py createsuperuser
```

4. 运行开发服务器：
```bash
python manage.py runserver
```

5. 访问地址：
- 后台管理: http://localhost:8000/admin/
- API文档: http://localhost:8000/swagger/

## 数据模型

### 用户模型 (User)
- openid: 微信OpenID
- nickname: 用户昵称
- avatar: 头像URL
- vocabulary_level: 词汇水平
- total_tests: 总测试次数
- average_score: 平均分数

### 测试记录模型 (TestRecord)
- user: 用户
- test_type: 测试类型
- difficulty: 难度等级
- score: 得分
- vocabulary_level: 词汇水平
- duration: 测试时长

### 词汇模型 (Vocabulary)
- word: 单词
- translation: 中文释义
- difficulty: 难度等级
- part_of_speech: 词性
- example_sentence: 例句

### 排行榜模型 (Ranking)
- user: 用户
- ranking_type: 排行榜类型
- score: 分数
- rank_position: 排名位置

## 开发规范

1. 代码规范遵循PEP 8
2. API响应格式统一
3. 错误处理完善
4. 日志记录详细
5. 测试覆盖完整

## 部署说明

1. 生产环境配置
2. 数据库优化
3. 缓存策略
4. 监控告警
5. 备份恢复

## 联系方式

如有问题请联系开发团队。 