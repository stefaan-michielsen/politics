doubleUs x y = x*2 + y*2
doubleMe x = x*2
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]

lucky :: (Integral a) => a -> String  
lucky 7 = "LUCKY NUMBER SEVEN!"  
lucky x = "Sorry, you're out of luck, pal!"   


charName :: Char -> String  
charName 'a' = "Albert"  
charName 'b' = "Broseph"  
charName 'c' = "Cecil"  
