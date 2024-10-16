# ฟังพาลาดินให้ดีแล้วหาคีย์ที่ถูกต้อง

def onHear(event):
    # สัตว์เลี้ยงสามารถหาพาลาดินและกุญแจได้
    paladinUnit = pet.findNearestByType("paladin")
    goldKey = pet.findNearestByType("gold-key")
    silverKey = pet.findNearestByType("silver-key")
    bronzeKey = pet.findNearestByType("bronze-key")
    # If event.speaker เป็น paladinUnit:
    if event.speaker == paladinUnit:
        # If event.message เป็น "Gold":
        if event.message == "Gold":
            # สัตว์เลี้ยงควรจะเอากุญแจทองมาได้
            pet.fetch(goldKey)
        # If event.message เป็น "Silver":
        if event.message == "Silver":
            # สัตว์เลี้ยงควรจะเอากุญแจเงินมาได้
            pet.fetch(silverKey)
        # If event.message เป็น "Bronze":
        if event.message == "Bronze":
            # สัตว์เลี้ยงควรจะเอากุญแจทองแดงมาได้
            pet.fetch(bronzeKey)

pet.on("hear", onHear)