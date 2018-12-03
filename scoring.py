scoring = {
    'a' = 8,
    'b' = 1,
    'c' = 3,
    'd' = 4,
    'e' = 13,
    'f' = 2,
    'g' = 2,
    'h' = 6,
    'i' = 7,
    'j' = 0,
    'k' = 4,
    'l' = 4,
    'm' = 2,
    'n' = 7,
    'o' = 8,
    'p' = 2,
    'q' = 0,
    'r' = 6,
    's' = 6,
    't' = 9,
    'u' = 3,
    'v' = 1,
    'w' = 5,
    'x' = 0,
    'y' = 4,
    'z' = 0,
}

def scoreString(user_string):
     user_string.lower()
     total = 0
     for char in user_string:
         if char in scoring:
             total += scoring[char]
     return total
