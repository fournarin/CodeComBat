# ตระเวนและวางกับดักหากคุณเห็นเหรียญเท่านั้น

# เขียนฟังก์ชันนี้
def maybeBuildTrap(x, y):
    # ย้ายไปยังตำแหน่ง x,y ที่กำหนด
    hero.moveXY(x, y)
    # ค้นหาเหรียญและถ้าคุณเห็นมันสร้าง "fire-trap"
    coin = hero.findNearestItem()
    if coin:
        hero.buildXY("fire-trap", x, y)
    pass

while True:
    # เรียก mayBuildTrap สำหรับข้อความด้านบนซ้าย
    maybeBuildTrap(12, 56)
    # ตอนนี้สำหรับทางขวาบน
    maybeBuildTrap(68, 56)
    # ตอนนี้สำหรับทางเดินด้านล่างขวา
    hero.moveXY(70, 22)
    maybeBuildTrap(68, 12)
    # ตอนนี้สำหรับทางเดินซ้ายล่าง
    maybeBuildTrap(12, 12)
