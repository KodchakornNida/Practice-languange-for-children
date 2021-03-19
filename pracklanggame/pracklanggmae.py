#pracklanggame

class Student:
	def __init__(self,name):   #function __int__เป็นfunction พิเศษ ให้มันRunได้
		self.name = name    # self เป็นเหมือนคำพิเศษใช้แทนตัวเอง เวลาเอาไปประกาศ
		self.exp = 0
		self.lesson = 0
		#Call Function
		# self.AddEXP(10) # ให้คะแนนมาสมัครครั้งแรก
		# student1.name
		# self = student1

	def Hello(self):
		print(f'สวัสดีจ้าาาาา ผมชื่อ {self.name}')

	def Coding(self):
		print(f'{self.name} : กำลังเขียนโปรแกรม')
		self.exp += 5
		self.lesson += 1

	def ShowEXP(self):
		print(f'- {self.name} มีประสบการณ์ {self.exp} EXP')
		print(f'- เรียนไป {self.lesson} ครั้ง')

	def AddEXP(self, score):
		self.exp += score
		self.lesson += 1

# คะแนนพิเศษ ไม่ต้องบวกก่อน
# class SpecialScore:    # SpecialScore(): ไม่ต้องใส่ () ไม่มีต้องใส่เพิ่ม Student or score
# 	def __init__(self):
# 		self.score = 500

####เป็นรูปแบบพิเศษ Inheritant  #case เด็กเส้น แยกออกมา 
class SpecialStudent(Student):  
	def __init__(self,name,father):
		super().__init__(name)  #init นี้เป็นการแทนstudent class
		self.father = father
		mafia = ['Bill Gates','Prayut','Elon musk','sia O No.10']
		if father in mafia:
			self.exp += 100

	def AddEXP(self,score):  #เด็กเส้น คะแนนเพิ่ม * 3
		self.exp += (score * 3)
		self.lesson += 1

	def ArkEXP(self,score=10): #เด็กเส้นขอคะแนนเพิ่ม
		print(f'ขู่ครู!!!!  ขอคะแนนพิเศษให้หน่อยสัก {score} EXP')
		self.AddEXP(score)




if __name__ == '__main__':  #เป็นการเช็คว่าอยู่ใน file packlanggame นี้จริงๆ

	# เป็นการ check ว่า __name__ อยู่ใน file __main__ หรือไม่ ว่ามันอยู่ในfile __main__ไม่ได้ถูก import ไปหา file อื่น ****มันจะสามารถrun ได้******

	##################### SHOW RESULT ##########################################################################
	print('============1 Jan 2021=============')
	student0 = SpecialStudent('Mark Zuckerberg','Elon musk')  #SpecialStudent('ชื่อลูก','ชื่อพ่อ')
	student0.ArkEXP()  # score = 10 * 3 
	student0.ShowEXP()

	student1 = Student('Albert')   #ประกาศตัวแปร
	print(student1.name)
	student1.Hello()

	print('-'*40)

	student2 = Student('Steve')
	print(student2.name)
	student2.Hello()

	print('============2 Jan 2021=============')
	print('-------------uncle: ใครอยากเรียนโค้ดดิ้งบ้าง?????---(10 exp.)--------')
	# ถ้าเรามานั่งเขียน  student1.exp += 10 ,student1.lesson += 10 มีโอกาสใส่พลาดได้
	student1.AddEXP(10)

	print('============3 Jan 2021=============')
	student1.name = 'Bruno Fernandes'   # ปป.ชื่อทีหลัง
	print('ตอนนี้ exp องแต่ละคนได้เท่าไหร่กันแล้ว')
	print(student1.name,student1.exp)
	print(student2.name,student2.exp)

	print('============4 Jan 2021=============')
	for i in range(5):
		student2.Coding()

	student1.ShowEXP()
	student2.ShowEXP()