# ไปที่ 'Eszter' และรับหมายเลขลับจากเธอ
hero.moveXY(16, 32)
esz = hero.findNearestFriend().getSecret()

# คูณด้วย 3 และลบ 2 เพื่อรับหมายเลขของ 'Tamas'
# อย่าลืมใช้ parentheses (วงเล็บ) ในการคำนวณตามลำดับที่ถูกต้อง
# ไปที่ 'Tamas' และพูดหมายเลขวิเศษของเขา
tam = (esz * 3) - 2
hero.moveXY(24, 28)
hero.say(tam)

# ลบ 1 และคูณด้วย 4 เพื่อรับเลขของ 'Zsofi'
# ไปที่ 'Zsofi' และพูดหมายเลขวิเศษของเธอ
Zso = (tam - 1) * 4
hero.moveXY(32,24)
hero.say(Zso)
# บวกตัวเลขของ 'Tamas' และ 'Zsofi' แล้วหารด้วย 2 เพื่อรับหมายเลขของ 'Istvan'
Ista = (tam + Zso)/2
# ย้ายไปที่ 'Istvan' และพูดหมายเลขวิเศษของเขา
hero.moveXY(40, 20)
hero.say(Ista)
# บวกตัวเลขของ 'Tamas' และ 'Zsofi' ลบหมายเลขของ 'Istvan' จาก 'Zsofi' คูณผลลัพธ์ทั้งสองเพื่อรับหมายเลขของ 'Csilla'
CS = (tam + Zso)*(Zso - Ista)
# ไปที่ 'Csilla' และพูดหมายเลขวิเศษของเธอ
hero.moveXY(48, 16)
hero.say(CS)