#coding=utf-8

#用来保存学生的所有信息

studentInfos = []

#打印功能提示

def printMenu():

	print("="*70)
	print("			学生信息管理系统 V1.0			") 
	print("			                 			")
	print("			   1. 添加学生信息 			")
	print("			   2. 修改学生信息   			")
	print("			   3. 显示学生信息		    ")
	print("			   4. 保存学生信息		    ")
	print("			   0. 退出系统		        ")
	print("			                 			")
	print("="*70)

#获取一个学生信息

def getInfo():

	#3.1 提示并获取学生的学号
	newNum = input("请输入新学生的学号:")

	#3.2 提示并获取学生的姓名
	newName = input("请输入新学生的姓名:")

	#3.3 提示并获取学生的性别
	newSex = input("请输入新学生的性别(男/女):")
	
	#3.4 提示并获取学生的手机号码
	newPhone = input("请输入新学生的手机号码:")

	return {"num":newNum, "name":newName, "sex":newSex, "phone":newPhone}

#添加一个新学生的信息

def addInfo():

	result = getInfo()  

	newInfo = {}

	newInfo['num'] = result['num']
	newInfo['name'] = result['name']
	newInfo['sex'] = result['sex']
	newInfo['phone'] = result['phone']

	studentInfos.append(newInfo)

#修改一个学生的信息

def modifyInfo():

	#提示并获取修改学生的序号
	studentId = int(input("请输入修改学生的序号:"))

	result = getInfo()

	studentInfos[studentId - 1]['num'] = result['num']
	studentInfos[studentId - 1]['name'] = result['name']
	studentInfos[studentId - 1]['sex'] = result['sex']
	studentInfos[studentId - 1]['phone'] = result['phone']

#保存当前所有的学生信息到文件中

def saveToFile():

	f = open("studentInfos.data", "w")

	#[{},{},{}]
	f.write(str(studentInfos))

	f.close()

#恢复数据

def recoverData():

	global studentInfos
	f = open("studentInfos.data", "r")
	content = f.read()
	studentInfos = eval(content)
	f.close()

def main():

	#恢复之前的数据
	recoverData()

	while True:

		#1. 打印功能的提示
		printMenu()

		#2. 获取功能的选择
		key = input("请选择您的操作(1,2,3,4,0):")

		#3. 根据选择进行相应操作
		if key == "1": 

			#添加学生信息
			addInfo()

		elif key == "2":

			#修改学生信息
			modifyInfo()

		elif key == "3":

			#打印学生信息
			print("="*80)
			print(" "*80)
			print("学生信息如下:")
			print(" "*80)
			print("="*80)

			print("序号		学号		姓名		性别 	手机号码 	")
			
			i = 1
			for tempInfo in studentInfos:
				print("%d 		%s 		%s 		%s 		%s"%(i, tempInfo['num'], tempInfo['name'], tempInfo['sex'], tempInfo['phone']))

				i += 1

		elif key == "4":

			#保存数据到文件中
			saveToFile()



#调用主函数
main()



