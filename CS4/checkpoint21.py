# ฟิลด์นี้ถูกปกคลุมด้วยกองไฟ โชคดีที่เราได้ส่งหน่วยสอดแนมไปล่วงหน้าเพื่อค้นหาเส้นทาง เขาทิ้งเหรียญไว้ตามทาง เพื่อว่าถ้าเรายึดติดกับเหรียญที่ใกล้ที่สุด เราจะหลีกเลี่ยงกับดัก

# หุบเขานี้ดูเหมือนจะรบกวนแว่นตา findNearest ของคุณ!
# คุณจะต้องค้นหาเหรียญที่ใกล้ที่สุดด้วยตัวคุณเอง
while True:
    coins = hero.findItems()
    coinIndex = 0
    nearest = None
    nearestDistance = 9999
    
    # loop รอบเหรียญทั้งหมดเพื่อค้นหาเหรียญที่ใกล้ที่สุด
    while coinIndex < len(coins):
        coin = coins[coinIndex]
        coinIndex += 1
        distance = hero.distanceTo(coin)
        # หากระยะทางของเหรียญนี้น้อยกว่า nearestDistance
        if distance < nearestDistance:
            # ตั้ง nearest กับเหรียญ
            nearest = coin
            # ตั้งค่า nearestDistance  ถึงระยะทาง
            nearestDistance = distance
            
    # หากมีเหรียญที่ใกล้ที่สุด ให้ย้ายไปที่ตำแหน่ง คุณจะต้องใช้ moveXY เพื่อไม่ให้หักมุมและโดนกับดัก
    if nearest:
        hero.moveXY(nearest.pos.x, nearest.pos.y)