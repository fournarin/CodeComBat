# คุณสามารถเขียนโค้ดก่อนลูป
hero.moveRight()
hero.moveUp()

# เปิด "Chest" ก่อนใช้ลูปหนีออกจากเขาวงกต!
hero.attack("Chest")
# กลับเข้าสู่โถงทางเดินหลัก
hero.moveDown()

while True:
    # ขยับ3 ครั้ง
    hero.moveRight(3)
    # ขยับอีก 3 ครั้ง
    hero.moveDown(3)
    
    