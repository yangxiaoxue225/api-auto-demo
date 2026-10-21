import pytest
import yaml
from apis.post_api import PostAPI

# 读取 YAML 文件里的测试数据
with open("data/posts.yaml", "r", encoding="utf-8") as f:
    post_data = yaml.safe_load(f)


class TestPosts:

    # 测试获取单篇文章
    def test_get_post(self):
        api = PostAPI()
        response = api.get_post(1)  # 获取第一篇文章
        assert response.status_code == 200
        assert response.json()["id"] == 1

    # 测试创建文章（使用 parametrize 进行数据驱动）
    @pytest.mark.parametrize("case", post_data["create_post_cases"])
    def test_create_post(self, case):
        api = PostAPI()
        # 从 YAML 的 case 字典里取出需要的变量
        response = api.create_post(case["payload"])

        # 断言 1：状态码
        assert response.status_code == case["expected_status"]
        # 断言 2：返回的 title 是否和我们传进去的一致
        assert response.json()["title"] == case["expected_title"]