# ปกป้องรงขัง
# วางทหารแต่ละคนที่ X
points = [{"x": 33, "y": 42},
          {"x": 47, "y": 42},
          {"x": 33, "y": 26},
          {"x": 47, "y": 26}]

# 1. เก็บ 80 เหรียญทอง
while hero.gold < 80:
    coin = hero.findNearestItem()
    hero.move(coin.pos)
# 2. สร้างหทาร 4 นาย
for i in range(4):
    hero.summon("soldier")
    
# 3. ส่งทหารของคุณไปประจำที่
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