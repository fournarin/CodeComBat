# คุณมีเวลาเพียง 20 วินาทีก่อนที่ฝูงยักษ์จะมาถึง!
# เก็บทองให้ได้มากที่สุด แล้วถอยกลับไปที่ฐานของคุณแล้วปิดกำแพง!
while hero.time < 20:
    # เก็บเหรียญ
    hero.say("ฉันควรหยิบเหรียญนะ")
    coin = hero.findNearestItem()
    hero.move(coin.pos)
while hero.pos.x > 16:
    # ถอยไปอยู่หลังรั้ว
    hero.say("ฉันควรถอยนะ")
    hero.moveXY(15, 38)
    
# สร้างรั้วเพื่อไล่ยักษ์ออกไป
hero.buildXY("fence", 21, 40)