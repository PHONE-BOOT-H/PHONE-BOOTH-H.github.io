import os
import subprocess

# 한글 오류 방지
env = os.environ.copy()
env["LC_ALL"] = "C.UTF-8"
env["LANG"] = "C.UTF-8"

# 1. Git 저장소 경로 설정
GIT_REPO_PATH = r"C:\Users\hanta\git\PHONE-BOOTH-H.github.io"

# 2. 저장소 디렉토리로 이동
os.chdir(GIT_REPO_PATH)

# 3. Git 명령어 실행 함수
def run_git_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"⚠️ 오류 발생: {result.stderr}")

# 4. Git Push 자동화
run_git_command("git add -A")
run_git_command('git commit -m "auto update"')
run_git_command("git push")
