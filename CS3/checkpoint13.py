# โจมตีมันชกินส์ เรียกนักทะเลาะวิวาทและเพิกเฉยต่อเบิร์ล

# ฟังก์ชันนี้กำหนดพฤติกรรมของฮีโร่เกี่ยวกับศัตรู
def dealEnemy(enemy):
    # หากศัตรูประเภทเป็น "munchkin":
    if enemy.type == "munchkin":
        # จากนั้นโจมตี:
        hero.attack(enemy)
    # หากประเภทของศัตรูคือ "brawler":
    if enemy.type == "brawler":
        # แล้วพูดอะไรบางอย่างเพื่อทะเลาะวิวาท:
        hero.say("ไอเต่า")
    pass

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        dealEnemy(enemy)
    else:
        hero.moveXY(30, 34)