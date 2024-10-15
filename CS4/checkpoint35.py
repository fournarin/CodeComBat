while True:
    friends = hero.findFriends()
    # ใช้ for-loop สำหรับเพื่อนแต่ละคน
    for friend in friends:
        enemy = friend.findNearestEnemy()  # ค้นหาศัตรูที่ใกล้ที่สุดสำหรับเพื่อนแต่ละคน
        if enemy:
            hero.command(friend, "attack", enemy)  # ถ้ามีศัตรูให้โจมตี
        else:
            # หากไม่มีศัตรูให้เคลื่อนที่ไปทางทิศตะวันออก
            hero.command(friend, "move", {'x': friend.pos.x + 5, 'y': friend.pos.y})