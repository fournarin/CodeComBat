# รอคำสั่งจากนักเล่นแร่แปรธาตุเพื่อเอาโพชั่นมา

# ตัวจัดการอีเวนท์สำหรับอีเวนท์ของสัตว์เลี้ยง "hear"
def onHear(event):
    # ให้หาโพชั่นที่ใกล้ที่สุด
    potion = pet.findNearestByType("potion")
    message = event.message
    # หากข้อความอีเวนท์คือ "Fetch"
    if message == "Fetch":
        # ให้สัตว์เลี้ยงไปรับโพชั่น
        pet.fetch(potion)
    # อื่น ๆ (สำหรับข้อความอื่น ๆ ):
    else:
        pet.moveXY(54, 34)
        # ใช้ pet.moveXY เพื่อให้กลับไปจุดสีแดง
        

pet.on("hear", onHear)

# คุณไม่จำเป็นต้องเปลี่ยนโค้ดด้านล่าง
while True:
    enemy = hero.findNearest(hero.findEnemies())
    if enemy:
        hero.attack(enemy)
    else:
        hero.moveXY(40, 34)