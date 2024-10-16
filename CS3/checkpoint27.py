# รับเหรียญก็ต่อเมื่ออยู่ใกล้กว่า 20 เมตรเท่านั้น
# หยิบอัญมณีทั้งหมด

while True:
    item = hero.findNearestItem()
    distance = hero.distanceTo(item)
    # หากประเภทไอเทมเป็น "gem"
    # หรือระยะทางไปยังรายการน้อยกว่า 20 เมตร
    if item.type == "gem" or distance < 20:
        # ไปยังตำแหน่งของรายการ
        hero.moveXY(item.pos.x, item.pos.y)