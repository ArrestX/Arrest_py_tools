import argparse
import os
import subprocess

__author__ = "Arrest"

# 设置Ghostscript的路径
ghostscript_path = r'C:\Program Files\gs\gs10.02.0\bin\gswin64.exe'


def title():
    print("""
   _____  ____  ____   ___  ____  
  / ____|/ ___|/ ___| / _ \|  _ \ 
 | |  __| |  _| |  _  | | | | |_) |
 | | |_ | |_| | |_| | |_| |  __/ 
  \____|\____|\____| \___/|_|    

    Author: Arrest
    Github: https://github.com/ArrestX                             
    """)
    print('''
    Usage:
    Compress a PDF: python pdf_compressor.py -i input.pdf [-o output.pdf]
    ''')


def compress_pdf(input_file, output_file):
    try:
        if output_file is None:
            output_file = os.path.basename(input_file).replace(".pdf", "_compressed.pdf")

        # 使用Ghostscript进行PDF压缩
        subprocess.call([ghostscript_path, "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
                         "-dPDFSETTINGS=/screen", "-dNOPAUSE", "-dQUIET", "-dBATCH",
                         f"-sOutputFile={output_file}", input_file])

        print(f"已压缩的PDF文件已保存到: {output_file}")

    except Exception as e:
        print(f"发生错误: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF压缩工具")
    parser.add_argument("-i", "--input", required=True, help="要压缩的PDF文件")
    parser.add_argument("-o", "--output", help="压缩后的PDF文件保存路径")

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    if not os.path.exists(input_file):
        print(f"指定的输入文件 '{input_file}' 不存在.")
    else:
        title()  # 打印标题和作者信息
        compress_pdf(input_file, output_file)
