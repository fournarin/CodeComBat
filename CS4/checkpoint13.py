# นี่คือรายการชื่อเพื่อนของคุณ
friendNames = ['Joan', 'Ronan', 'Nikita', 'Augustus']

# ดัชนีในลิสต์เริ่มที่ 0 ไม่ใช่ 1!
friendIndex = 0

# loop แต่ละชื่อในอาร์เรย์
# ฟังก์ชัน len() เป็นความยาวของรายการ
while friendIndex < len(friendNames):
    # ใช้วงเล็บเหลี่ยมแปลงชื่อจากรายการ
    friendName = friendNames[friendIndex]
    
    # บอกเพื่อนให้กลับบ้าน
    # ใช้ + เพื่อเชื่อมต่อสองสตริง
    hero.say(friendName + ', go home!')
    
    # เพิ่ม friendIndex เพื่อรับชื่อถัดไป
    friendIndex +=1
    
# ถอยกลับไปที่โอเอซิสและสร้าง "fence" บน X.
hero.moveXY(24, 30)
hero.buildXY("fence", 30, 30)