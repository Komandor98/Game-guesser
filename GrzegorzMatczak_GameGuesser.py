#importing stuff
from random import randint
import random


#List of games
gamer_kokos = ['Fortnite', 'Roblox', 'Minecraft', 'CS GO', 'Among Us', 'Team Fortress 2', 'Transport Fever 2', 'Slime Rancher', 'Slime Rancher 2', 'Calculator PRO', 'Calculator', 'Pinball', 'Saper', 'This Game', 'Plants vs Zombies 2', 'Plants vs Zombies', 'GeoGuesser', 'Sleeping Simulator', 'PC Building Simulator 2', 'PC Building Simulator',"The Last of Us Part II","Hades","Ghost of Tsushima","Ori and the Will of the Wisps","Half-Life: Alyx","Cyberpunk 2077","Animal Crossing: New Horizons","Doom Eternal","Final Fantasy VII Remake","Spiritfarer","Tony Hawk's Pro Skater 1 + 2","Resident Evil 3","The Legend of Zelda: Breath of the Wild","Demon's Souls","Kentucky Route Zero: TV Edition","Dreams","Fall Guys: Ultimate Knockout","Metro Exodus","Ori and the Blind Forest","Final Fantasy IX","The Witcher 3: Wild Hunt","Minecraft","Mafia: Definitive Edition","Tetris Effect: Connected","Among Us","Assassin's Creed Valhalla","Wolfenstein: Youngblood","Ori and the Blind Forest: Definitive Edition","Final Fantasy VIII Remastered","The Elder Scrolls V: Skyrim","Super Mario Odyssey","Doom","The Last of Us","The Evil Within 2","Far Cry 5","Borderlands 3","Monster Hunter: World","Ori and the Blind Forest: Definitive Edition","Fortnite","Stardew Valley","Gears 5","Sekiro: Shadows Die Twice","Rayman Legends","The Evil Within","Minecraft Dungeons","Super Mario Maker 2","Cuphead","The Legend of Zelda: Link's Awakening","Fire Emblem: Three Houses","Sekiro: Shadows Die Twice","Ori and the Blind Forest: Definitive Edition","Fortnite","Stardew Valley","Gears 5","Sekiro: Shadows Die Twice","Rayman Legends","The Evil Within","Minecraft Dungeons","Super Mario Maker 2","Cuphead","The Legend of Zelda: Link's Awakening","Fire Emblem: Three Houses","Ori and the Blind Forest: Definitive Edition","Fortnite","Stardew Valley","Gears 5","Sekiro: Shadows Die Twice","Rayman Legends","The Evil Within","Minecraft Dungeons","Super Mario Maker 2","Cuphead","The Legend of Zelda: Link's Awakening","Fire Emblem: Three Houses","Ori and the Blind Forest: Definitive Edition","Fortnite","Stardew Valley","Gears 5","Sekiro: Shadows Die Twice","Rayman Legends","The Evil Within","Minecraft Dungeons","Super Mario Maker 2","Cuphead","The Legend of Zelda: Link's Awakening","Fire Emblem: Three Houses" ]
#gamer_kokos = ['Plants vz Zombies 2', 'Transport Fever 2', 'Team Fortress 2'] #a test for a secret option :)


#randomiser
secretword = random.choice(gamer_kokos)
isGuessed = False
x = 0
tries = 3
N = 0
print("-------------------------------")

print("Try guessing the game! Good luck!")

while not(isGuessed):
    x = str(input("Guess the game: "))
    #print("-------------------------------") #it was a test
    # if tries run out
    if tries == 0:
        print("You failed to guess the game :(. The game was: " + secretword)
        break

    #if not do the guessing code
    else:
        #Player guessed the game
        if x == secretword:
            isGuessed = True
            print("you have guessed the game in " + str(3 - tries) + " tries. Good job!")
            break
        #the player typed wrong game 
        else:
            print("You guessed wrong!")
            tries-=1
            N += 1
            #hint
            hint = secretword[ 0 : N ]
            print("hint: " + str(hint))
    print("You have " + str(tries) + " tries left")
    if secretword[-1] == '2' and tries == 1:
        print("Another hint! Its a sequel :)")
    print("-------------------------------")
           
           
            #player input                   #this is a test too
    #x = int(input("Guess the number: "))