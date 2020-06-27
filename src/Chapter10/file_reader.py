# 文件名（默认优先查找当前工作目录）
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines() #读取文件全部行数据

#逐行输出
for line in lines:
    print(line.rstrip())

'''
因为read() 到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一
个空行。要删除多出来的空行，可在print 语句中使用rstrip() ：

Result:
3.1415926535
  8979323846
  2643383279
'''
