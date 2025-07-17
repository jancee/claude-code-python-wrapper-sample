#!/usr/bin/env python3
"""
使用 claude-code-python-wrapper SDK 从中文博客中提取关键词
使用多线程处理，2个线程分别处理不同的博客文件
"""

import os
import csv
import threading
import queue
from pathlib import Path
from claude_cli import ClaudeCLI, ClaudeOptions

# 配置
BLOGS_DIR = Path("blogs")
OUTPUT_FILE = "result.csv"
NUM_THREADS = 2
KEYWORDS_PER_BLOG = 3

# 创建任务队列
task_queue = queue.Queue()
results_queue = queue.Queue()

# 线程锁，用于安全写入结果
results_lock = threading.Lock()


def extract_keywords(blog_content: str, blog_name: str) -> list:
    """使用 Claude CLI 提取关键词"""
    # 初始化 Claude CLI
    claude = ClaudeCLI(command="claudee")
    
    # 构建提示词
    prompt = f"""请阅读以下中文博客内容，提取出3个最能代表这个故事的关键词。
只需要返回3个关键词，用逗号分隔，不要其他任何解释。

博客内容：
{blog_content}
"""
    
    try:
        # 执行查询
        response = claude.query(prompt)
        
        if response.return_code == 0:
            # 解析关键词
            keywords = [k.strip() for k in response.output.strip().replace('，', ',').split(',')][:3]
            print(f"✓ {blog_name}: {', '.join(keywords)}")
            return keywords
        else:
            print(f"✗ {blog_name}: 提取失败 - {response.error}")
            return []
            
    except Exception as e:
        print(f"✗ {blog_name}: 发生错误 - {str(e)}")
        return []


def worker_thread(thread_id: int):
    """工作线程函数"""
    print(f"线程 {thread_id} 启动")
    
    while True:
        try:
            # 获取任务（超时设置为1秒）
            blog_file = task_queue.get(timeout=1)
            
            # 读取博客内容
            blog_path = BLOGS_DIR / blog_file
            with open(blog_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取关键词
            keywords = extract_keywords(content, blog_file)
            
            # 将结果放入结果队列
            if keywords:
                results_queue.put({
                    'blog': blog_file,
                    'keywords': keywords
                })
            
            # 标记任务完成
            task_queue.task_done()
            
        except queue.Empty:
            # 队列为空，退出线程
            break
        except Exception as e:
            print(f"线程 {thread_id} 处理时出错: {str(e)}")
            task_queue.task_done()
    
    print(f"线程 {thread_id} 结束")


def main():
    """主函数"""
    print("=== 中文博客关键词提取工具 ===")
    print(f"使用 {NUM_THREADS} 个线程处理")
    
    # 获取所有博客文件
    blog_files = sorted([f for f in os.listdir(BLOGS_DIR) if f.endswith('.md')])
    print(f"找到 {len(blog_files)} 个博客文件")
    
    # 将博客文件加入任务队列
    for blog_file in blog_files:
        task_queue.put(blog_file)
    
    # 创建并启动工作线程
    threads = []
    for i in range(NUM_THREADS):
        t = threading.Thread(target=worker_thread, args=(i+1,))
        t.start()
        threads.append(t)
    
    # 等待所有任务完成
    task_queue.join()
    
    # 等待所有线程结束
    for t in threads:
        t.join()
    
    print("\n所有线程已完成，正在整理结果...")
    
    # 收集所有结果
    all_results = []
    while not results_queue.empty():
        all_results.append(results_queue.get())
    
    # 按博客名称排序
    all_results.sort(key=lambda x: x['blog'])
    
    # 写入CSV文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # 写入标题行
        writer.writerow(['博客文件', '关键词1', '关键词2', '关键词3'])
        
        # 写入数据
        for result in all_results:
            row = [result['blog']] + result['keywords']
            # 确保有3个关键词
            while len(row) < 4:
                row.append('')
            writer.writerow(row)
    
    print(f"\n✓ 结果已保存到 {OUTPUT_FILE}")
    print(f"✓ 成功处理 {len(all_results)} 个博客文件")
    
    # 显示结果摘要
    print("\n=== 提取结果摘要 ===")
    for result in all_results:
        keywords_str = ', '.join(result['keywords'])
        print(f"{result['blog']}: {keywords_str}")


if __name__ == "__main__":
    main()