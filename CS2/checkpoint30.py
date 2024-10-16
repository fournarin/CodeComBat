# รวบรวม 4 lightstones เพื่อเอาชนะ Brawler
# หากคุณพบ lightstone ให้ซ่อนมันไว้

def checkTakeHide(item):
    if item:
        # ของมาแล้วครับ รับไปเลย
        hero.moveXY(item.pos.x, item.pos.y)
        # แล้วเคลื่อนไปกลางค่าย (40,34)
        hero.moveXY(40, 34)

while True:
    # ไปที่เครื่องหมาย X ด้านบนขวา
    hero.moveXY(68, 56)
    # ค้นหา lightstone ที่นั่น
    lightstone = hero.findNearestItem()
    # โทร checkTakeHide ด้วยอาร์กิวเมนต์: lightstone
    checkTakeHide(lightstone)
    
    # ไปที่เครื่องหมายด้านซ้ายบน
    hero.moveXY(12, 56)
    # ค้นหา lightstone
    item = hero.findNearestItem()
    # เรียกใช้ฟังก์ชัน checkTakeHide
    checkTakeHide(item)
    # ส่งผ่านผลการค้นหาของคุณเป็นอาร์กิวเมนต์
    
    
