# อัญมณีหนึ่งปลอดภัย อัญมณีอื่นเป็นระเบิด
# แต่คุณก็รู้คำตอบ: จะเป็นข้อที่สองเสมอ

while True:
    items = hero.findItems()
    # หากความยาวของรายการมากกว่าหรือเท่ากับ 2:
    if (items.length >= 2):
        # ย้ายไปยังไอเท็มที่สองในไอเท็ม
        hero.moveXY(items[1].pos.x, items[1].pos.y)
    # Else:
    else:
        
        # ไปที่เครื่องหมายตรงกลาง
        hero.moveXY(40, 34)