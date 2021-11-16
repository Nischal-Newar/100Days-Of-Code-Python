print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print('Welcome to Treasure Hunt Game!')
print('You reached a jungle using your treasure map. Now you will have to make bunch of choices to reach the treasure!')
print('Be cautious though. If you make any wrong turn, you will die!', '\n')

# Story
status = 'alive'
print('You are at the start of a jungle. You see two paths from there. One towards left and another towards right')
choice = input('choose left or right: ')
if choice == 'left':
    print('''
        It seems you have now reached a calm river. You see a temple on the other side of the river. 
        You have three options - swim, go up towards the mountain or go down?\n
    ''')
    choice = input('Choose swim or up or down ')
    if choice == 'up':
        print('''
            After climbing at a certain height, you see no path going up any further. However there is a bridge. 
            Now you have two options - cross through the bridge or go down?\n
        ''')
        choice = input('Choose bridge or down')
        if choice == 'bridge':
            print('The bridge collapsed. You died by falling from a height in a river')
            status = 'dead'
        else:
            print('While going down towards your original location, a tiger attacked you.')
            print('You tried to run away; however, you fell down the cliff')
            status = 'dead'
    elif choice == 'down':
        print('''
            After going down you see a village, you ask for their help. They gave you a boat.
            You successfully crossed the river using the boat.
        ''')
        print('''
            Now, you are on the other side of the river. You go towards the temple. However, you found the straight path is blocked by rocks.
            You have two options: try to remove the rocks or go right\n     
        ''')
        choice = input('Choose rocks or right')
        if choice == 'rocks':
            print('''
                While trying to find a way to remove the rocks. You found a bag near it. It has a shovel, torch light and knife.
                With the help of the shovel you remove the rocks.
                The path is clear and you successfully reached the temple.
            ''')
            print('''
                Once you reached the temple, there were two options available for you. Either you could go up the stairs or go down the stairs.
            ''')
            choice = input('Choose up or down')
            if choice == 'up':
                print('''
                    As soon as you start going up the stairs, you hear some kind of sound. In a distance you see few statues came out of a door. They were holding bows.
                    The moment you try to move from the stairs they start shooting you and killing you in the action.
                ''')
                status = 'dead'
            else:
                print('''
                    You went down the stairs and found three rooms infront of you. One leading to right, one leading to left and one going straight.
                ''')
                choice = ('Choose left, right or straight')
                if choice == 'left':
                    print('''
                        You went through the left door. The door closed behind you. The room is dark. You used your torch light you found earlier.
                        As soon as you turn on the torch, you see that you are surrounded by poisonous spider.
                        You die a slow and painfully.
                    ''')
                    status = 'dead'
                elif choice == 'straight':
                    print('''
                        You went straight through the door. The door closed behind you. The room is dark. You used your torch light you found earlier.
                        As soon as you turn on the torch, you see walls closing in slowly. You try to run fast through the path. However, the path end abruptly.
                        You die painfully.
                    ''')
                    status = 'dead'
                else:
                    print('''
                        You went through the right door. The door closed behind you. The room is dark. You used your torch light you found earlier.
                        As soon as you turn on the torch, you see there is a path going straight. You walk the path for few minutes.
                        It leds you to a room. Inside that room you found the treasure.
                        Congratulations!!! YOU WON!!!
                    ''')
                    status = 'alive'
        else:
            print('''
                You went on the right side. It led you to the deeper part of the jungle.
                There a posionous snake bites you. You died on the spot.
            ''')
            status = 'dead'
    else:
        print('''
            You tried to swim across the river. However, in the middle of the river you felt something touched your legs.
            When you tried to swim litte further, an alligator came out of nowhere, bite your arm and tore it apart.
            You bleed to death.
        ''')
        status = 'dead'
else:
    print('''
        You went to the right path. After moving a little further you found a cave. You went inside the cave.
        However, the cave was full of wolves.
        They attacked you and killed you.
    ''')
    status = 'dead'

# end scene
if status == 'dead':
    print('''
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
    ''')
else: 
    print('Congratulations you found the treasure.!!')
    print('''
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
    ''')
