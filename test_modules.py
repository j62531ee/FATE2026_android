#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
測試 FATE Suite v2.3
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

try:
    print("="*60)
    print("開始測試 FATE Suite v2.3")
    print("="*60)
    
    # 測試導入所有模組
    print("\n1. 測試導入模組...")
    from mingli_astrology import ZodiacSignAnalyzer, BloodTypeAnalyzer
    from mingli_blood_type_enhanced import BloodTypeAnalyzerEnhanced
    from mingli_bazi_analyzer import BaziAnalyzer
    from mingli_purplestar_analyzer import PurpleStarAnalyzer
    from mingli_tarot import TarotAnalyzer
    from mingli_yijing import YijingAnalyzer
    print("   ✓ 所有模組導入成功")
    
    # 測試基本功能
    print("\n2. 測試星座分析...")
    zodiac = ZodiacSignAnalyzer()
    result = zodiac.analyze_zodiac(5, 15)
    print(f"   ✓ 星座分析成功: {len(result)} 字元")
    
    print("\n3. 測試血型分析...")
    blood = BloodTypeAnalyzerEnhanced()
    result = blood.analyze_blood_type('A', '男')
    print(f"   ✓ 血型分析成功: {len(result)} 字元")
    
    print("\n4. 測試八字分析...")
    bazi = BaziAnalyzer()
    result = bazi.analyze_bazi(1990, 5, 15, 14)
    print(f"   ✓ 八字分析成功: {result['year_pillar']}")
    
    print("\n5. 測試紫微分析...")
    ps = PurpleStarAnalyzer()
    result = ps.analyze_ziwei(1990, 5, 15, 14, 'M')
    print(f"   ✓ 紫微分析成功: 命宮={result['ming_gong']}")
    
    print("\n6. 測試塔羅占卜...")
    tarot = TarotAnalyzer()
    result = tarot.draw_cards("1990-05-15", "測試")
    print(f"   ✓ 塔羅占卜成功: {len(result)} 字元")
    
    print("\n7. 測試周易卜卦...")
    yijing = YijingAnalyzer()
    result = yijing.divine("1990-05-15", "測試")
    print(f"   ✓ 周易卜卦成功: {len(result)} 字元")
    
    print("\n" + "="*60)
    print("✓ 所有基本功能測試通過！")
    print("="*60)
    
except Exception as e:
    print(f"\n✗ 測試失敗: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
