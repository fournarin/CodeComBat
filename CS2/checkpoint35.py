# จะสร้างก็ต่อเมื่อคุณเห็นศัตรู

# ฟังก์ชันกำหนดพารามิเตอร์สามตัว
def maybeBuildSomething(typeToBuild, x, y):
    hero.moveXY(x, y)
    # ค้นหาศัตรูที่ใกล้ที่สุด
    enemy = hero.findNearestEnemy()
    # หากมีศัตรู
    if enemy:
        # จากนั้นใช้ buildXY กับ typeToBuild, x และ y
        # ใช้ตัวแปร typeToBuild เป็นอาร์กิวเมนต์แรก
        hero.buildXY(typeToBuild, x, y)
    pass

# คุณไม่จำเป็นต้องเปลี่ยนโค้ดด้านล่าง
while True:
    # เรียก mayBuildSomething ด้วย "fire-trap" และพิกัดของ X ด้านล่าง
    maybeBuildSomething("fire-trap", 40, 20)
    # เรียกหา mayBuildSomething ด้วย "fence" ที่ X ทางซ้าย!
    maybeBuildSomething("fence", 26, 34)
    # โทรเรียก mayBuildSomething ด้วย "fire-trap" ที่ X บนสุด!
    maybeBuildSomething("fire-trap", 40, 50)
    # โเรียก mayBuildSomething ด้วย "fence" ที่ X ทางขวา!
    maybeBuildSomething("fence", 54, 34)
