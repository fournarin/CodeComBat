# ตาม lightstone เพื่อค้นหากับดัก

while True:
    item = hero.findNearestItem()
    if item:
        # บันทึกตำแหน่งของรายการในตัวแปรใหม่โดยใช้ item.pos:
        itemPosition = item.pos
        # บันทึกพิกัด X และ Y โดยใช้ pos.x และ pos.y:
        itemX = itemPosition.x
        itemY = itemPosition.y
        # ไปยังพิกัดโดยใช้ตัวแปร moveXY() และตัวแปร X และ Y
        hero.moveXY(itemX, itemY)