# กำหนดฟังก์ชั่นการเคลื่อนไหวที่เรียบง่ายของคุณเอง
# กำหนด moveRight
# หมายเหตุ: แต่ละฟังก์ชั่นควรขยับฮีโร 12 เมตร!
def moveRight():
    x = hero.pos.x + 12
    y = hero.pos.y
    hero.moveXY(x, y)

# กำหนด moveUp
def moveUp():
    x = hero.pos.x
    y = hero.pos.y+12
    hero.moveXY(x, y)
# กำหนด moveDown
def moveDown():
    x = hero.pos.x 
    y = hero.pos.y-12
    hero.moveXY(x, y)
# ตอนนี้แหละ ใช้ฟังก์ชั่น
# ตอนนี้แหละ ใช้ฟังก์ชั่นพวกนั้น!
moveRight()
moveDown()
moveUp()
moveUp()
moveRight()