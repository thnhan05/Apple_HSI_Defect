@echo off
chcp 65001 >nul
echo =======================================================
echo   Dang khoi dong Apple HSI & PCA Data Viewer...
echo =======================================================
call conda activate hsi
if %errorlevel% neq 0 (
    echo [Thong bao] Dang dung python truc tiep tu C:\Users\LENOVO\miniconda3\envs\hsi\python.exe
    C:\Users\LENOVO\miniconda3\envs\hsi\python.exe view_apple_data.py
) else (
    python view_apple_data.py
)
pause
