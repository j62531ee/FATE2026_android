#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整測試 mingli_suite_v23_final.py
測試所有功能模組
"""

import sys
import traceback
from datetime import datetime

def test_imports():
    """測試模組導入"""
    print("="*70)
    print("測試 1: 模組導入測試")
    print("="*70)
    
    try:
        print("導入 mingli_astrology...")
        import mingli_astrology
        print("  ✓ mingli_astrology 導入成功")
        
        print("導入 mingli_blood_type_enhanced...")
        import mingli_blood_type_enhanced
        print("  ✓ mingli_blood_type_enhanced 導入成功")
        
        print("導入 mingli_bazi_analyzer...")
        import mingli_bazi_analyzer
        print("  ✓ mingli_bazi_analyzer 導入成功")
        
        print("導入 mingli_purplestar_analyzer...")
        import mingli_purplestar_analyzer
        print("  ✓ mingli_purplestar_analyzer 導入成功")
        
        print("導入 mingli_tarot...")
        import mingli_tarot
        print("  ✓ mingli_tarot 導入成功")
        
        print("導入 mingli_yijing...")
        import mingli_yijing
        print("  ✓ mingli_yijing 導入成功")
        
        print("導入 mingli_suite_v23_final...")
        import mingli_suite_v23_final
        print("  ✓ mingli_suite_v23_final 導入成功")
        
        print("\n✓✓✓ 所有模組導入測試通過！\n")
        return True
        
    except Exception as e:
        print(f"\n✗✗✗ 模組導入失敗：{str(e)}")
        traceback.print_exc()
        return False

def test_individual_modules():
    """測試各個分析模組"""
    print("="*70)
    print("測試 2: 各個分析模組功能測試")
    print("="*70)
    
    try:
        # 測試星座分析
        print("\n測試星座分析...")
        from mingli_astrology import ZodiacSignAnalyzer
        zodiac = ZodiacSignAnalyzer()
        result = zodiac.analyze_zodiac(5, 15)
        print(f"  ✓ 星座分析成功 (結果長度: {len(result)} 字元)")
        
        # 測試血型分析
        print("\n測試血型分析...")
        from mingli_blood_type_enhanced import BloodTypeAnalyzerEnhanced
        blood = BloodTypeAnalyzerEnhanced()
        result = blood.analyze_blood_type("A")
        print(f"  ✓ 血型分析成功 (結果長度: {len(result)} 字元)")
        
        # 測試八字分析
        print("\n測試八字分析...")
        from mingli_bazi_analyzer import BaziAnalyzer
        bazi = BaziAnalyzer()
        result = bazi.analyze(1990, 5, 15, 14, "男")
        print(f"  ✓ 八字分析成功 (結果長度: {len(result)} 字元)")
        
        # 測試紫微斗數
        print("\n測試紫微斗數...")
        from mingli_purplestar_analyzer import PurpleStarAnalyzer
        ps = PurpleStarAnalyzer()
        result = ps.analyze(1990, 5, 15, 14, 'M')
        print(f"  ✓ 紫微斗數分析成功 (結果長度: {len(result)} 字元)")
        
        # 測試塔羅占卜
        print("\n測試塔羅占卜...")
        from mingli_tarot import TarotAnalyzer
        tarot = TarotAnalyzer()
        result = tarot.draw_cards("1990-05-15", "人生運勢")
        print(f"  ✓ 塔羅占卜成功 (結果長度: {len(result)} 字元)")
        
        # 測試周易卜卦
        print("\n測試周易卜卦...")
        from mingli_yijing import YijingAnalyzer
        yijing = YijingAnalyzer()
        result = yijing.divine("1990-05-15", "人生運勢")
        print(f"  ✓ 周易卜卦成功 (結果長度: {len(result)} 字元)")
        
        print("\n✓✓✓ 所有模組功能測試通過！\n")
        return True
        
    except Exception as e:
        print(f"\n✗✗✗ 模組功能測試失敗：{str(e)}")
        traceback.print_exc()
        return False

def test_main_program_functions():
    """測試主程式的特殊函數"""
    print("="*70)
    print("測試 3: 主程式特殊功能測試")
    print("="*70)
    
    try:
        # 這裡不啟動GUI，只測試類別可以創建
        print("\n測試主程式類別創建...")
        import tkinter as tk
        from mingli_suite_v23_final import EnhancedFATESuiteGUI
        
        # 創建隱藏視窗測試
        root = tk.Tk()
        root.withdraw()  # 隱藏主視窗
        
        print("  ✓ Tkinter 根視窗創建成功")
        
        # 測試流年流月函數（不依賴GUI）
        print("\n測試流年流月分析函數...")
        app = EnhancedFATESuiteGUI(root)
        
        # 直接調用流年流月函數
        result = app.add_yearly_monthly_fortune(1990, 5, 15, 14, "男")
        print(f"  ✓ 流年流月分析成功 (結果長度: {len(result)} 字元)")
        print(f"\n流年流月分析結果預覽：")
        print(result[:500] + "..." if len(result) > 500 else result)
        
        root.destroy()
        
        print("\n✓✓✓ 主程式功能測試通過！\n")
        return True
        
    except Exception as e:
        print(f"\n✗✗✗ 主程式功能測試失敗：{str(e)}")
        traceback.print_exc()
        return False

def main():
    """主測試程式"""
    print("\n" + "="*70)
    print("      FATE Suite v2.3 Final - 完整測試程式")
    print("="*70)
    print(f"測試開始時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70 + "\n")
    
    # 執行所有測試
    results = []
    
    # 測試 1：模組導入
    results.append(("模組導入", test_imports()))
    
    # 測試 2：各模組功能
    if results[0][1]:  # 如果導入成功才繼續
        results.append(("模組功能", test_individual_modules()))
    else:
        print("跳過模組功能測試（導入失敗）")
        results.append(("模組功能", False))
    
    # 測試 3：主程式功能
    if results[0][1]:  # 如果導入成功才繼續
        results.append(("主程式功能", test_main_program_functions()))
    else:
        print("跳過主程式功能測試（導入失敗）")
        results.append(("主程式功能", False))
    
    # 測試總結
    print("\n" + "="*70)
    print("                     測試總結")
    print("="*70)
    print(f"測試結束時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    for test_name, result in results:
        status = "✓ 通過" if result else "✗ 失敗"
        print(f"  {test_name:15s}: {status}")
    
    all_passed = all(result for _, result in results)
    
    print("\n" + "="*70)
    if all_passed:
        print("          ✓✓✓ 所有測試通過！程式可以正常使用 ✓✓✓")
    else:
        print("          ✗✗✗ 有測試失敗！請檢查錯誤訊息 ✗✗✗")
    print("="*70 + "\n")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
