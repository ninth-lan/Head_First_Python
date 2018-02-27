Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> try:
	data=open("missing.txt")
	print(data.readline(),end='')
except IOError:
	print('File error')
finally:
	data.close()

	
File error
Traceback (most recent call last):
  File "<pyshell#8>", line 7, in <module>
    data.close()
NameError: name 'data' is not defined
>>> try:
	data=open("missing.txt")
	print(data.readline(),end='')
except IOError:
	print('File error')
finally:
	if 'data' in locals():
		data.close()

		
File error
>>> try:
	data=open("missing.txt")
	print(data.readline(),end='')
except IOError:
	print('File error')
finally:
	if 'data' in locals():
		data.close()
	else:
		print("aaaaa")

		
File error
aaaaa
>>> try:
	data=open("missing.txt")
	print(data.readline(),end='')
except IOError as err:
	print('File error: ' +err)
finally:
	if 'data' in locals():
		data.close()

		
Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    data=open("missing.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#18>", line 5, in <module>
    print('File error: ' +err)
TypeError: Can't convert 'FileNotFoundError' object to str implicitly
>>> try:
	data=open("missing.txt")
	print(data.readline(),end='')
except IOError as err:
	print('File error: ' +str(err))
finally:
	if 'data' in locals():
		data.close()

		
File error: [Errno 2] No such file or directory: 'missing.txt'
>>> 
