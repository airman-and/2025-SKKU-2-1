import os

# 현재 스크립트의 디렉토리 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__))

try:
    # 파일 경로를 현재 디렉토리 기준으로 설정
    input_path = os.path.join(current_dir, '123.png')
    output_path = os.path.join(current_dir, 'kkk.png')
    
    infile = open(input_path, 'rb')
    outfile = open(output_path, 'wb')

    while True:
        copy_buffer = infile.read(1024)
        if not copy_buffer:
            break
        outfile.write(copy_buffer)
        
    infile.close()
    outfile.close()
    print("파일 복사가 성공적으로 완료되었습니다.")
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다. '{input_path}' 파일이 존재하는지 확인해주세요.")
except Exception as e:
    print(f"오류가 발생했습니다: {str(e)}")


