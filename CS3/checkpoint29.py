# เหรียญและอัญมณีบางอันดึงดูดสายฟ้า
# ฮีโร่ควรคว้าเหรียญเงินและอัญมณีสีน้ำเงินเท่านั้น

while True:
    item = hero.findNearestItem()
    # เหรียญเงินมีค่า 2
    # รวบรวมถ้า item.type เท่ากับ "coin"
    # และ item.value เท่ากับ 2
    if item.type == "coin" and item.value == 2:
        hero.moveXY(item.pos.x, item.pos.y)
    # อัญมณีสีน้ำเงินมีค่าเท่ากับ 10
    if item.type == "gem" and item.value == 10:
    # รวบรวมถ้า item.type เท่ากับ "อัญมณี"
        hero.moveXY(item.pos.x, item.pos.y)
    # และ item.value เท่ากับ 10