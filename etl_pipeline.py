import subprocess
import time
import sys

def run_script(script_name):
    print("=" * 50)
    print(f"[INFO] 正在执行: {script_name} ...")
    start_time = time.time()
    
    # 使用 subprocess 执行外部 python 脚本
    # 强制使用 utf-8 编码读取，避免 Windows 下 GBK 报错
    result = subprocess.run(
        [sys.executable, script_name], 
        capture_output=True, 
        text=True, 
        encoding='utf-8', 
        errors='replace'
    )
    
    # 安全打印标准输出（防止 stdout 为空时报错）
    if result.stdout and result.stdout.strip():
        print(result.stdout.strip())
    
    # 判断是否执行失败
    if result.returncode != 0:
        print(f"[ERROR] {script_name} 执行失败！")
        if result.stderr:
            print("[ERROR DETAILS]:")
            print(result.stderr.strip())
        sys.exit(1)  # 失败则终止整个流程
        
    end_time = time.time()
    print(f"[SUCCESS] {script_name} 执行成功，耗时: {end_time - start_time:.2f} 秒")

if __name__ == "__main__":
    print("[START] 离线数仓全链路 ETL 任务开始 ...\n")
    
    scripts = [
        "step1_ods.py",
        "step2_dwd.py",
        "step3_dws.py",
        "step4_ads.py"
    ]
    
    for script in scripts:
        run_script(script)
        
    print("\n" + "=" * 50)
    print("[FINISH] 恭喜！整个数仓链路运行完毕！所有层级数据已更新。")