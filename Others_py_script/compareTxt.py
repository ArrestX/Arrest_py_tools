# 打开两个txt文件，读取内容到两个列表中
with open("file1.txt") as file1:
    lines1 = file1.readlines()
with open("file2.txt") as file2:
    lines2 = file2.readlines()

# 将两个列表中相同的行保存到一个新的txt文件中
with open("result.txt", "w") as result_file:
    for line in lines1:
        if line in lines2:
            result_file.write(line)
