class Player:
    count = 0
    def __init__(self,name,level):
        self.name = name
        self.level = level
        Player.count += 1
    
p1 = Player("Ritik","Begginer")
print(Player.count)
p2 = Player("Prakash","Advanced")
p3 = Player("Lakshay","Noob")
print(p3.count)