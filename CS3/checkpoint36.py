# ให้จามรีเข้ามาใกล้แล้วขยับไปทางขวา 10 เมตรเพื่อหลบ
# หลบจามรี 4 ตัวเพื่อให้ผ่านด่าน

while True:
    # บันทึกตำแหน่ง x และ y ปัจจุบันของฮีโร่
    x = hero.pos.x
    y = hero.pos.y
    
    # ค้นหาจามรีที่ใกล้ที่สุด
    yak = hero.findNearestEnemy()
    
    # หาก distanceTo ถึงจามรีน้อยกว่า 10:
    if hero.distanceTo(yak) < 10:
        # หากต้องการไปทางขวา ให้เพิ่ม 10 ในตำแหน่ง x ของฮีโร่
        x=x+10
        # ใช้ moveXY(x, y) เพื่อเคลื่อนที่!
        hero.moveXY(x, y)
        pass