# สนามเหรียญถูกโปรยด้วยยาพิษร้ายแรง
# ยักษ์โอเกอร์กำลังโจมตี ในขณะที่บ่าวของพวกมันกำลังพยายามขโมยเหรียญของคุณ!

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # โจมตีศัตรูก็ต่อเมื่อ type (ประเภท) ไม่เท่ากับ "peon"
        if enemy.type != "peon":
            hero.attack(enemy)
    item = hero.findNearestItem()
    if item:
        # รวบรวมไอเทมเฉพาะในกรณีที่ type (ประเภท) ไม่เท่ากับ "poison"
        if item.type != "poison":
            hero.moveXY(item.pos.x, item.pos.y)
        pass