doubleUs x y = x*2 + y*2
doubleMe x = x*2
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]
