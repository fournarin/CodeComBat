# กำจัดฮีโร่ศัตรูภายในสองนาที

summonOrder = ["soldier", "soldier"]
summonCount = 0

while True:
    enemies = hero.findEnemies()
    nearestEnemy = hero.findNearest(enemies)
    
    # ฮีโร่ของเธอสามารถเก็บเงินและเรียกหน่วยทหารได้
    summonType = summonOrder[summonCount % summonOrder.length]
    if hero.gold > hero.costOf(summonType):
        hero.summon(summonType)
        summonCount += 1
    
    # เขายังสั่งการพันธมิตรของคุณในสนามรบ
    friends = hero.findFriends()
    for friend in friends:
        hero.command(friend, "attack", friend.findNearest(enemies))
    
    # เก็บเหรียญ โจมตีศัตรู หรือทั้งสองอย่าง!
    item = hero.findNearestItem()
    hero.move(item.pos)