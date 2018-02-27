
import PrintNester
import os
import pickle
'''
list1 = [1,'as','dd',[2,'dfd','wqw','rwe',['da',3,['dd',4],'fda','ds']]]
PrintNester.print_list (list1)
"""等价于PrintNester.print_list (list1，0)，因为这里函数设置了默认参数"""
print('1==================================================')
PrintNester.print_list(list1,True)
print('2==================================================')
PrintNester.print_list(list1,True,2)

'''

"""
os.chdir ('E:\\qsl\\learning\\Python')
man = []
other = []
try:
        with open('Sketch.txt') as data:
                for each_line in data:
                        try:
                                (role,line_spoken)=each_line.split(':',1)
                                line_spoken=line_spoken.strip()
                                if role == 'Man':
                                        man.append(line_spoken)
                                elif role == 'Other Man':
                                        other.append(line_spoken)
                        except ValueError:
                                pass
        data.close()
except IOError:
    print("The datafile is missing!")
"""
"""
try:
        with open('man_data.txt','w')as man_file:
                PrintNester.print_list(man, fh=man_file)
        with open('other_data.txt','w')as other_file:
                PrintNester.print_list(other,fh=other_file)
except IOError as err:
	print('File Error: '+str(err))
"""
'''
try:#采用dump保存文件，wb参数代表二进制保存，需要导入pickle模块
        with open('man_data1.txt','wb')as man_file,open('other_data1.txt','wb')as other_file:
                pickle.dump(man, man_file)
                pickle.dump(other,other_file)
except IOError as err:
	print('File Error: '+str(err))
except pickle.PickleError as peer:
        print('Pickling Error: '+str(peer))
'''

'''
>>> import PrintNester
>>> import pickle
>>> new_man=[]
>>> try:
	with open('man_data1.txt','rb') as man_file:
		new_man=pickle.load(man_file)
except IOError as err:
	print('File Error: '+str(err))
except pickle.PickleError as perr:
	print("Pickling Error: "+str(perr))

	
>>> PrintNester.print_list(new_man)
>>> print(new_man[0])#显示这个人讲的第一行
Is this the right room for an argument?
>>> print(new_man[-1])#显示这个人讲的最后一行
Yes it is!
'''

###------第5章代码-------#
###1. 初始读取文件
##os.chdir("E:\\qsl\\learning\\Python\\chapter5")
##with open("james.txt") as jaf:
##        data1=jaf.readline()
##james_data = data1.strip().split(',')
##with open("julie.txt") as juf:
##        data2=juf.readline()
##julie_data = data2.strip().split(',')
##with open("mikey.txt") as mif:
##        data3=mif.readline()
##mikey_data = data3.strip().split(',')
##with open("sarah.txt") as saf:
##        data4=saf.readline()
##sarah_data = data4.strip().split(',')
##"""
##print('===========1===============')
##print(james_data)
##print(julie_data)
##print(mikey_data)
##print(sarah_data)
##
##print('===========2===============')
##print(sorted(james_data))
##print(sorted(julie_data))
##print(sorted(mikey_data))
##print(sorted(sarah_data))
##
##"""
##'''
###两种排序方式：
###a. 原地排序（sort()方法，调用data=data.sort()）--按照指定的顺序排列数据，排序后的数据替换原来的数据，原来的顺序丢失
###b. 复制排序（soted()BIF，调用data2=sorted(data)）--按指定顺序排序，返回原数据的有序副本，原数据顺序依然保留，只是对副本排序
###2. 直接进行排序
##print('===========1===============')
##print('james_data: '+str(james_data))
##print('julie_data: '+str(julie_data))
##print('mikey_data: '+str(mikey_data))
##print('sarah_data: '+str(sarah_data))
##
##print('===========2（排序）===============')
##print('james_data_sorted: '+str(sorted(james_data)))
##print('julie_data_sorted: '+str(sorted(julie_data)))
##print('mikey_data_sorted: '+str(sorted(mikey_data)))
##print('sarah_data_sorted: '+str(sorted(sarah_data)))
##'''
##
##
###3. 处理数据然后进行排序
##def sanitize(time_string):
##        if '-' in time_string:
##                splitter='-'
##        elif ':' in time_string:
##                splitter=':'
##        else:
##                return time_string
##        (mins,secs)=time_string.split(splitter)
##        return(mins+'.'+secs)
##"""
##clean_james=[]
##clean_julie=[]
##clean_mikey=[]
##clean_sarah=[]
##
##for each_james in james_data:
##        clean_james.append(sanitize(each_james))
##
###for语句等价于以下语句，转换成一行代码利用列表推到来完成，这个列表推导隐含append()方法
###clean_james=[sanitize(each_james) for each_james in james_data]
##
##for each_julie in julie_data:
##        clean_julie.append(sanitize(each_julie))
##for each_mikey in mikey_data:
##        clean_mikey.append(sanitize(each_mikey))
##for each_sarah in sarah_data:
##        clean_sarah.append(sanitize(each_sarah))
##
##print('=====================处理1======================')
##print(clean_james)
##print(clean_julie)
##print(clean_mikey)
##print(clean_sarah)
##print('=====================处理2（排序）======================')
##
##print(sorted(clean_james))
###print(sorted(clean_james,reverse=True))#第二个参数表名数据降序排序
##print(sorted(clean_julie))
##print(sorted(clean_mikey))
##print(sorted(clean_sarah))
##
##
###4. 迭代删除重复项，打印最快的3次时间
##unique_james=[]
##for each_unique_james in sorted(clean_james):
##        if each_unique_james not in unique_james:
##                unique_james.append(each_unique_james)
##unique_julie=[]
##for each_unique_julie in sorted(clean_julie):
##        if each_unique_julie not in unique_julie:
##                unique_julie.append(each_unique_julie)
##unique_mikey=[]
##for each_unique_mikey in sorted(clean_mikey):
##        if each_unique_mikey not in unique_mikey:
##                unique_mikey.append(each_unique_mikey)
##unique_sarah=[]
##for each_unique_sarah in sorted(clean_sarah):
##        if each_unique_sarah not in unique_sarah:
##                unique_sarah.append(each_unique_sarah)
##print('===========最快3次============')
##print(unique_james)
##print(unique_julie[0:3])
##print(unique_mikey[0:3])
##"""
##'''
###5. 用集合删除重复项
##print('===========注释第2~4段代码,保留sanitize()方法============')
##print(sorted(set([sanitize(t) for t in james_data])))
##print(sorted(set([sanitize(t) for t in julie_data]))[0:3])
##print(sorted(set([sanitize(t) for t in mikey_data]))[0:3])
##print(sorted(set([sanitize(t) for t in sarah_data]))[0:3])
##'''
###6. 将第1部分的4个with语句改为函数然后进行调用
##
##def get_coach_data(filename):
##        try:#记住必须进行异常处理
##                with open(filename) as f:
##                        data=f.readline()
##                return(data.strip().split(','))
##        except IOError as ioerr:
##                print("File Error: "+str(ioerr))
##                return(None)
##james_data1 = get_coach_data('james.txt')
##julie_data1 = get_coach_data('julie.txt')
##mikey_data1 = get_coach_data('mikey.txt')
##sarah_data1 = get_coach_data('sarah.txt')
##print('====使用两个自定义函数的调用打印列表前三项数据===')
##print(sorted(set([sanitize(t) for t in james_data1]))[0:3])
##print(sorted(set([sanitize(t) for t in julie_data1]))[0:3])
##print(sorted(set([sanitize(t) for t in mikey_data1]))[0:3])
##print(sorted(set([sanitize(t) for t in sarah_data1]))[0:3])
##

#第6章 定制数据对象--打包代码与数据
os.chdir("E:\\qsl\\learning\\Python\\chapter6")

##def get_coach_data(filename):
##        try:#记住必须进行异常处理
##                with open(filename) as f:
##                        data=f.readline()
##                return(data.strip().split(','))
##        except IOError as ioerr:
##                print("File Error: "+str(ioerr))
##                return(None)
def sanitize(time_string):
        if '-' in time_string:
                splitter='-'
        elif ':' in time_string:
                splitter=':'
        else:
                return time_string
        (mins,secs)=time_string.split(splitter)
        return(mins+'.'+secs)

#1. 有额外的数据，抽取数据的名称及出生日期
##james_data1 = get_coach_data('james2.txt')
##julie_data1 = get_coach_data('julie2.txt')
##mikey_data1 = get_coach_data('mikey2.txt')
##sarah_data1 = get_coach_data('sarah2.txt')
##(james_name,james_dob) = james_data1.pop(0),james_data1.pop(0)
##print(james_name + "'s faster times are: " + str(sorted(set([sanitize(t) for t in james_data1]))[0:3]))
##(julie_name,julie_dob) = julie_data1.pop(0),julie_data1.pop(0)
##print(julie_name + "'s faster times are: " + str(sorted(set([sanitize(t) for t in julie_data1]))[0:3]))
##(mikey_name,mikey_dob) = mikey_data1.pop(0),mikey_data1.pop(0)
##print(mikey_name + "'s faster times are: " + str(sorted(set([sanitize(t) for t in mikey_data1]))[0:3]))
##(sarah_name,sarch_dob) = sarah_data1.pop(0),sarah_data1.pop(0)
##print(sarah_name + "'s faster times are: " + str(sorted(set([sanitize(t) for t in sarah_data1]))[0:3]))

#2. 使用字典关联数据，改写get_coach_data()，将print语句中的str(……)写入函数

def get_coach_data(filename):
        try:
                with open(filename) as f:
                        data=f.readline()
                temp=data.strip().split(',')
                return({'Name':temp.pop(0),
                        'Dob':temp.pop(0),
                        'Times':str(sorted(set([sanitize(t) for t in temp]))[0:3])})
        except IOError as ioerr:
                print("File Error: "+str(ioerr))
                return(None)
james_data2 = get_coach_data('james2.txt')
julie_data2 = get_coach_data('julie2.txt')
mikey_data2 = get_coach_data('mikey2.txt')
sarah_data2 = get_coach_data('sarah2.txt')

print(james_data2['Name']+"'s fastest times are: "+james_data2['Times'])
print(julie_data2['Name']+"'s fastest times are: "+julie_data2['Times'])
print(mikey_data2['Name']+"'s fastest times are: "+mikey_data2['Times'])
print(sarah_data2['Name']+"'s fastest times are: "+sarah_data2['Times'])


