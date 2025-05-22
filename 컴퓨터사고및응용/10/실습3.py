def main():
    # 1) 사용자 입력
    filename = input("파일 이름을 입력하시오: ")
    to_remove = input("삭제할 문자열을 입력하시오: ")

    # 2) 파일 읽기
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"파일 '{filename}'을(를) 찾을 수 없습니다.")
        return

    # 3) 문자열 삭제
    new_content = content.replace(to_remove, "")

    # 4) 파일에 덮어쓰기
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("변경된 파일이 저장되었습니다.")
    except IOError as e:
        print(f"파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
