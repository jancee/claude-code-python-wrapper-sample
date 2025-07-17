# Claude Code Python Wrapper 示例项目

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/claude-code-python-wrapper.svg)](https://badge.fury.io/py/claude-code-python-wrapper)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

这是一个演示如何使用 [`claude-code-python-wrapper`](https://github.com/jancee/claude-code-python-wrapper) SDK 的完整示例项目。

## 🎯 项目概述

本项目通过一个实际的应用场景展示了如何使用 `claude-code-python-wrapper` SDK：
- 📚 **场景**：从10篇中文博客故事中提取关键词
- 🧵 **技术**：多线程并发处理，2个线程同时工作
- 🤖 **AI驱动**：使用Claude AI分析文本内容
- 📊 **输出**：结构化的CSV格式结果

## 📋 执行顺序

本项目包含3个主要脚本，**请严格按照数字顺序执行**：

1. **`1_test_sdk.py`** - 验证SDK和环境是否正确配置
2. **`2_extract_keywords.py`** - 执行多线程关键词提取任务
3. **`3_display_results.py`** - 展示和分析提取结果

💡 **为什么要按顺序执行？**
- 步骤1确保环境配置正确，避免后续错误
- 步骤2生成 `result.csv` 文件，步骤3需要读取此文件
- 循序渐进的执行方式帮助理解整个工作流程

## 📁 项目结构

```
claude-code-python-wrapper-sample/
├── blogs/                 # 📖 中文博客文件目录
│   ├── blog-1.md         # 小镇图书馆的奇遇
│   ├── blog-2.md         # 时空咖啡馆
│   ├── blog-3.md         # 月光下的竹林
│   ├── blog-4.md         # 老街的糖人师傅
│   ├── blog-5.md         # 海边的瓶中信
│   ├── blog-6.md         # 雨夜的出租车
│   ├── blog-7.md         # 书店里的猫
│   ├── blog-8.md         # 地铁站的小提琴手
│   ├── blog-9.md         # 修钟表的爷爷
│   └── blog-10.md        # 天台上的星空课
├── 1_test_sdk.py         # 🧪 步骤1：SDK测试脚本
├── 2_extract_keywords.py # 🚀 步骤2：多线程关键词提取
├── 3_display_results.py  # 📊 步骤3：结果展示脚本
├── requirements.txt       # 📦 项目依赖
├── README.md             # 📄 本文档
└── result.csv            # 📈 输出结果（运行后生成）
```

## ✨ 功能特性

- 🔄 **多线程并发**：使用2个线程同时处理不同的博客文件
- 🎯 **精准提取**：从每篇博客中提取3个最具代表性的关键词
- 📊 **结构化输出**：结果保存为CSV格式，便于后续分析
- 🛡️ **错误处理**：完善的异常处理和重试机制
- 📈 **进度监控**：实时显示处理进度和结果统计
- 🔍 **结果可视化**：提供结果展示脚本

## 🚀 快速开始

### 前置要求

1. **Python 3.10+**
2. **Claude CLI**：确保 `claudee` 命令已安装并可在 PATH 中访问

### 安装步骤

1. **克隆项目**

```bash
git clone https://github.com/jancee/claude-code-python-wrapper-sample.git
cd claude-code-python-wrapper-sample
```

2. **安装依赖**

```bash
pip install -r requirements.txt
```

### 按序执行（重要）

⚠️ **请按照以下顺序执行脚本，每个步骤都很重要！**

1. **步骤1：测试SDK环境**

```bash
python 1_test_sdk.py
```

2. **步骤2：执行关键词提取**

```bash
python 2_extract_keywords.py
```

3. **步骤3：查看结果**

```bash
python 3_display_results.py
```

## 📊 输出结果

程序运行后会生成 `result.csv` 文件，包含每篇博客的关键词：

```csv
博客文件,关键词1,关键词2,关键词3
blog-1.md,图书馆,穿越,林黛玉
blog-2.md,时空咖啡馆,平行人生,人生选择
blog-3.md,竹林,萤火虫,心灵
...
```

### 实际运行结果

```
=== 中文博客关键词提取工具 ===
使用 2 个线程处理
找到 10 个博客文件
线程 1 启动
线程 2 启动
✓ blog-1.md: 图书馆, 穿越, 林黛玉
✓ blog-2.md: 时空咖啡馆, 平行人生, 人生选择
...
✓ 结果已保存到 result.csv
✓ 成功处理 10 个博客文件
```

## 🛠️ 技术实现

### 多线程架构

```python
# 创建任务队列和结果队列
task_queue = queue.Queue()
results_queue = queue.Queue()

# 启动工作线程
for i in range(NUM_THREADS):
    t = threading.Thread(target=worker_thread, args=(i+1,))
    t.start()
    threads.append(t)
```

### SDK集成

```python
from claude_cli import ClaudeCLI

# 初始化Claude CLI
claude = ClaudeCLI(command="claudee")

# 执行查询
response = claude.query(prompt)
```

### 错误处理

```python
try:
    response = claude.query(prompt)
    if response.return_code == 0:
        # 处理成功结果
        keywords = parse_keywords(response.output)
    else:
        # 处理错误
        print(f"提取失败: {response.error}")
except Exception as e:
    print(f"发生异常: {str(e)}")
```

## 📝 博客故事简介

项目包含10个精心编写的中文短篇故事，每个都有独特的主题：

| 文件 | 标题 | 主题 |
|------|------|------|
| blog-1.md | 小镇图书馆的奇遇 | 穿越、文学、成长 |
| blog-2.md | 时空咖啡馆 | 平行世界、人生选择 |
| blog-3.md | 月光下的竹林 | 自然、神秘、内心 |
| blog-4.md | 老街的糖人师傅 | 传统工艺、希望 |
| blog-5.md | 海边的瓶中信 | 沟通、教育、温暖 |
| blog-6.md | 雨夜的出租车 | 父爱、同理心 |
| blog-7.md | 书店里的猫 | 陪伴、成长记忆 |
| blog-8.md | 地铁站的小提琴手 | 音乐、治愈、城市温度 |
| blog-9.md | 修钟表的爷爷 | 时间、传承、工匠精神 |
| blog-10.md | 天台上的星空课 | 科普、梦想、教育 |

## 🔧 自定义配置

### 调整线程数

```python
NUM_THREADS = 4  # 增加到4个线程
```

### 修改关键词数量

```python
KEYWORDS_PER_BLOG = 5  # 每篇博客提取5个关键词
```

### 自定义提示词

```python
prompt = f"""请分析以下中文故事，提取关键词：
要求：
1. 提取{KEYWORDS_PER_BLOG}个关键词
2. 关键词要能概括故事主题
3. 用逗号分隔，不要其他内容

故事内容：
{blog_content}
"""
```

### 添加更多博客

只需在 `blogs/` 目录下添加新的 `.md` 文件，程序会自动识别并处理。

## 📊 性能说明

- **处理速度**：2个线程并发，约30秒处理10篇博客
- **资源占用**：CPU使用率中等，内存占用小
- **扩展性**：支持处理任意数量的博客文件
- **容错性**：单个文件失败不影响整体处理

## 🐛 故障排除

### 常见问题

1. **Claude CLI 未找到**
   ```bash
   ✗ claudee 命令未找到
   ```
   **解决方案**：确保 `claudee` 已安装并在 PATH 中

2. **SDK 导入失败**
   ```bash
   ✗ 无法导入 SDK
   ```
   **解决方案**：运行 `pip install claude-code-python-wrapper`

3. **权限错误**
   ```bash
   ✗ Permission denied
   ```
   **解决方案**：确保有文件读写权限

### 调试模式

启用详细日志输出：

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 项目
2. 创建功能分支：`git checkout -b feature/new-feature`
3. 提交更改：`git commit -m 'Add some feature'`
4. 推送分支：`git push origin feature/new-feature`
5. 创建 Pull Request

## 📚 相关链接

- **主SDK项目**：[claude-code-python-wrapper](https://github.com/jancee/claude-code-python-wrapper)
- **PyPI包**：[claude-code-python-wrapper](https://pypi.org/project/claude-code-python-wrapper/)
- **Claude CLI文档**：[Claude Code文档](https://docs.anthropic.com/en/docs/claude-code)

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 👨‍💻 作者

- **jancee** - [GitHub](https://github.com/jancee)

## 🙏 致谢

- 感谢 [Anthropic](https://www.anthropic.com/) 提供优秀的 Claude AI
- 感谢开源社区的支持和贡献

---

如有问题或建议，请提交 [Issue](https://github.com/jancee/claude-code-python-wrapper-sample/issues) 或 [Pull Request](https://github.com/jancee/claude-code-python-wrapper-sample/pulls)。