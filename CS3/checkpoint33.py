# รับค่า true/false ที่เป็นความลับสองค่าจากตัวช่วยสร้าง
# ตรวจสอบคำแนะนำสำหรับหมายเหตุเกี่ยวกับวิธีการเขียนนิพจน์เชิงตรรกะ
hero.moveXY(14, 24)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()

# ถ้าทั้ง secretA และ secretB เป็นจริง ให้เลือกเส้นทางที่สูง มิฉะนั้นให้ใช้เส้นทางที่ต่ำ
secretC = secretA and secretB
if secretC:
    hero.moveXY(20, 33)
else:
    hero.moveXY(20, 15)
hero.moveXY(26, 24)

# หากทั้ง secretA หรือ secretB เป็นจริง ให้ใช้เส้นทางที่สูง
if secretA == True or secretB == True: 
    hero.moveXY(32, 33)
hero.moveXY(38, 24)
# หาก secretB ไม่เป็นความจริง ให้ไปที่เส้นทางที่สูง
if secretB == False:
    hero.moveXY(44, 33)
else:
    hero.moveXY(44, 15)
hero.moveXY(50, 24)