import os
os.chdir ('E:\\qsl\\learning\\Python')

'''
#利用程序生成数据(打开读文件）
man=[]
other=[]
try:
    data=open('Sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            line_spoken=line_spoken.strip()     #strip()方法从字符串中去处不想要的空白符
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print("The datafile is missing!")
print('What the Man said:',end='')
print(man)
print('What the Other Man said:',end='')
print(other)
'''

"""
#以写模式打开文件

out=open("data.txt",'w')
print('Norwegian Blues stun easily.',file = out)
print('写入文件完成')
out.close()

"""

#将磁盘文件分别命名为man_data.txt（存储一个人讲的话）和other_data.txt（另一个人讲的话）

man=[]
other=[]
try:
    data=open('Sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            line_spoken=line_spoken.strip()     #strip()方法从字符串中去处不想要的空白符
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print("The datafile is missing!")

try:
    man_file=open("man_data.txt","w")
    other_file=open("other_data.txt","w")
    print(man,file=man_file)
    print(other,file=other_file)
    #man_file.close()   #假设第二个print语句运行异常，调用except语句，那么两个close语句不运行，需要用finally扩展try
    #other_file.close()
except IOError:
    print('File Error')
finally:#无论任何情况，finally中的代码都要运行
    man_file.close()
    other_file.close()
