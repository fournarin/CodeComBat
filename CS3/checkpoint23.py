# Wonderglade เปลี่ยนไปตั้งแต่ครั้งล่าสุดที่เรามา
# ยักษ์โอเกอร์สาปแช่งมันและเราควรเอาชนะพวกมัน
# เบิร์ลยังคงเก็บอัญมณีอยู่ ดังนั้นอย่าแตะต้องพวกมัน
# อย่าโจมตีเบิร์ลด้วย

while True:
    # ค้นหาไอเท็มที่ใกล้ที่สด
    item = hero.findNearestItem()
    # รวบรวม (ถ้ามี) เฉพาะในกรณีที่ประเภทไม่ใช่ "gem"
    if item:
        if item.type !="gem":
            hero.moveXY(item.pos.x, item.pos.y)
    # ค้นหาศัตรูที่ใกล้ที่สุด
    
    enemy = hero.findNearestEnemy()
    # โจมตีหากมีอยู่และประเภทไม่ใช่ "burl"
    if enemy:
        if enemy.type != "burl":
            hero.attack(enemy)
    pass