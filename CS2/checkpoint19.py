# อีกหีบในสนามให้ฮีโร่เปิด!
# โจมตีหีบเพื่อเปิดมันออก
# มันชกินส์บางตัวจะไม่อยู่เฉย ๆ ในขณะที่คุณโจมตีมัน!
# ป้องกันตัวเองเมื่อมันชกินส์เข้ามาใกล้เกินไป

while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if hero.isReady("cleave"):
        # สิ่งสำคัญอันดับแรกคือการผ่าหากพร้อม
        hero.cleave(enemy)
        pass
    elif distance < 5:
        # โจมตีมันชกินส์ที่ใกล้ที่สุดที่เข้าใกล้มาก
        hero.attack(enemy)
        pass
    else:
        # มิฉะนั้น พยายามเปิดหีบแทน
        # ใช้ชื่อหีบเพื่อโจมตี: "Chest"
        hero.attack("Chest")
        pass
    
