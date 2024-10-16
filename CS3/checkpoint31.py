# อย่าสนใจกับยักษ์ขนาดเล็กและขนาดกลาง
# เป้าหมายของคุณคือประเภท ""brawler"
# เมื่อ "brawler" อยู่ใกล้กว่า 50 เมตร ให้ยิงปืนใหญ่ได้

while True:
    # ค้นหาศัตรูที่ใกล้ที่สุดและระยะห่างจากมัน
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    # ถ้าประเภทศัตรูคือ "brawler"
    # และระยะห่างไม่ถึง 50 เมตร
    # ให้พูดว่า "Fire!" เพื่อส่งสัญญาณปืนใหญ่
    if enemy.type == "brawler" and distance < 50 :
        hero.say("Fire!")
    pass