# 英语单词量测试小程序

## 项目简介

英语单词量测试小程序是一个基于微信小程序和Django后端的英语词汇量测试应用。该项目旨在为用户提供便捷的英语词汇量评估服务，帮助用户了解自己的词汇水平并提供个性化的学习建议。

## 项目架构

### 前端 (微信小程序)
- **技术栈**: 微信小程序原生框架
- **主要功能**: 用户测试、结果展示、历史记录、排行榜等
- **目录结构**: 位于 `miniprogram/` 目录

### 后端 (Django API)
- **技术栈**: Python + Django 4 + MySQL 8 + Django REST Framework
- **主要功能**: 用户管理、测试逻辑、数据统计、API接口
- **目录结构**: 位于 `backend/` 目录

## 项目结构

```
english-vocabulary-miniprogram/
├── 1-需求分析/                    # 项目需求文档
│   └── 项目需求.md
├── 2-UI设计图/                    # UI设计文件
│   ├── index.html                 # 设计图展示页面
│   ├── home.html                  # 首页设计
│   ├── test.html                  # 测试页面设计
│   ├── result.html                # 结果页面设计
│   ├── history.html               # 历史记录设计
│   ├── profile.html               # 个人中心设计
│   ├── ranking.html               # 排行榜设计
│   ├── vocabulary.html            # 词汇库设计
│   └── settings.html              # 设置页面设计
├── 3-架构设计/                    # 架构设计文档
│   ├── 1-项目后端架构文档.md      # 后端架构设计
│   └── 2-项目小程序架构文档.md    # 小程序架构设计
├── backend/                       # 后端项目 (待开发)
├── miniprogram/                   # 小程序项目 (待开发)
├── docs/                          # 项目文档
└── README.md                      # 项目说明
```

## 核心功能

### 用户功能
- ✅ 微信授权登录
- ✅ 个人信息管理
- ✅ 学习统计展示

### 测试功能
- ✅ 多种难度级别测试
- ✅ 实时答题进度
- ✅ 详细结果分析
- ✅ 学习建议推荐

### 学习功能
- ✅ 测试历史记录
- ✅ 成绩趋势分析
- ✅ 词汇库学习
- ✅ 个性化推荐

### 社交功能
- ✅ 好友排行榜
- ✅ 全球排行榜
- ✅ 成绩分享

## 技术特点

### 前端特点
- 🎨 现代化UI设计，符合微信小程序设计规范
- ⚡ 流畅的用户体验，响应式设计
- 🔧 组件化开发，代码复用性高
- 📱 适配不同尺寸的手机屏幕

### 后端特点
- 🛡️ 安全性高，JWT认证，权限控制
- 🚀 性能优秀，Redis缓存，数据库优化
- 📊 数据统计完善，支持多维度分析
- 🔌 API设计规范，支持版本管理

## 开发环境

### 前端环境
- 微信开发者工具
- Node.js 14+
- 微信小程序基础库 2.19.4+

### 后端环境
- Python 3.9+
- Django 4.2
- MySQL 8.0
- Redis 6.0

## 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/keiyoui/english-vocabulary-miniprogram.git
cd english-vocabulary-miniprogram
```

### 2. 后端开发
```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 数据库迁移
python manage.py migrate

# 启动开发服务器
python manage.py runserver
```

### 3. 小程序开发
```bash
# 使用微信开发者工具打开 miniprogram 目录
# 配置AppID和服务器域名
```

## 部署说明

### 后端部署
- 使用Docker容器化部署
- 支持Nginx反向代理
- 配置SSL证书
- 数据库主从分离

### 小程序部署
- 提交微信小程序审核
- 配置生产环境API地址
- 发布正式版本

## 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 联系方式

- 项目维护者: keiyoui
- 邮箱: 308864210@qq.com
- 项目地址: [https://github.com/keiyoui/english-vocabulary-miniprogram](https://github.com/keiyoui/english-vocabulary-miniprogram)

## 更新日志

### v1.0.0 (计划中)
- ✅ 项目架构设计完成
- ✅ UI设计图完成
- ✅ 需求分析文档完成
- 🔄 后端开发进行中
- 🔄 小程序开发进行中

---

⭐ 如果这个项目对您有帮助，请给我们一个星标！ 