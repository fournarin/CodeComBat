# ตามรอยเหรียญไปยัง X สีแดงที่ทางออก

while True:
    # นี้จะพบไอเทมที่ใกล้ที่สุด
    item = hero.findNearestItem()
    if item:
        # สิ่งนี้จะเก็บ pos หรือตำแหน่งของไอเทมในตัวแปร
        itemPosition = item.pos
        # ใส่พิกัด X และ Y ของไอเทมลงในตัวแปร
        itemX = itemPosition.x
        itemY = itemPosition.y
        # ตอนนี้ ใช้ moveXY เพื่อย้ายไปที่ itemX และ itemY
        hero.moveXY(itemX, itemY)