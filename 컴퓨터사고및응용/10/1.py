infile = open(r'C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\컴퓨터사고및응용\10\sales.txt', 'r', encoding='utf-8')
outfile = open(r'C:\Users\andycho\OneDrive\Desktop\2025 2학년 1학기\컴퓨터사고및응용\10\summary.txt', 'w', encoding='utf-8')

total = 0
count = 0

line = infile.readline()
while line != "":
    stripped = line.strip()
    if stripped != "":
        s = int(stripped)
        total += s
        count += 1
    line = infile.readline()

outfile.write("총매출 = " + str(total) + '\n')
if count > 0:
    outfile.write("평균 일매출 = " + str(total / count))
else:
    outfile.write("평균 일매출을 계산할 수 없습니다.")

infile.close()
outfile.close()
