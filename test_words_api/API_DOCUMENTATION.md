# 英语单词量测试小程序 API 文档

## 基础信息

- **基础URL**: `http://localhost:8000/api/v1/`
- **认证方式**: JWT Token (Bearer Token)
- **数据格式**: JSON
- **字符编码**: UTF-8

## 认证

### 用户登录
**POST** `/auth/login/`

**请求参数:**
```json
{
    "code": "微信授权码",
    "user_info": {
        "nickName": "用户昵称",
        "avatarUrl": "头像URL"
    }
}
```

**响应示例:**
```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user": {
        "id": 1,
        "username": "openid_123",
        "nickname": "用户昵称",
        "avatar": "头像URL",
        "phone": "",
        "vocabulary_level": "beginner",
        "total_tests": 0,
        "average_score": "0.00",
        "created_at": "2024-01-01T00:00:00Z"
    }
}
```

### 获取用户信息
**GET** `/auth/profile/`

**请求头:**
```
Authorization: Bearer <token>
```

**响应示例:**
```json
{
    "id": 1,
    "username": "openid_123",
    "nickname": "用户昵称",
    "avatar": "头像URL",
    "phone": "",
    "vocabulary_level": "beginner",
    "total_tests": 5,
    "average_score": "75.50",
    "created_at": "2024-01-01T00:00:00Z"
}
```

### 更新用户信息
**PUT** `/auth/profile/`

**请求头:**
```
Authorization: Bearer <token>
```

**请求参数:**
```json
{
    "nickname": "新昵称",
    "phone": "13800138000"
}
```

## 测试功能

### 获取测试题目
**GET** `/tests/questions/`

**请求头:**
```
Authorization: Bearer <token>
```

**查询参数:**
- `test_type`: 测试类型 (vocabulary/speed/accuracy)
- `difficulty`: 难度等级 (beginner/intermediate/advanced/professional)
- `question_count`: 题目数量 (默认20)

**响应示例:**
```json
{
    "questions": [
        {
            "id": 1,
            "question_type": "choice",
            "question_text": "What is the meaning of 'apple'?",
            "options": ["苹果", "香蕉", "橙子", "葡萄"],
            "difficulty": "intermediate"
        }
    ],
    "test_id": "uuid-string",
    "total_count": 20
}
```

### 提交测试答案
**POST** `/tests/submit/`

**请求头:**
```
Authorization: Bearer <token>
```

**请求参数:**
```json
{
    "test_id": "uuid-string",
    "answers": [
        {"question_id": 1, "answer": "A"},
        {"question_id": 2, "answer": "B"}
    ],
    "duration": 900
}
```

**响应示例:**
```json
{
    "test_id": 1,
    "score": 85.0,
    "correct_count": 17,
    "total_questions": 20,
    "vocabulary_level": "intermediate"
}
```

### 获取测试结果
**GET** `/tests/result/{test_id}/`

**请求头:**
```
Authorization: Bearer <token>
```

**响应示例:**
```json
{
    "id": 1,
    "user": 1,
    "user_nickname": "用户昵称",
    "test_type": "vocabulary",
    "difficulty": "intermediate",
    "total_questions": 20,
    "correct_answers": 17,
    "score": "85.00",
    "vocabulary_level": "intermediate",
    "duration": 900,
    "start_time": "2024-01-01T10:00:00Z",
    "end_time": "2024-01-01T10:15:00Z",
    "created_at": "2024-01-01T10:15:00Z"
}
```

### 获取测试历史
**GET** `/tests/history/`

**请求头:**
```
Authorization: Bearer <token>
```

**查询参数:**
- `test_type`: 测试类型
- `date_from`: 开始日期 (YYYY-MM-DD)
- `date_to`: 结束日期 (YYYY-MM-DD)
- `page`: 页码 (默认1)
- `page_size`: 每页数量 (默认20)

**响应示例:**
```json
{
    "results": [
        {
            "id": 1,
            "user": 1,
            "user_nickname": "用户昵称",
            "test_type": "vocabulary",
            "difficulty": "intermediate",
            "total_questions": 20,
            "correct_answers": 17,
            "score": "85.00",
            "vocabulary_level": "intermediate",
            "duration": 900,
            "start_time": "2024-01-01T10:00:00Z",
            "end_time": "2024-01-01T10:15:00Z",
            "created_at": "2024-01-01T10:15:00Z"
        }
    ]
}
```

## 词汇库

### 获取词汇列表
**GET** `/vocabulary/`

**请求头:**
```
Authorization: Bearer <token>
```

**查询参数:**
- `difficulty`: 难度等级
- `search`: 搜索关键词
- `page`: 页码 (默认1)
- `page_size`: 每页数量 (默认20)

**响应示例:**
```json
{
    "results": [
        {
            "id": 1,
            "word": "apple",
            "phonetic": "/ˈæpəl/",
            "translation": "苹果",
            "difficulty": "intermediate",
            "part_of_speech": "noun",
            "example_sentence": "I eat an apple every day.",
            "frequency": 100,
            "created_at": "2024-01-01T00:00:00Z"
        }
    ],
    "total_count": 1000,
    "page": 1,
    "page_size": 20
}
```

### 获取词汇详情
**GET** `/vocabulary/{word}/`

**请求头:**
```
Authorization: Bearer <token>
```

**响应示例:**
```json
{
    "id": 1,
    "word": "apple",
    "phonetic": "/ˈæpəl/",
    "translation": "苹果",
    "difficulty": "intermediate",
    "part_of_speech": "noun",
    "example_sentence": "I eat an apple every day.",
    "frequency": 100,
    "is_active": true,
    "created_at": "2024-01-01T00:00:00Z"
}
```

## 排行榜

### 获取排行榜
**GET** `/ranking/`

**请求头:**
```
Authorization: Bearer <token>
```

**查询参数:**
- `ranking_type`: 排行榜类型 (daily/weekly/monthly/all_time)
- `page`: 页码 (默认1)
- `page_size`: 每页数量 (默认50)

**响应示例:**
```json
{
    "rankings": [
        {
            "id": 1,
            "user": 1,
            "user_nickname": "用户昵称",
            "user_avatar": "头像URL",
            "ranking_type": "weekly",
            "score": "95.50",
            "vocabulary_level": "advanced",
            "rank_position": 1,
            "test_count": 10,
            "period_start": "2024-01-01",
            "period_end": "2024-01-07",
            "created_at": "2024-01-01T00:00:00Z"
        }
    ],
    "total_count": 100,
    "page": 1,
    "page_size": 50,
    "ranking_type": "weekly"
}
```

### 获取用户排名
**GET** `/ranking/user-rank/`

**请求头:**
```
Authorization: Bearer <token>
```

**查询参数:**
- `ranking_type`: 排行榜类型

**响应示例:**
```json
{
    "id": 1,
    "user": 1,
    "user_nickname": "用户昵称",
    "user_avatar": "头像URL",
    "ranking_type": "weekly",
    "score": "85.00",
    "vocabulary_level": "intermediate",
    "rank_position": 5,
    "test_count": 8,
    "period_start": "2024-01-01",
    "period_end": "2024-01-07",
    "created_at": "2024-01-01T00:00:00Z"
}
```

## 统计分析

### 获取学习统计
**GET** `/history/statistics/`

**请求头:**
```
Authorization: Bearer <token>
```

**响应示例:**
```json
{
    "total_tests": 25,
    "average_score": 78.5,
    "vocabulary_level": "intermediate",
    "difficulty_stats": [
        {
            "difficulty": "intermediate",
            "count": 15,
            "avg_score": 80.0,
            "max_score": 95.0,
            "min_score": 65.0
        }
    ],
    "test_type_stats": [
        {
            "test_type": "vocabulary",
            "count": 25,
            "avg_score": 78.5
        }
    ],
    "level_stats": [
        {
            "vocabulary_level": "intermediate",
            "count": 20
        }
    ],
    "recent_tests_count": 8
}
```

### 获取历史记录统计
**GET** `/history/statistics/detail/`

**请求头:**
```
Authorization: Bearer <token>
```

**查询参数:**
- `test_type`: 测试类型
- `date_from`: 开始日期
- `date_to`: 结束日期

**响应示例:**
```json
{
    "total_records": 25,
    "average_score": 78.5,
    "max_score": 95.0,
    "min_score": 60.0,
    "filter_params": {
        "test_type": "vocabulary",
        "date_from": "2024-01-01",
        "date_to": "2024-01-31"
    }
}
```

## 错误码说明

| 状态码 | 说明 |
|--------|------|
| 200 | 请求成功 |
| 201 | 创建成功 |
| 400 | 请求参数错误 |
| 401 | 未认证 |
| 403 | 权限不足 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |

## 数据模型

### 用户模型 (User)
```json
{
    "id": 1,
    "openid": "微信OpenID",
    "nickname": "用户昵称",
    "avatar": "头像URL",
    "phone": "手机号",
    "vocabulary_level": "词汇水平",
    "total_tests": "总测试次数",
    "average_score": "平均分数",
    "created_at": "创建时间",
    "updated_at": "更新时间"
}
```

### 测试记录模型 (TestRecord)
```json
{
    "id": 1,
    "user": "用户ID",
    "test_type": "测试类型",
    "difficulty": "难度等级",
    "total_questions": "总题目数",
    "correct_answers": "正确答案数",
    "score": "得分",
    "vocabulary_level": "词汇水平",
    "duration": "测试时长(秒)",
    "start_time": "开始时间",
    "end_time": "结束时间",
    "created_at": "创建时间"
}
```

### 词汇模型 (Vocabulary)
```json
{
    "id": 1,
    "word": "单词",
    "phonetic": "音标",
    "translation": "中文释义",
    "difficulty": "难度等级",
    "part_of_speech": "词性",
    "example_sentence": "例句",
    "frequency": "使用频率",
    "is_active": "是否启用",
    "created_at": "创建时间"
}
```

## 部署说明

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

5. 访问API文档：
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## 注意事项

1. 所有API请求都需要在请求头中包含JWT Token（除了登录接口）
2. 时间格式统一使用ISO 8601格式
3. 分页参数page从1开始计数
4. 所有响应数据都使用UTF-8编码
5. 错误响应会包含详细的错误信息 