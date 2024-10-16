# เรากำลังทดสอบสนามใน ยูนิตตัวล่อต่อสู้ใหม่
# สร้างตัวล่อ 4 ตัว แล้วรีพอร์ททั้งหมดให้ Naria

decoysBuilt = 0
while True:
    coin = hero.findNearestItem()
    
    if coin:
        # เก็บเหรียฐแล้ว!
        hero.moveXY(coin.pos.x, coin.pos.y)
        pass
    # ตัวล่อแต่ละตัวมีราคา 25 ทอง
    # หาก hero.gold มากกว่าหรือเท่ากับ 25:
    if hero.gold >= 25:
        # buildXY a "decoy"
        hero.buildXY("decoy", hero.pos.x, hero.pos.y)
        # เพิ่มอีก 1 เพื่อสร้างจำนวน decoysBuilt
        decoysBuilt += 1
    if decoysBuilt == 4:
        # Break ออกจาก loop เมื่อคุณสร้าง 4 ตัว
        break
        pass
    
hero.say("สร้างล่อเสร็จแล้ว!")
hero.moveXY(14, 36)
# พูด ว่าคุณสร้างตัวล่อกี่ตัวแล้ว
hero.say("4")