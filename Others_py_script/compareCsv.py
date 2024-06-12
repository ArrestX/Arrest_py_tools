import csv

# 打开第一个csv文件
with open('csv1.csv', 'r') as f1:
    reader1 = csv.reader(f1)
    data1 = [row for row in reader1]

# 打开第二个csv文件
with open('csv2.csv', 'r') as f2:
    reader2 = csv.reader(f2)
    data2 = [row for row in reader2]

# 将两个csv文件转换为txt文件
with open('file1.txt', 'w') as f1_txt:
    for row in data1:
        f1_txt.write('\t'.join(row) + '\n')

with open('file2.txt', 'w') as f2_txt:
    for row in data2:
        f2_txt.write('\t'.join(row) + '\n')

# 比较两个txt文件并输出相同的数据到新的文本文件中
with open('same_data.txt', 'w') as same_data:
    with open('file1.txt', 'r') as f1_txt, open('file2.txt', 'r') as f2_txt:
        for line1 in f1_txt:
            for line2 in f2_txt:
                if line1 == line2:
                    same_data.write(line1.strip() + '\n')
                    break
