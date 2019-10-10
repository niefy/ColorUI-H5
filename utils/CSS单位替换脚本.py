"""
按固定比例替换文件中的单位
"""
import re
path="E:/projects/消息平台/源代码/message-client/src/css/"

def main():
    pattern = "(?P<value>\d+)upx"
    file=open(path+"ColorUi-backup.css","r",encoding="utf-8") #只读方式打开文件
    file_new = open(path+"ColorUi-H5.css","w+",encoding="utf-8") #保存修改后的文件，不存在则创建
    lines=file.readlines()
    for line in lines:
        str=re.sub(pattern, calculate, line)
        file_new.write(str)
    file.close()
    file_new.close()


def calculate(matched):# 单位换算
    value = int(matched.group('value'))
    return str(int(round(value /2)))+'px'

if __name__ == "__main__":
    main()