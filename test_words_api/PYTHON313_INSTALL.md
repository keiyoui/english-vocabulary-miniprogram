# Python 3.13 安装指南

## 问题说明

Python 3.13 是一个相对较新的版本，某些包可能还没有完全支持。以下是解决方案：

## 解决方案

### 方案1: 使用兼容的requirements文件

```bash
# 使用Python 3.13兼容的requirements文件
python313 -m pip install -r requirements_python313.txt
```

### 方案2: 逐个安装依赖

```bash
# 升级pip
python313 -m pip install --upgrade pip

# 安装核心依赖
python313 -m pip install Django>=4.2.0
python313 -m pip install djangorestframework>=3.14.0
python313 -m pip install djangorestframework-simplejwt>=5.3.0
python313 -m pip install django-cors-headers>=4.3.0
python313 -m pip install django-simpleui>=2023.12.0

# 安装数据库驱动 (使用PyMySQL替代mysqlclient)
python313 -m pip install PyMySQL>=1.1.0

# 安装其他依赖
python313 -m pip install django-redis>=5.4.0
python313 -m pip install redis>=5.0.0
python313 -m pip install gunicorn>=21.2.0
python313 -m pip install celery>=5.3.0
python313 -m pip install Pillow>=10.0.0
python313 -m pip install python-decouple>=3.8
python313 -m pip install django-filter>=23.0
python313 -m pip install drf-yasg>=1.21.0
python313 -m pip install requests>=2.31.0
```

### 方案3: 使用安装脚本

```bash
# 运行自动安装脚本
python313 install_dependencies.py
```

## 常见错误及解决方案

### 1. mysqlclient 安装失败

**错误信息**: `mysqlclient` 编译失败

**解决方案**: 使用 PyMySQL 替代
```bash
python313 -m pip install PyMySQL>=1.1.0
```

项目已配置支持 PyMySQL，无需额外修改。

### 2. 某些包版本冲突

**解决方案**: 使用 `>=` 而不是 `==` 来安装包
```bash
python313 -m pip install Django>=4.2.0
```

### 3. 编译错误

**解决方案**: 安装编译工具
```bash
# Windows
# 安装 Visual Studio Build Tools

# Linux
sudo apt-get install python3-dev build-essential

# macOS
xcode-select --install
```

## 验证安装

安装完成后，运行以下命令验证：

```bash
# 检查项目完整性
python313 check_project.py

# 测试Django
python313 manage.py check

# 查看已安装的包
python313 -m pip list
```

## 下一步操作

安装成功后，继续以下步骤：

1. **数据库迁移**
   ```bash
   python313 manage.py makemigrations
   python313 manage.py migrate
   ```

2. **创建超级用户**
   ```bash
   python313 manage.py createsuperuser
   ```

3. **初始化数据**
   ```bash
   python313 init_data.py
   ```

4. **启动服务器**
   ```bash
   python313 manage.py runserver
   ```

## 注意事项

1. **Python版本**: 确保使用 Python 3.9+ 版本
2. **虚拟环境**: 建议使用虚拟环境隔离依赖
3. **数据库**: 确保MySQL服务正在运行
4. **网络**: 如果网络有问题，可以使用国内镜像源

## 使用国内镜像源

如果网络连接有问题，可以使用国内镜像源：

```bash
python313 -m pip install -r requirements_python313.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

或者：

```bash
python313 -m pip install -r requirements_python313.txt -i https://mirrors.aliyun.com/pypi/simple/
``` 