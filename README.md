# 英语单词量测试API

## 项目简介

英语单词量测试API是为微信小程序提供后端服务的Django项目，实现了用户管理、测试功能、数据统计等核心功能。

## 技术栈

- **Python**: 3.9+
- **Django**: 4.2.7
- **Django REST Framework**: 3.14.0
- **MySQL**: 8.0
- **Redis**: 6.0
- **SimpleUI**: 后台管理美化

## 项目结构

```
test_words_api/
├── english_vocabulary/          # Django项目配置
│   ├── settings.py             # 项目设置
│   ├── urls.py                 # 主URL配置
│   ├── wsgi.py                 # WSGI配置
│   └── asgi.py                 # ASGI配置
├── apps/                       # 应用目录
│   ├── users/                  # 用户管理
│   ├── tests/                  # 测试管理
│   ├── vocabulary/             # 词汇管理
│   ├── ranking/                # 排行榜
│   └── statistics/             # 统计分析
├── manage.py                   # Django管理脚本
├── requirements.txt            # 项目依赖
├── init_data.py               # 初始化数据脚本
└── README.md                  # 项目说明
```

## 快速开始

### 1. 环境准备

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 数据库配置

确保MySQL服务已启动，并创建数据库：

```sql
CREATE DATABASE fast_words CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. 数据库迁移

```bash
# 创建数据库表
python manage.py makemigrations
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser

# 初始化示例数据
python init_data.py
```

### 4. 启动服务

```bash
# 启动开发服务器
python manage.py runserver
```

## API接口文档

启动服务后，访问以下地址查看API文档：

- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/

## 主要功能

### 1. 用户管理
- 微信授权登录
- 用户信息管理
- JWT认证

### 2. 测试功能
- 获取测试题目
- 提交测试答案
- 获取测试结果
- 测试历史记录

### 3. 词汇管理
- 词汇列表查询
- 词汇详情查看
- 按难度分类

### 4. 排行榜
- 好友排行榜
- 全球排行榜
- 用户排名查询

### 5. 数据统计
- 学习统计
- 历史记录统计
- 进度分析

## API接口列表

### 认证相关
- `POST /api/v1/auth/login/` - 用户登录
- `GET /api/v1/auth/profile/` - 获取用户信息
- `PUT /api/v1/auth/profile/` - 更新用户信息

### 测试相关
- `GET /api/v1/tests/questions/` - 获取测试题目
- `POST /api/v1/tests/submit/` - 提交测试答案
- `GET /api/v1/tests/result/{test_id}/` - 获取测试结果
- `GET /api/v1/tests/history/` - 获取测试历史

### 词汇相关
- `GET /api/v1/vocabulary/` - 获取词汇列表
- `GET /api/v1/vocabulary/{word}/` - 获取词汇详情

### 排行榜相关
- `GET /api/v1/ranking/` - 获取排行榜
- `GET /api/v1/ranking/user-rank/` - 获取用户排名

### 统计相关
- `GET /api/v1/history/statistics/` - 获取学习统计
- `GET /api/v1/history/statistics/detail/` - 获取历史统计详情

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
    }
}
```

## 后台管理

访问 http://localhost:8000/admin/ 进入后台管理界面，使用创建的超级用户账号登录。

## 开发说明

### 添加新的API接口

1. 在对应的app中创建视图函数
2. 在urls.py中添加URL配置
3. 在serializers.py中定义序列化器
4. 在models.py中定义数据模型（如需要）

### 测试

```bash
# 运行测试
python manage.py test

# 运行特定应用的测试
python manage.py test apps.users
```

## 部署

### 生产环境配置

1. 修改 `settings.py` 中的 `DEBUG = False`
2. 配置生产环境的数据库连接
3. 配置静态文件收集
4. 使用 Gunicorn 或 uWSGI 部署

### Docker部署

```bash
# 构建镜像
docker build -t english-vocabulary-api .

# 运行容器
docker run -p 8000:8000 english-vocabulary-api
```

## 贡献

1. Fork 本仓库
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证。 