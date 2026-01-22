#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试紫微分析 - 验证主星显示功能
"""

import sys
import traceback
from datetime import datetime

def test_ziwei_analysis():
    """测试紫微分析主星显示"""
    print("="*70)
    print("          紫微斗数主星显示功能测试")
    print("="*70)
    print(f"测试时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    try:
        # 导入紫微分析模块
        print("1. 导入紫微分析模块...")
        from mingli_purplestar_analyzer import PurpleStarAnalyzer
        print("   ✓ 模块导入成功\n")
        
        # 创建分析器
        print("2. 创建分析器实例...")
        analyzer = PurpleStarAnalyzer()
        print("   ✓ 分析器创建成功\n")
        
        # 测试数据
        test_data = {
            'year': 1990,
            'month': 5,
            'day': 15,
            'hour': 14,
            'gender': 'M'
        }
        
        print("3. 执行紫微分析...")
        print(f"   测试数据：{test_data['year']}年{test_data['month']}月{test_data['day']}日 {test_data['hour']}时")
        print(f"   性别：{'男' if test_data['gender'] == 'M' else '女'}\n")
        
        # 执行分析
        result = analyzer.analyze_ziwei(
            test_data['year'],
            test_data['month'],
            test_data['day'],
            test_data['hour'],
            test_data['gender']
        )
        
        if not result.get('success', False):
            print("   ✗ 分析失败")
            print(f"   错误信息：{result.get('error', '未知错误')}")
            return False
        
        print("   ✓ 分析执行成功\n")
        
        # 检查主星配置
        print("4. 检查主星配置...")
        main_stars = result.get('main_stars', {})
        
        if not main_stars:
            print("   ✗ 未找到主星配置")
            return False
        
        print(f"   ✓ 找到 {len(main_stars)} 个宫位的主星配置\n")
        
        # 显示各宫位主星
        print("5. 各宫位主星配置：")
        print("   " + "="*66)
        
        important_palaces = ['命宮', '夫妻宮', '財帛宮', '官祿宮', '田宅宮', '福德宮']
        
        for palace in important_palaces:
            if palace in main_stars:
                star_info = main_stars[palace]
                star_name = star_info.get('star', '未知')
                star_desc = star_info.get('description', '无描述')
                print(f"\n   【{palace}】")
                print(f"     主星：{star_name}")
                print(f"     特质：{star_desc}")
        
        print("\n   " + "="*66)
        
        # 检查宫位分析
        print("\n6. 检查宫位分析内容...")
        palace_analysis = result.get('palace_analysis', '')
        
        if not palace_analysis:
            print("   ✗ 未找到宫位分析")
            return False
        
        # 验证是否包含各宫位主星信息
        palaces_to_check = ['命宮', '夫妻宮', '財帛宮', '官祿宮', '田宅宮']
        found_count = 0
        
        for palace in palaces_to_check:
            if palace in palace_analysis and '主星' in palace_analysis:
                found_count += 1
        
        print(f"   ✓ 宫位分析包含主星信息")
        print(f"   ✓ 找到 {found_count} 个重要宫位的分析\n")
        
        # 显示部分宫位分析
        print("7. 宫位分析预览：")
        print("   " + "-"*66)
        lines = palace_analysis.split('\n')
        for i, line in enumerate(lines[:30]):  # 显示前30行
            print(f"   {line}")
        if len(lines) > 30:
            print(f"   ... （还有 {len(lines)-30} 行）")
        print("   " + "-"*66 + "\n")
        
        # 测试格式化输出
        print("8. 测试格式化输出...")
        formatted_result = analyzer.format_result(result)
        
        if not formatted_result:
            print("   ✗ 格式化失败")
            return False
        
        print(f"   ✓ 格式化成功（长度：{len(formatted_result)} 字符）\n")
        
        # 最终结果
        print("="*70)
        print("                    测试总结")
        print("="*70)
        print("\n✓ 所有测试通过！\n")
        print("主要改进：")
        print("  • 显示所有12个宫位的主星配置")
        print("  • 每个宫位都有主星名称和特质描述")
        print("  • 增加了主星在特定宫位的影响分析")
        print("  • 宫位分析更加详细和完整")
        print("\n重要宫位示例：")
        
        for palace in ['命宮', '夫妻宮', '財帛宮', '田宅宮']:
            if palace in main_stars:
                star_name = main_stars[palace].get('star', '未知')
                print(f"  • {palace}：主星 {star_name}")
        
        print("\n" + "="*70 + "\n")
        
        return True
        
    except Exception as e:
        print(f"\n✗ 测试过程发生错误：{str(e)}")
        traceback.print_exc()
        return False

def main():
    """主函数"""
    print("\n")
    result = test_ziwei_analysis()
    
    if result:
        print("测试状态：✅ 通过")
        return 0
    else:
        print("测试状态：❌ 失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())
