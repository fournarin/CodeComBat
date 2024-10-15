# ล่อยักษ์ไปที่กบดักด้วยตัวล่อ

# ฟังก์ชั่นนี้มีให้ฮีโร่เก็บทองจนกว่าจะมี enoughGold.
def collectUntil(enoughGold):
    # ในขณะที่ hero.gold น้อยกว่า enoughGold
    while hero.gold < enoughGold :
        # ค้นหาเหรียญและเก็บมัน
        item = hero.findNearestItem()
        if item:
            hero.moveXY(item.pos.x, item.pos.y)
    pass

# รวบรวม 25 ทองสำหรับหนึ่งตัวล่อ และสร้างบนเครื่องหมายสีแดง
collectUntil(25)
hero.buildXY("decoy", 40, 52)
# ซ่อนน่าจะดีกว่านะ
hero.moveXY(20, 52)
# ใช้ฟังก์ชัน collectUntil เพื่อรวบรวม 50 ทอง
collectUntil(50)
# สร้าง "decoy" บนเครื่องหมายที่เป็นกระดูก:
hero.buildXY("decoy", 68, 22)
# สร้าง "decoy" บนเครื่องหมายที่เป็นไม้
hero.buildXY("decoy", 30, 20)