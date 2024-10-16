# ไปทางขวาเพื่อไปถึงโอเอซิส
# ไปทางซ้ายเพื่อหลีกเลี่ยงจามรีที่อยู่ใกล้ๆ
while True:
    x = hero.pos.x
    y = hero.pos.y
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        # ลบ 10 จาก x เพื่อไปทางซ้าย
        x=x-10
        # ใช้ moveXY เพื่อย้ายไปยังตำแหน่ง x, y ใหม่
        hero.moveXY(x, y)
        pass
    else:
        # เพิ่ม 10 ไปที่ x เพื่อไปทางขวา
        x=x+10
        # ใช้ moveXY เพื่อย้ายไปยังตำแหน่ง x, y ใหม่
        hero.moveXY(x, y)
        pass