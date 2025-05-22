def main():
    filename = input("파일명을 입력하세요: ")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {filename}")
        return
    
    try:
        line_num = int(input("몇 번째 줄을 출력할까요?: "))
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
        return
    
    if 1 <= line_num <= len(lines):
        print(f"{line_num}번 행은 다음과 같습니다.")
        # 줄바꿈 문자 제거하고 출력
        print(lines[line_num - 1].rstrip('\n'))
    else:
        print("행 번호가 파일의 행 수를 벗어났습니다.")

if __name__ == "__main__":
    main()