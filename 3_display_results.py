#!/usr/bin/env python3
"""显示关键词提取结果"""

import csv
import os
from pathlib import Path

def display_results(csv_file='result.csv'):
    """读取并显示CSV结果"""
    if not os.path.exists(csv_file):
        print(f"错误：找不到结果文件 {csv_file}")
        print("请先运行 extract_keywords.py")
        return
    
    print("="*70)
    print("中文博客关键词提取结果".center(70))
    print("="*70)
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # 跳过标题行
        
        results = list(reader)
        
    # 统计信息
    print(f"\n总计处理博客数: {len(results)}")
    print("\n详细结果：")
    print("-"*70)
    
    # 显示每篇博客的结果
    for row in results:
        if len(row) >= 4:
            blog_name = row[0]
            keywords = [k for k in row[1:4] if k]  # 过滤空值
            
            # 获取博客标题（从文件中读取第一行）
            blog_path = Path('blogs') / blog_name
            title = "未知标题"
            if blog_path.exists():
                with open(blog_path, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
                    if first_line.startswith('#'):
                        title = first_line.replace('#', '').strip()
            
            print(f"\n📖 {blog_name}")
            print(f"   标题: {title}")
            print(f"   关键词: {' | '.join(keywords)}")
    
    print("\n" + "-"*70)
    
    # 关键词统计
    all_keywords = []
    for row in results:
        if len(row) >= 4:
            keywords = [k for k in row[1:4] if k]
            all_keywords.extend(keywords)
    
    # 找出最常见的关键词
    from collections import Counter
    keyword_counts = Counter(all_keywords)
    
    print("\n📊 关键词频率统计（出现次数 > 1）：")
    print("-"*30)
    
    common_keywords = [(k, v) for k, v in keyword_counts.items() if v > 1]
    if common_keywords:
        for keyword, count in sorted(common_keywords, key=lambda x: x[1], reverse=True):
            print(f"   {keyword}: {count}次")
    else:
        print("   （所有关键词都只出现了1次）")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    display_results()