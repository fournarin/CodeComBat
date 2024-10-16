# แสดงวิธีการกำหนดฟังก์ชันที่เรียกว่า cleaveWhenClose
# ฟังก์ชันกำหนดพารามิเตอร์ที่เรียกว่า `target`
def cleaveWhenClose(target):
    if hero.distanceTo(target) < 5:
        pass
        # ใส่โค้ดโจมตีของคุณที่นี่
        # ถ้า Cleave พร้อม  ก็ Cleave เป้าหมาย
        if hero.isReady("cleave"):
            hero.cleave(target)
        # หรือ เพียงแค่โจมตี `target`!
        else:
            hero.attack(target)

# โค้ดนี้ไม่ได้เป็นส่วนหนึ่งของฟังก์ชัน
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # โปรดทราบว่าใน cleaveWhenClose เราเรียก `enemy` เป็น`target`
        cleaveWhenClose(enemy)
