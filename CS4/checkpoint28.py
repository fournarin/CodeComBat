# ใช้ออบเจ็กต์เพื่อเดินบนเส้นทางที่ปลอดภัยและรวบรวมอัญมณี
# คุณไม่สามารถใช้ moveXY() ในระดับนี้! ใช้ move() เพื่อไปรอบๆ
gems = hero.findItems()

while hero.pos.x < 20:
	# move() รับวัตถุที่มีคุณสมบัติ x และ y ไม่ใช่แค่ตัวเลข
	hero.move({'x': 20, 'y': 35})

while hero.pos.x < 25:
	# ตำแหน่งของอัญมณีเป็นวัตถุที่มีคุณสมบัติ x และ y
	gem0 = gems[0]
	hero.move(gem0.pos)

# ในขณะที่ x ของคุณน้อยกว่า 30
# ใช้ออบเจ็กต์เพื่อย้ายไปที่ 30, 35
while hero.pos.x < 30:
    hero.move({'x': 30, 'y': 35})
# ในขณะที่ x ของคุณน้อยกว่า 35
# ย้ายตำแหน่งอัญมณี[1].
while hero.pos.x < 35:
    gem1 = gems[1]
    hero.move(gem1.pos)
# รับอัญมณีคู่สุดท้ายด้วยตัวคุณเอง!
while hero.pos.x < 40:
    hero.move({'x': 40, 'y': 35})

while hero.pos.x < 45: 
    gem2 = gems[2]
    hero.move(gem2.pos)

while hero.pos.x < 50:
    hero.move({'x': 50, 'y': 35})

while hero.pos.x < 55: 
    gem3 = gems[3]
    hero.move(gem3.pos)