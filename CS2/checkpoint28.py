# สุสานที่ถูกลืมในป่า!
# แต่พวกยักษ์โอเกอร์ก็ร้อนแรงเหมือนกัน
# ทำลายหลุมฝังศพในขณะที่ปกป้องตัวเองจากมันชกินส์

# ฟังก์ชั่นนี้ควรโจมตีศัตรูหากมีอยู่ ไม่อย่างนั้นให้โจมตีประตู!
def checkToDefend(target):
    # ตรวจสอบว่า `target` มีอยู่หรือไม่
    if target:
        # ถ้าใช่ ให้โจมตี `target`
        hero.attack(target)
    # ใช้ else เพื่อทำบางสิ่งหากไม่มี `target`
    else:
        # มิฉะนั้นโจมตี "Door"
        hero.attack("Door")
    pass

while True:
    enemy = hero.findNearestEnemy()
    checkToDefend(enemy)
