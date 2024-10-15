#station26
less = "Non satis" 
more = "Nimis"      
requiredGold = 104  

def sumCoinValues(coins):
    coinIndex = 0
    totalValue = 0
    
    while coinIndex < len(coins):
        totalValue += coins[coinIndex].value
        coinIndex += 1
    return totalValue

def collectAllCoins():
    item = hero.findNearest(hero.findItems())
    while item:
        hero.moveXY(item.pos.x, item.pos.y)
        item = hero.findNearest(hero.findItems())

while True:
    items = hero.findItems()  
    goldAmount = sumCoinValues(items)  
    if goldAmount != 0:
        if goldAmount < requiredGold:
            hero.say(less)
        elif goldAmount > requiredGold:
            hero.say(more)
        elif goldAmount == requiredGold:
            collectAllCoins()