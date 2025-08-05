letter = ''' Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", "Dipak").replace("<|Date|>", "1st January 2026"))
