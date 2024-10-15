# รอยักษ์ ปราบพวกมันและรวบรวมทอง

while True:
    enemies = hero.findEnemies()
    # enemyIndex ใช้เพื่อวนซ้ำอาร์เรย์ของศัตรู
    enemyIndex = 0
    # ในขณะที่ enemyIndex น้อยกว่า  len(enemies)
    while enemyIndex < len(enemies):
        # โจมตีศัตรูที่ enemyIndex
        enemy = enemies[enemyIndex]
        hero.attack(enemy)
        # เพิ่ม enemyIndex ขึ้นหนึ่ง
        enemyIndex += 1
    coins = hero.findItems()
    # coinIndex ใช้เพื่อวนซ้ำอาร์เรย์เหรียญ
    coinIndex = 0
    while coinIndex < len(coins):
        # รับเหรียญจากอาร์เรย์เหรียญโดยใช้ coinIndex
        coin = coins[coinIndex]
        # เก็บเหรียญนั้น
        hero.moveXY(coin.pos.x, coin.pos.y)
        # เพิ่ม coinIndex ขึ้นหนึ่ง
        coinIndex += 1