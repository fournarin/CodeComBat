# ดูศัตรูทั้งหมดเพื่อดูว่าอันไหนอยู่ไกลที่สุด

while True:
    farthest = None
    maxDistance = 0
    enemyIndex = 0
    enemies = hero.findEnemies()

    # ดูศัตรูทั้งหมดเพื่อดูว่าใครอยู่ไกลที่สุด
    while enemyIndex < len(enemies):
        target = enemies[enemyIndex]
        enemyIndex += 1

        # ศัตรูคนนี้อยู่ไกลเกินกว่าที่เราเคยเห็นมามะ?
        distance = hero.distanceTo(target)
        if distance > maxDistance: # นี่ไกลกว่าที่เราเคยไปมา
            maxDistance = distance # ดังนั้นมาอัพเดท `maxDistance` เป็น `distance` ที่ใหญ่สุดใหม่กันเถอะ
            farthest = target # `farthest` คือคนที่เราวางแผนจะโจมตี

    if farthest:
        # กำจัดศัตรูที่ไกลที่สุด!
        # โจมตีศัตรูต่อไปในขณะที่พลังชีวิตของมันมากกว่า 0
        while farthest.health > 0:
            hero.attack(farthest)
        pass