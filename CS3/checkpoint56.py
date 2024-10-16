# มีเพียงสัตว์เลี้ยงของคุณเท่านั้นที่สามารถปลุกพ่อมดได้

def onHear(event):
    # เหตุการณ์ "hear" ตั้งค่าคุณสมบัติ event.speaker
    # ตรวจสอบว่าสัตว์เลี้ยงเคยได้ยินฮีโร่หรือไม่
    if event.speaker == hero:
        pet.say("WOOF")

# กำหนดตัวจัดการอีเวนท์สำหรับอีเวนท์"hear"
pet.on("hear", onHear)

while True:
    enemy = hero.findNearestEnemy()
    # หากมีศัตรู:
    if enemy:
        # ใช้ hero.say() เพื่อเตือนสัตว์เลี้ยงของคุณ
        hero.say("!!")
        # เคลื่อนที่ไปที่ X ในค่าย
        hero.moveXY(30, 33)
        # แล้วออกมาที่ X นอกค่าย
        hero.moveXY(30, 15)