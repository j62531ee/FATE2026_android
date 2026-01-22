#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GUI测试 - 验证紫微命盘主星显示
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
from mingli_suite_v23_final import EnhancedFATESuiteGUI

def quick_test():
    """快速GUI测试"""
    print("="*70)
    print("       GUI紫微命盘主星显示测试")
    print("="*70)
    
    # 创建主窗口
    root = tk.Tk()
    root.title("FATE Suite v2.3 - 紫微主星测试")
    root.geometry("1200x800")
    
    # 创建GUI实例
    app = EnhancedFATESuiteGUI(root)
    
    # 自动填入测试数据
    app.date_entry.delete(0, tk.END)
    app.date_entry.insert(0, "1990/05/15")
    
    app.hour_entry.delete(0, tk.END)
    app.hour_entry.insert(0, "14")
    
    app.gender_var.set("男")
    app.blood_var.set("A")
    
    # 创建一个提示窗口
    tip_window = tk.Toplevel(root)
    tip_window.title("测试说明")
    tip_window.geometry("500x300")
    
    tip_text = """
    紫微命盘主星显示功能测试
    
    测试步骤：
    1. 程序已自动填入测试数据：
       - 出生日期：1990/05/15
       - 出生时间：14时
       - 性别：男
       - 血型：A
    
    2. 点击"开始完整分析"按钮
    
    3. 等待分析完成（约5-10秒）
    
    4. 切换到"紫微"标签页
    
    5. 验证以下内容：
       ✓ 命盘图中显示所有宫位的主星
       ✓ 命宫主星名称
       ✓ 夫妻宫主星名称
       ✓ 财帛宫主星名称
       ✓ 官禄宫主星名称
       ✓ 田宅宫主星名称
       ✓ 其他宫位主星名称
    
    6. 向下滚动查看12宫位详细分析
    
    关闭此窗口开始测试。
    """
    
    label = tk.Label(tip_window, text=tip_text, justify=tk.LEFT, padx=20, pady=20)
    label.pack()
    
    def close_tip():
        tip_window.destroy()
        print("\n✓ 测试数据已自动填入")
        print("✓ 请点击'开始完整分析'按钮进行测试")
        print("✓ 分析完成后切换到'紫微'标签页查看结果\n")
    
    close_button = tk.Button(tip_window, text="开始测试", command=close_tip, 
                             font=("微软正黑体", 12), bg="#4CAF50", fg="white",
                             padx=20, pady=10)
    close_button.pack(pady=20)
    
    # 运行主循环
    root.mainloop()

if __name__ == "__main__":
    quick_test()
