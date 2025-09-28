###Task 1: Read a File and Handle Errors
'''file1=open('sample.txt','r')
reading_file1=file1.read()
print(reading_file1)
file1.close()'''

'''file1=open('sample.txt','r')
reading_file1=file1.read()
print(reading_file1)
file1.close()'''


###Task 2: Write and Append Data to a File

file1=open('output.txt','w')
write_file1=file1.write(input("write your text:"))
file1.close()

file1=open('output.txt','r')
reading_file1=file1.read()
file1.close()

file2=open('output.txt','a')
append_file2=file2.write('\nLearning file handling in Python')
file2.close()

file2=open('output.txt','r')
reading_file2=file2.read()
print(reading_file2)
file2.close()