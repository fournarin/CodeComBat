while True:
    coins = hero.findItems()
    coinIndex = 0
    
    
    while coinIndex < len(coins):
        coin = coins[coinIndex]
        
        if coin.value == 3:
            
            hero.moveXY(coin.pos.x, coin.pos.y)
        
        coinIndex += 1