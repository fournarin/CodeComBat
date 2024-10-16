# ย้ายไปทางขวา

# ทำฟังก์ชั่นนี้ให้สมบูรณ์:
def onSpawn(event):
    pass
    # ภายใน while-true while True:
    while True:
        # ใช้ hero.findNearestItem()
        item = hero.findNearestItem()
        # หากมีไอเทม:
        if item:
            # ใช้ pet.fetch(item) เพื่อคาบไอเท็ม
            pet.fetch(item)

# ใช้ pet.on() เพื่อกำหนด onSpawn ให้กับเหตุการณ์ "spawn"
pet.on("spawn", onSpawn)
hero.moveXY(78, 35)
