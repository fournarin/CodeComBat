# เก็บให้ได้ 25 ทอง แล้วบอกนาเรียทั้งหมด
# ใช้ตัวแบ่งเพื่อหยุดการสะสมเมื่อ TotalGold >= 25

totalGold = 0
while True:
    coin = hero.findNearestItem()
    if coin:
        # เก็บเหรียญ
        hero.moveXY(coin.pos.x, coin.pos.y)
        # เพิ่มมูลค่าของเหรียญเป็น TotalGold
        # รับความคุ้มค่าด้วย:  coin.value
        totalGold += coin.value
        pass
    if totalGold >= 25:
        # สิ่งนี้จะแยกออกจากลูปเพื่อเรียกใช้โค้ดที่ด้านล่าง
        # เมื่อ loop สิ้นสุดลง โค้ดหลัง loop จะทำงาน
        break

# เก็บทองเสร็จแล้ว!
hero.moveXY(58, 33)
# ไปที่นาเรียแล้วบอกว่าคุณเก็บทองได้เท่าไหร่
hero.say(totalGold)