# ใช้ตัวจัดการอีเวนท์เพื่อให้ทั้งสัตว์เลี้ยงและฮีโรวิ่ง!

def petMove():
    pet.moveXY(50, 21)

# ใช้ pet.on("spawn", petMove) แทน petMove() 
# ด้วยวิธีนี้ฮีโรและสัตว์เลี้ยงของคุณจะวิ่งไปพร้อม ๆ กัน
pet.on("spawn", petMove) # ∆ แทนที่ด้วย pet.on("spawn", petMove)
hero.moveXY(50, 12)
