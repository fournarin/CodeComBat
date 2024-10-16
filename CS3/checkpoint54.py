# เอาชนะโครงกระดูกและเปิดหีบสมบัติให้ได้

def onSpawn (event):
    # สัตว์เลี้ยงควรหาโพชั่นเพิ่มพลังชีวิต (ประเภทคือ "potion"):
    potion = pet.findNearestByType("potion")
    # และคาบมัน
    pet.fetch(potion)
    # สัตว์เลี้ยงควรหากุญแจทอง (ประเภทคือ "gold-key"):
    key = pet.findNearestByType("gold-key")
    # และคาบมัน
    pet.fetch(key)
    pass

# สัตว์เลี้ยงสามารถหาได้มากกว่าไอเทมเท่านั้น
skeleton = pet.findNearestByType("skeleton")
pet.on("spawn", onSpawn)

while True:
    if skeleton.health > 0:
        hero.attack(skeleton)
    else:
        hero.moveXY(31, 38)