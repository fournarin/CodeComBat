# เพื่อให้การฝึกอบรมน่าสนใจยิ่งขึ้น Senick จะวางยาพิษคุณ
# ในขณะที่คุณไม่ได้ขยับ  พิษจะไม่เป็นอันตราย

# ฟังก์ชันนี้ควรตรวจสอบว่าเหรียญอยู่ใกล้กว่า 20 เมตรหรือไม่
def isCoinClose(coin):
    # ค้นหาระยะทางไปยัง `coin'
    coin = hero.findNearestItem()
    distance = hero.distanceTo(coin)
    # หากระยะทางน้อยกว่า 20
    if distance < 20:
        # Return True
        return True
    # Else:
    else:
        # Return False
        return False
    pass

while True:
    item = hero.findNearestItem()
    if item:
        # หาก isCoinClose(item) คืนค่าเป็นจริง
        if isCoinClose(item):
            hero.moveXY(item.pos.x, item.pos.y)