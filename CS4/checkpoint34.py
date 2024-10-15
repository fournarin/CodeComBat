# เก็บให้ได้ 80 ทอง
while hero.gold < 80:
    gold = hero.findNearestItem()
    hero.move(gold.pos)
# สร้างทหาร 4 นายเพื่อใช้เป็นเหยื่อล่อ
for i in range(4):
    hero.summon("soldier")
# ส่งทหารของคุณเข้าประจำตำแหน่ง
points = []
points[0] = { "x": 13, "y": 73 }
points[1] = { "x": 51, "y": 73 }
points[2] = { "x": 51, "y": 53 }
points[3] = { "x": 90, "y": 52 }
friends = hero.findFriends()

# ใช้ range เพื่อสร้างอาร์เรย์เพื่อวนซ้ำ
# จับคู่เพื่อนไปที่จุด และสั่งให้พวกเขาเคลื่อนไหว
while True:
    friends = hero.findFriends()
    for j in range(len(friends)):
        point = points[j]
        friend = friends[j]
        enemy = friend.findNearestEnemy()
        if enemy and enemy.team == "ogres" and friend.distanceTo(enemy) < 5:
            # สั่งให้เพื่อนโจมตี
            hero.command(friend, "attack", enemy)
            pass
            
        else:
            # สั่งให้เพื่อนไปยังจุดที่กำหนด
            hero.command(friend, "move", point)
            pass