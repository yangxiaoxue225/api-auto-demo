# 接口自动化测试框架 (api-auto-demo)

基于 Python + Pytest + Requests + YAML 数据驱动的接口自动化测试框架。

项目地址：[https://github.com/yangxiaoxue225/api-auto-demo](https://github.com/你的GitHub用户名/api-auto-demo)

## 📁 项目结构
- `config/`: 环境配置（BASE_URL 抽离）
- `apis/`: 接口层封装（API Object 模式）
``- `data/`: YAML 格式的测试数据（数据驱动）
``- `tests/`: 测试用例层

## 🛠️ 技术栈
- Python 3
- Requests (HTTP 请求)
- Pytest (测试框架)
- PyYAML (数据解析)

## 🚀 如何运行
1. 安装依赖：`pip install -r requirements.txt`
2. 运行测试：`python -m pytest tests/test_posts.py -v`