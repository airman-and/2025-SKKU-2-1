def main():
    while True:
        filename = input("입력 파일 이름: ")
        try:
            with open(filename, 'r', encoding='utf-8'):
                # 파일을 성공적으로 열었으니 메시지 출력 후 루프 종료
                print("파일이 성공적으로 열렸습니다.")
                break
        except (IOError, FileNotFoundError):
            # 파일이 없거나 열 수 없을 때
            print(f"파일 {filename}이(가) 없습니다. 다시 입력하시오.")

if __name__ == "__main__":
    main()
