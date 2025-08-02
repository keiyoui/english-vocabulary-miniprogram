# 英语单词量测试小程序后端 - 启动指南

## 项目概述

这是一个基于Django 4.2的英语单词量测试小程序后端API服务，为微信小程序提供完整的后端支持。

## 技术栈

- **后端框架**: Django 4.2
- **API框架**: Django REST Framework 3.14
- **数据库**: MySQL 8.0
- **认证**: JWT (Simple JWT)
- **后台管理**: Django Admin + SimpleUI
- **API文档**: drf-yasg (Swagger)

## 快速开始

### 1. 环境准备

确保您的系统已安装：
- Python 3.9+
- MySQL 8.0
- Redis (可选，用于缓存)

### 2. 安装依赖

```bash
# 进入项目目录
cd test_words_api

# 安装依赖
pip install -r requirements.txt
```

如果遇到网络问题，可以使用国内镜像：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

### 3. 数据库配置

确保MySQL服务正在运行，并创建数据库：

```sql
CREATE DATABASE fast_words CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

项目已配置的数据库连接信息：
- 主机: 127.0.0.1
- 端口: 3306
- 数据库: fast_words
- 用户名: root
- 密码: asdasd

### 4. 数据库迁移

```bash
# 创建数据库迁移文件
python manage.py makemigrations

# 执行数据库迁移
python manage.py migrate
```

### 5. 创建超级用户

```bash
python manage.py createsuperuser
```

### 6. 初始化测试数据

```bash
python init_data.py
```

### 7. 启动开发服务器

```bash
python manage.py runserver
```

### 8. 访问地址

- **后台管理**: http://localhost:8000/admin/
- **API文档**: http://localhost:8000/swagger/
- **ReDoc文档**: http://localhost:8000/redoc/

## 项目结构

```
test_words_api/
├── manage.py                          # Django管理脚本
├── requirements.txt                   # 项目依赖
├── README.md                         # 项目说明
├── STARTUP_GUIDE.md                  # 启动指南
├── check_project.py                   # 项目检查脚本
├── api_test.py                       # API测试脚本
├── init_data.py                      # 初始化数据脚本
├── english_vocabulary/               # 项目主目录
│   ├── __init__.py
│   ├── settings.py                   # 配置文件
│   ├── urls.py                      # 主URL配置
│   ├── wsgi.py                      # WSGI配置
│   └── asgi.py                      # ASGI配置
└── apps/                            # 应用目录
    ├── users/                        # 用户管理
    ├── tests/                        # 测试管理
    ├── vocabulary/                   # 词汇管理
    ├── ranking/                      # 排行榜
    └── statistics/                   # 统计分析
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

## 测试和验证

### 1. 项目完整性检查

```bash
python check_project.py
```

### 2. API接口测试

```bash
# 确保服务器正在运行
python manage.py runserver

# 在另一个终端运行测试
python api_test.py
```

### 3. 数据库检查

```bash
python manage.py dbshell
```

## 常见问题

### 1. 依赖安装失败
- 检查网络连接
- 使用国内镜像源
- 升级pip版本

### 2. 数据库连接失败
- 检查MySQL服务是否运行
- 确认数据库连接信息
- 检查防火墙设置

### 3. 迁移失败
- 删除migrations文件夹重新生成
- 检查数据库表结构
- 确认模型定义正确

### 4. 服务器启动失败
- 检查端口是否被占用
- 确认依赖安装完整
- 查看错误日志

## 开发建议

1. **代码规范**: 遵循PEP 8编码规范
2. **API设计**: 保持RESTful风格
3. **错误处理**: 完善异常处理机制
4. **日志记录**: 详细记录操作日志
5. **测试覆盖**: 编写完整的测试用例

## 部署说明

### 开发环境
- 使用Django内置服务器
- 开启DEBUG模式
- 使用SQLite或本地MySQL

### 生产环境
- 使用Gunicorn或uWSGI
- 关闭DEBUG模式
- 配置Nginx反向代理
- 使用Redis缓存
- 配置日志轮转

## 联系方式

如有问题请联系开发团队。

---

**注意**: 首次运行请按照上述步骤逐一执行，确保每个步骤都成功完成。 