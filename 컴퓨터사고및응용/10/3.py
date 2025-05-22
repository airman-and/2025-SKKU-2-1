filename = r"C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\컴퓨터사고및응용\10\words.txt"  # 절대 경로 설정
infile = open(filename, 'r', encoding='utf-8')

freqs = {}

for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1

print(freqs)
infile.close()
