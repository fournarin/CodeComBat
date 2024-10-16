# ย้ายสัตว์เลี้ยงของคุณไปที่ปุ่มซ้ายหรือขวาตามต้องการ

def onHear(event):
    # หาผู้พิทักษ์ที่จะฟัง
    archer = pet.findNearestByType("archer")
    soldier = pet.findNearestByType("soldier")
    # หาก event.speaker เป็น archer
    if event.speaker == archer:
        # ย้ายไปที่ปุ่มซ้าย
        pet.moveXY(32, 30)
    # หาก event.speaker เป็น soldier
    if event.speaker == soldier:
        # ย้ายไปที่ปุ่มขวา
        pet.moveXY(48, 30)

pet.on("hear", onHear)

# คุณไม่จำเป็นต้องเปลี่ยนโค้ดด้านล่าง
# ฮีโร่ของคุณควรปกป้องทางขวาล่าง
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)