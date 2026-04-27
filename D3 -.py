print('''
                                 ____                                         
                              .-"    `-.      ,                               
                            .'          '.   /j\                              
                           /              \,/:/#\                /\           
                          ;              ,//' '/#\              //#\          
                          |             /' :   '/#\            /  /#\         
                          :         ,  /' /'    '/#\__..--""""/    /#\__      
                           \       /'\'-._:__    '/#\        ;      /#, """---
                            `-.   / ;#\']" ; """--./#J       ':____...!       
                               `-/   /#\  J  [;[;[;Y]         |      ;        
""""""---....             __.--"/    '/#\ ;   " "  |     !    |   #! |        
             ""--.. _.--""     /      ,/#\'-..____.;_,   |    |   '  |        
                   "-.        :_....___,/#} "####" | '_.-",   | #['  |        
                      '-._      |[;[;[;[;|         |.;'  /;\  |      |        
                      ,   `-.   |        :     _   .;'    /;\ |   #" |        
                      !      `._:      _  ;   ##' .;'      /;\|  _,  |        
                     .#\"""---..._    ';, |      .;{___     /;\  ]#' |__....--
          .--.      ;'/#\         \    ]! |       "| , """--./_J    /         
         /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__      
        i__..'%] _:_   ;##J         \      :"#...._!   '  "  "|__  |    `--.._
         | .--""" !|""""  |"""----...J     | '##"" `-._       |  """---.._    
     ____: |      #|      |         #|     |          "]      ;   ___...-"T,  
    /   :  :      !|      |   _______!_    |           |__..--;"""     ,;MM;  
   :____| :    .-.#|      |  /\      /#\   |          /'               ''MM;  
    |""": |   /   \|   .----+  ;      /#\  :___..--"";                  ,'MM; 
   _Y--:  |  ;     ;.-'      ;  \______/#: /         ;                  ''MM; 
  /    |  | ;_______;     ____!  |"##"""MM!         ;                    ,'MM;
 !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''MM  
  | """"--!._|     |##""         !       !         :____.....-------"""""" |'
  |          :     |______                        ___!_ "#""#""#"""#"""#"""|  
__|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |   
  "\-.      :      |#                                  :                   |  
    /#'.    |      /##,                                !                   |  
   .',/'\   |       #:#,                                ;       .==.       |  
  /"\'#"\',.|       ##;#,                               !     ,'||||',     |  
        /;/`:       ######,          ____             _ :     M||||||M     |  
       ###          /;"\.__"-._   """                   |===..M!!!!!!M_____|  
                           `--..`--.._____             _!_                    
                                          `--...____,="_.'`-.____        fsc
''')
print('''
The heavy tolling of a bell vibrates through your skull. You wake on a cold stone floor, your head spinning.
The last thing you remember was the blinding glare of headlights on a rain-slicked road.

Now, you are trapped in a decaying castle that reeks of ancient dust. 
Behind you, a massive, grotesque portrait stares with stitched-shut eyes. 
Suddenly, the far wall let out a deafening grind and begins sliding toward you, faster and faster.

The hallway is becoming a trash compactor. You sprint for your life. At the dead end, two paths emerge:''')
print("""
A. The Red Door: 
    A heavy oak door to the left. Warm, flickering light leaks through the cracks, accompanied by a faint, rhythmic humming.

B. The Corridor: A dark stone passage to the right. 
    It is choked with a freezing, unnatural mist and smells of wet earth.
      
Quick! Choose your path or death awaiting you!""")
choice1 = input("Choose A or B?\n").lower()

if choice1 == "b":
    print('You choose the brave way! You still running through the mist corridor but you find another option! '
          'There\' are 3 doors right now. Green, Yellow, and White. '
          'There are one door that lead to a infinity hole, one lead to freedom, and one lead to another challenges')
    choice2 = input("Submit your choice! Green, Yellow, or White?\n").lower()
    if choice2 == "yellow":
        print("CONGRATULATIONS! You manage to escape from the castle.")
    elif choice2 == "white":
        print("It's yet another long corridor! Good luck!")
    else:
        print("It's not a good choice! You fell into an infinity hole! Game Over!")
else:
    print('It\'s a TRAP! There is no easy escape. ' 
          'You opened the door and VOILA! A big monster appear and crushed you to the death! '
          'Game Over!')
