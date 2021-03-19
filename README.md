# นี่คือตัวอย่างโปรแกรมสำหรับการเรียน     OOP

### วิธีติดตั้ง

เปิด CMD / Terminal

```python
pip install pracklanggame
```

### วิธีเล่น

เปิด IDLE ขึ้นมาแล้วพิมพ์...

```python
from pracklanggame import Student, SpecialStudent

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
```

พัฒนาโดย: นายกชกร เลื่อนสุขสันต์
FB: https://www.facebook.com/Kodchakorn Lernsuksarn
YouTube: https://www.youtube.com/Kodchakorn Lernsuksarn
