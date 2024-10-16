# ปืนใหญ่ใช้เหรียญเป็นเป้าหมาย
# คุณจะเป็นเครื่องวัดระยะของปืนใหญ่

# เขียนฟังก์ชัน
def coinDistance():
    # ค้นหาเหรียญที่ใกล้ที่สุด
    item = hero.findNearestItem()
    # หากมีเหรียญ ให้คืนระยะทางให้มัน
    if item:
        return hero.distanceTo(item)
    # Else, return 0 (zero).
    else:
        return 0
    pass

while True:
    distance = coinDistance()
    if distance > 0:
        # Say the `distance`.
        hero.say(distance)
        pass