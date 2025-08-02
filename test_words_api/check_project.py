#!/usr/bin/env python
"""
项目完整性检查脚本
检查所有必要的文件和目录是否存在
"""

import os
import sys

def check_file_exists(file_path, description):
    """检查文件是否存在"""
    if os.path.exists(file_path):
        print(f"✓ {description}: {file_path}")
        return True
    else:
        print(f"✗ {description}: {file_path} (缺失)")
        return False

def check_directory_exists(dir_path, description):
    """检查目录是否存在"""
    if os.path.exists(dir_path):
        print(f"✓ {description}: {dir_path}")
        return True
    else:
        print(f"✗ {description}: {dir_path} (缺失)")
        return False

def main():
    """主检查函数"""
    print("=" * 50)
    print("英语单词量测试小程序后端项目检查")
    print("=" * 50)
    
    # 检查根目录文件
    print("\n1. 检查根目录文件:")
    root_files = [
        ('manage.py', 'Django管理脚本'),
        ('requirements.txt', '项目依赖文件'),
        ('README.md', '项目说明文档'),
    ]
    
    root_files_exist = True
    for file_path, description in root_files:
        if not check_file_exists(file_path, description):
            root_files_exist = False
    
    # 检查项目主目录
    print("\n2. 检查项目主目录:")
    project_files = [
        ('english_vocabulary/__init__.py', '项目初始化文件'),
        ('english_vocabulary/settings.py', '项目配置文件'),
        ('english_vocabulary/urls.py', '主URL配置'),
        ('english_vocabulary/wsgi.py', 'WSGI配置'),
        ('english_vocabulary/asgi.py', 'ASGI配置'),
    ]
    
    project_files_exist = True
    for file_path, description in project_files:
        if not check_file_exists(file_path, description):
            project_files_exist = False
    
    # 检查应用目录
    print("\n3. 检查应用目录:")
    apps = ['users', 'tests', 'vocabulary', 'ranking', 'statistics']
    
    apps_exist = True
    for app in apps:
        app_dir = f'apps/{app}'
        if not check_directory_exists(app_dir, f'{app}应用目录'):
            apps_exist = False
            continue
        
        # 检查每个应用的必要文件
        app_files = [
            f'apps/{app}/__init__.py',
            f'apps/{app}/models.py',
            f'apps/{app}/views.py',
            f'apps/{app}/urls.py',
            f'apps/{app}/admin.py',
            f'apps/{app}/serializers.py',
            f'apps/{app}/apps.py',
        ]
        
        for file_path in app_files:
            if not check_file_exists(file_path, f'{app}应用文件'):
                apps_exist = False
    
    # 检查apps目录的__init__.py
    if not check_file_exists('apps/__init__.py', 'apps目录初始化文件'):
        apps_exist = False
    
    # 总结
    print("\n" + "=" * 50)
    print("检查结果总结:")
    print("=" * 50)
    
    if root_files_exist and project_files_exist and apps_exist:
        print("✓ 项目结构完整，所有必要文件都存在")
        print("\n下一步操作:")
        print("1. 安装依赖: pip install -r requirements.txt")
        print("2. 数据库迁移: python manage.py makemigrations && python manage.py migrate")
        print("3. 创建超级用户: python manage.py createsuperuser")
        print("4. 运行服务器: python manage.py runserver")
        print("5. 访问后台管理: http://localhost:8000/admin/")
        print("6. 访问API文档: http://localhost:8000/swagger/")
    else:
        print("✗ 项目结构不完整，请检查缺失的文件")
        print("\n缺失的文件需要创建:")
        if not root_files_exist:
            print("- 根目录文件")
        if not project_files_exist:
            print("- 项目主目录文件")
        if not apps_exist:
            print("- 应用目录文件")
    
    print("\n" + "=" * 50)

if __name__ == '__main__':
    main() 