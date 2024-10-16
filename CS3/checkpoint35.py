# ย้ายไปที่ 'Eszter' และรับค่าลับสามประการจากเธอ
hero.moveXY(24, 16)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()
secretC = hero.findNearestFriend().getSecretC()

# พูดว่า "TRUE" กับ 'Tamas' ถ้า A และ B เป็นจริง หรือถ้า C เป็นจริง มิฉะนั้น ให้พูดว่า "FALSE."
# อย่าลืมใช้วงเล็บเพื่อจัดลำดับตรรกะให้ถูกต้อง
tam = (secretA and secretB) or secretC
hero.moveXY(19, 26)
hero.say(tam)

# พูดว่า "TRUE" กับ 'Zsofi' ถ้า A หรือ B เป็นจริง และถ้า C เป็นจริง มิฉะนั้น ให้พูดว่า "FALSE."
zso = (secretA or secretB) and secretC
hero.moveXY(26, 36)
hero.say(zso)
# พูดว่า "TRUE" กับ 'Istvan' ถ้า A OR C เป็นจริง และถ้า B OR C เป็นจริง มิฉะนั้น ให้พูดว่า "FALSE."
ist = (secretA or secretC) and (secretB or secretC)
hero.moveXY(37, 34)
hero.say(ist)
# พูดว่า "TRUE" กับ 'Csilla' ถ้า A และ B เป็นจริง หรือถ้า B เป็นจริงและ C ไม่เป็นจริง มิฉะนั้น ให้พูดว่า "FALSE."
csi = (secretA and secretB) or (secretB and secretC)
hero.moveXY(40, 22)
hero.say(csi)