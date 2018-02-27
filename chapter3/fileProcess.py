import os   #从标准库导入‘OS’
os.getcwd()     #当前工作目录
os.chdir('E:\\qsl\\learning\\Python')     #切换到包含数据文件的文件夹
filePath=os.getcwd()     #确认现在在正确的目录

'''
data = open('Sketch.txt')   #打开一个命名文件，将文件赋至名为data的文件对象
print(data.readline(),end='')   #使用readline()方法从文件获取一个数据行然后显示
print(data.readline(),end='')
print(data.readline(),end='')

print('--------------分割线-----------------')

data.seek(0)    #使用seek()方法回到文件起始位置，当然对python文件也可使用tell()
for each_line in data:
    print(each_line,end='')
data.close()

'''
"""
data = open('Sketch.txt')   #打开一个命名文件，将文件赋至名为data的文件对象
for each_line in data: #split()第二个可选参数设置为1，数据只被分解为2部分
    if each_line.find(':')!=-1: #增加额外逻辑来避免没有":"情况的错误
        role=each_line.split(':')[0]
        line_spoken=each_line.split(':')[1]
    #在本例中，前两句等价于(role, line_spoken)=each_line.split(':',1)
        print(role, end=' ')
        print('said:', end=' ')
        print(line_spoken, end='')
data.close()
"""
'''
data = open('Sketch.txt')   #打开一个命名文件，将文件赋至名为data的文件对象
for each_line in data:  #处理异常
    try:    #如果函数调用失败，则不希望进行3个打印,则需要保护其下所有语句
        (role, line_spoken)=each_line.split(':',1)
        print(role, end=' ')
        print('said:', end=' ')
        print(line_spoken, end='')
    except:     #异常出现时，直接忽略
        pass
data.close()
'''
"""
#增加代码处理文件缺失
if os.path.exists('Sketch.txt'):  #检查文件是否存在，exits()参数为路径，本例直接指向文件
    data = open('Sketch.txt')  
    for each_line in data:
        if each_line.find(':')!=-1:
            (role, line_spoken)=each_line.split(':',1)
            print(role, end=' ')
            print('said:', end=' ')
            print(line_spoken, end='')
    data.close()

else:  #通知用户此文件不存在
    print('The data file is missing!')

"""

#增加一层异常处理来处理文件缺失
try:
    data = open('Sketch.txt')
    for each_line in data:  #处理异常
        try:
            (role, line_spoken)=each_line.split(':',1)
            print(role, end=' ')
            print('said:', end=' ')
            print(line_spoken, end='')
        except ValueError:     
            pass
    data.close()
except IOError:
    print('The data file is missing!')

else:  #没有在代码中捕捉到异常执行

    print('\n'+'没有异常')

finally:    #不论在代码中是否检测到异常都会执行
    print('all')
