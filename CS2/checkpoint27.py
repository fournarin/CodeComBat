# ใช้ฟังก์ชัน checkAndAttack เพื่อทำให้โค้ดของคุณอ่านง่ายขึ้น

# ฟังก์ชันนี้มีพารามิเตอร์
# ตัวแปรพารามิเตอร์คือวิธีส่งข้อมูลเข้าไปในฟังก์ชัน
def checkAndAttack(target):
    # 'target' parameter เป็นแค่ตัวแปร!
    # มันมีอาร์กิวเมนต์เมื่อมีการเรียกฟังก์ชัน
    if target:
        hero.attack(target)
    hero.moveXY(43, 34)

while True:
    hero.moveXY(58, 52)
    topEnemy = hero.findNearestEnemy()
    # ใช้ฟังก์ชัน checkAndAttack กับตัวแปร topEnemy
    checkAndAttack(topEnemy)

    # ไปที่เครื่องหมาย X ล่างสุด
    hero.moveXY(58, 16)
    # สร้างตัวแปรชื่อ bottomEnemy และค้นหาศัตรูที่อยู่ใกล้ที่สุด
    bottomEnemy = hero.findNearestEnemy()
    # ใช้ฟังก์ชัน checkAndAttack และรวมถึงตัวแปร bottomEnemy ด้วย
    checkAndAttack(bottomEnemy)
