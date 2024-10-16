# ไปที่โอเอซิสโดยเลื่อนลงครั้งละ 10 เมตร
# สร้างรั้วทางด้านซ้ายของยักษ์แต่ละตัว 20 เมตร
x=hero.pos.x
y=hero.pos.y
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # buildXY เป็น "fence" 20 เมตร ไปทางซ้ายของศัตรู
        hero.buildXY("fence", enemy.pos.x - 20, enemy.pos.y)
        pass
    else:
        # moveXY ลง 10 เมตร
        y=y-10
        hero.moveXY(x, y)
        pass
