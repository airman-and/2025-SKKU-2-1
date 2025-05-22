def main():
    # 1) 파일 이름 입력
    filename = input("파일 이름을 입력하시오: ")

    # 2) 파일 읽기
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"파일 '{filename}'이(가) 없습니다.")
        return

    # 3) 번호 매기기
    numbered = []
    for idx, line in enumerate(lines, start=1):
        # 줄 끝 개행을 제거하고 번호와 함께 다시 줄바꿈
        numbered.append(f"{idx}: {line.rstrip()}")

    # 4) 같은 파일에 덮어쓰기
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for nl in numbered:
                f.write(nl + '\n')
        print("파일에 번호가 매겨져 저장되었습니다.")
    except IOError as e:
        print(f"파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
