#!/usr/bin/env python
"""
Python 3.13 兼容的依赖安装脚本
"""

import subprocess
import sys
import os

def run_command(command, description):
    """运行命令并显示结果"""
    print(f"\n{description}...")
    print(f"执行命令: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ 成功")
            if result.stdout:
                print(f"输出: {result.stdout}")
        else:
            print("❌ 失败")
            print(f"错误: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ 执行失败: {e}")
        return False
    
    return True

def main():
    """主安装函数"""
    print("=" * 60)
    print("Python 3.13 依赖安装脚本")
    print("=" * 60)
    
    # 检查Python版本
    python_version = sys.version_info
    print(f"当前Python版本: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major != 3 or python_version.minor < 9:
        print("❌ 需要Python 3.9或更高版本")
        return
    
    # 升级pip
    print("\n1. 升级pip...")
    run_command("python313 -m pip install --upgrade pip", "升级pip")
    
    # 安装基础依赖
    print("\n2. 安装基础依赖...")
    
    # 先安装Django
    if not run_command("python313 -m pip install Django>=4.2.7", "安装Django"):
        print("尝试安装最新版本的Django...")
        run_command("python313 -m pip install Django", "安装最新版Django")
    
    # 安装DRF
    if not run_command("python313 -m pip install djangorestframework>=3.14.0", "安装DRF"):
        print("尝试安装最新版本的DRF...")
        run_command("python313 -m pip install djangorestframework", "安装最新版DRF")
    
    # 安装其他依赖
    dependencies = [
        "djangorestframework-simplejwt",
        "django-cors-headers", 
        "django-simpleui",
        "django-redis",
        "gunicorn",
        "celery",
        "redis",
        "Pillow",
        "python-decouple",
        "django-filter",
        "drf-yasg"
    ]
    
    for dep in dependencies:
        run_command(f"python313 -m pip install {dep}", f"安装{dep}")
    
    # 尝试安装mysqlclient
    print("\n3. 安装MySQL客户端...")
    if not run_command("python313 -m pip install mysqlclient", "安装mysqlclient"):
        print("mysqlclient安装失败，尝试安装PyMySQL作为替代...")
        run_command("python313 -m pip install PyMySQL", "安装PyMySQL")
        
        # 如果使用PyMySQL，需要修改Django设置
        print("\n注意: 如果使用PyMySQL，需要在settings.py中添加以下代码:")
        print("import pymysql")
        print("pymysql.install_as_MySQLdb()")
    
    # 检查安装结果
    print("\n4. 检查安装结果...")
    run_command("python313 -m pip list", "查看已安装的包")
    
    print("\n" + "=" * 60)
    print("安装完成！")
    print("=" * 60)
    
    print("\n下一步操作:")
    print("1. 检查项目: python313 check_project.py")
    print("2. 数据库迁移: python313 manage.py makemigrations")
    print("3. 执行迁移: python313 manage.py migrate")
    print("4. 创建超级用户: python313 manage.py createsuperuser")
    print("5. 运行服务器: python313 manage.py runserver")

if __name__ == '__main__':
    main() 