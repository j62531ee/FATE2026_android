@echo off
chcp 65001 >nul
title FATE Suite v2.3.1 Final - 紫微主星完整版
echo.
echo ╔══════════════════════════════════════════════════╗
echo ║                                                  ║
echo ║   FATE Suite v2.3.1 Final - 紫微主星完整版        ║
echo ║                                                  ║
echo ╚══════════════════════════════════════════════════╝
echo.
echo 正在啟動 FATE Suite v2.3.1 Final...
echo 新功能：紫微斗數12宮位主星完整顯示
echo.

python mingli_suite_v23_final.py

if errorlevel 1 (
    echo.
    echo ╔══════════════════════════════════════════════════╗
    echo ║  程式執行時發生錯誤！                              ║
    echo ╚══════════════════════════════════════════════════╝
    echo.
    pause
) else (
    echo.
    echo 程式已正常關閉。
)
