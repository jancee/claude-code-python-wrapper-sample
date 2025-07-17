#!/usr/bin/env python3
"""测试 claude-code-python-wrapper SDK 是否正确安装"""

try:
    from claude_cli import ClaudeCLI, AsyncClaudeCLI, ClaudeOptions
    print("✓ SDK 导入成功！")
    print(f"  - ClaudeCLI: {ClaudeCLI}")
    print(f"  - AsyncClaudeCLI: {AsyncClaudeCLI}")
    print(f"  - ClaudeOptions: {ClaudeOptions}")
    
    # 测试初始化
    claude = ClaudeCLI(command="claudee")
    print("\n✓ ClaudeCLI 初始化成功！")
    
    # 简单测试
    print("\n正在测试基本功能...")
    response = claude.query("说'你好'")
    
    if response.return_code == 0:
        print(f"✓ 测试成功！Claude 回复: {response.output.strip()}")
    else:
        print(f"✗ 测试失败: {response.error}")
        
except ImportError as e:
    print(f"✗ 无法导入 SDK: {e}")
    print("\n请确保已安装 claude-code-python-wrapper:")
    print("  pip install claude-code-python-wrapper")
    
except RuntimeError as e:
    print(f"✗ claudee 命令未找到: {e}")
    print("\n请确保 claudee 命令已安装并在 PATH 中")
    
except Exception as e:
    print(f"✗ 发生错误: {e}")