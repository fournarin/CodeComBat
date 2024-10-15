while True:
    # เก็บทอง.
    gold = hero.findNearestItem()
    hero.move(gold.pos)
    # หากคุณมีทองเพียงพอ เรียกทหาร
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
    # ใช้ for-loop เพื่อสั่งการทหารแต่ละคน
    # loop มีสองส่วน: "for X in Y"
    # Y คืออาร์เรย์ที่จะ loop
    # การ loop จะทำงานหนึ่งครั้งสำหรับแต่ละไอเทมใน Y โดยที่ X ตั้งค่าเป็นไอเทมปัจจุบัน
    for friend in hero.findFriends():
        if friend.type == "soldier":
            enemy = friend.findNearestEnemy()
            # หากมีศัตรู สั่งให้เธอโจมตี
            # มิฉะนั้น ให้เคลื่อนเธอไปทางด้านขวาของแผนที่
            if enemy:
                hero.command(friend, "attack", enemy)
            else:
                # มิฉะนั้น ให้เคลื่อนเธอไปทางด้านขวาของแผนที่
                hero.command(friend, "move", {'x': friend.pos.x + 5, 'y': friend.pos.y})