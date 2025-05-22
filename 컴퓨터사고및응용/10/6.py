import os

def search_python_in_files():
    # 현재 스크립트의 디렉토리를 기준으로 작업
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    
    # 현재 디렉토리의 txt 파일만 필터링
    txt_files = [f for f in os.listdir() if f.endswith('.txt')]
    print("검색할 텍스트 파일들:", txt_files)
    found_count = 0
    
    for f in txt_files:
        try:
            with open(f, 'r', encoding='utf-8') as infile:
                for line_num, line in enumerate(infile, 1):
                    e = line.rstrip()
                    if "Python" in e:
                        print(f"{f} : {e}")
                        found_count += 1
        except Exception as e:
            print(f"파일 {f} 처리 중 오류 발생:", str(e))
    
    print(f"\n총 {found_count}개의 'Python' 문자열을 찾았습니다.")

if __name__ == "__main__":
    search_python_in_files()
