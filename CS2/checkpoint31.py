# ตรวจสอบว่าเหมืองปลอดภัยสำหรับคนงานหรือไม่

def checkEnemyOrSafe(target):
    # หากมี `target` (พารามิเตอร์) อยู่:
    if target:
        # จากนั้นโจมตีเป้าหมาย
        hero.attack(target)
    # ไม่อย่างนั้น
    else:
        # ใช้ say() เพื่อเรียกชาวบ้าน
        hero.say("message")
        
    pass

while True:
    # เคลื่อนย้าย และเลือกเครื่องหมาย X ด้านบนขวา
    hero.moveXY(64, 54)
    enemy = hero.findNearestEnemy()
    checkEnemyOrSafe(enemy)
    
    # ย้ายไปที่เครื่องหมาย X ล่างซ้าย
    hero.moveXY(16, 14)
    # ให้บันทึกผลลัพธ์ของ findNearestEnemy() ในตัวแปร
    enemy = hero.findNearestEnemy();
    # เรียกcheckEnemyOrSafe แล้วส่ง
    checkEnemyOrSafe(enemy)
    # ผลลัพธ์ของ findNearestEnemy เป็นอาร์กิวเมนต์
    hero.moveXY(42, 34)
    enemy = hero.findNearestEnemy()
    checkEnemyOrSafe(enemy)
