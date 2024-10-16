# ยักษ์ตัวใหญ่จะมองไม่เห็นคุณในป่า
# โจมตีเฉพาะยักษ์โอเกอร์ที่ตัวเล็กในป่าเท่านั้น
# เก็บเหรียญและอัญมณีเท่านั้น
# อย่าออกจากป่า และอย่ากินหรือดื่มอะไรเด็ดขาด

while True:
    # ค้นหาศัตรูที่ใกล้ที่สุด
    enemy = hero.findNearestEnemy()
    # โจมตีเฉพาะประเภท "thrower" หรือ "munchkin" 
    if enemy.type == "thrower" or enemy.type == "munchkin":
        hero.attack(enemy)
    # ค้นหาไอเทมที่ใกล้ที่สุด
    item = hero.findNearestItem()
    # จะเก็บได้ก็ต่อเมื่อประเภทของมันคือ "gem" หรือ"coin"
    if item.type == "gem" or item.type == "coin":
        hero.moveXY(item.pos.x, item.pos.y)
    pass