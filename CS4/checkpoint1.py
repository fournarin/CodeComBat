# ใช้ loop วนซ้ำจนกว่าคุณจะนับการโจมตี 10 ครั้ง

attacks = 0
while attacks < 10:
    # โจมตีศัตรูที่ใกล้ที่สุด!
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    # เพิ่มขึ้น หมายถึง เพิ่มขึ้น 1
    # เพิ่มตัวแปร `attacks`
    attacks += 1

# เสร็จแล้วก็ถอยไปยังจุดซุ่มโจมตี
hero.say("I should retreat!") #∆ อย่าเพิ่งยืนพูดพล่ามสิ!
hero.moveXY(79, 33);