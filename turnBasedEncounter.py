import random

#player stats
nathan_health = 104
nathan_ac = 16
nathan_str = 2
nathan_dex = 5
nathan_con = 3
nathan_int = 0
nathan_wis = 2
nathan_cha = 4
nathan_stealth = False
nathan = 1
nathan_down = 0


litrix_health = 115
litrix_ac = 18
litrix_str = 1
litrix_dex = 4
litrix_con = 4
litrix_int = 1
litrix_wis = 1
litrix_cha = 0
litrix = 2
litrix_down = 0

albrich_health = 98
albrich_magic_bonus = 6
albrich_spell_save = 15
albrich_ac = 15
albrich_mp = 30
albrich_str = -1
albrich_dex = 2
albrich_con = 4
albrich_int = 0
albrich_wis = 0
albrich_cha = 5
albrich = 3
albrich_down = 0

prof_bonus = 3

#enemy stats
etranth_health = 300
etranth_ac = 10
etranth_str = 5
etranth_dex = 0
etranth_con = 4
etranth_int = 2
etranth_wis = 1
etranth_cha = 4
etranth_perception = 13
fire_breath_counter = 0


#inventory
inventory = {"Potion": "3", "Revive": "3", "Bomb": "3"}


#nathan turn
def nathan_turn():
    global nathan_health
    while nathan_health >= 1:
        global etranth_health
        global nathan_stealth
        global etranth_perception
        global nathan_down
        global prof_bouns
        print("Nathan's Turn")
        print("\n")
        action = int(input("Enter Action: 1. Attack 2. Inventory 3. Scan: "))
        #attack
        if action == 1:
            print("\n")
            print("Your shadowy figure lunges toward the enemy")
            print("\n")
            roll = random.randint(1, 21 + nathan_dex + prof_bonus)
                
            if roll >= etranth_ac:
                damage_roll = random.randint(1, 13)
                damage_roll_total = damage_roll + nathan_dex + prof_bonus
                
                if roll == 20:
                    crit = damage_roll * 2
                    print("You Crit!")
                    etranth_health = etranth_health - crit - nathan_dex - prof_bonus
                    pass
                    
                if nathan_stealth == True:
                    stealth_damage = 8
                    print("\n")
                    print("you did good rouge")
                    stealth_total = damage_roll_total + stealth_damage
                    print("You deal", damage_roll_total, "damage")
                    etranth_health = etranth_health - stealth_total
                    print("\n")
                
                if nathan_stealth == False:
                    etranth_health = etranth_health - damage_roll_total
                    print("You deal", damage_roll_total, "damage")
                
            else:
                print("You miss")
                
                #Nathan stealth
            print("\n")
            print("Go into stealth?")
            print("\n")
            bonus_action = int(input("1. Yes 2. No: "))
            if bonus_action == 1:
                stealth_roll = random.randint(1, 21)
                stealth_total = (stealth_roll + nathan_dex + prof_bonus)
                if stealth_total >= etranth_perception:
                    nathan_stealth = True
                    print("You are in stealh")
                    print("\n")
                    
                else:
                    nathan_stealth = False
                    print("You need better dice")
                    print("\n")

            
            if bonus_action == 2:
                print("You choose to be seen")
                nathan_stealth = False
                print("\n")
                pass
                    
               
           #Inventory
        
        if action == 2:
            for key in inventory:
                print(key)
                print(inventory[key])
                
            item_select = int(input("1. Potion 2. Revive 3. Bomb :"))
            if item_select == 1:
                print("\n")
                if inventory.get("Potion") == 0:
                    print("You are out of potions!")
                if int(inventory.get("Potion")) >= 1:
                    nathan_health = nathan_health + 10
                    print("Nathan recovers 10HP", "Nathan's Health: ", nathan_health)
                    inventory.update({"Potion": int(inventory.get("Potion")) - 1})
                        
            if item_select == 2:
                global litrix_health
                global albrich_health
                global litrix_down
                global albrich_down
                print("\n")
                if inventory.get("Revive") == 0:
                    print("You are out of revives!")
                if int(inventory.get("Revive")) >= 1:
                    revive_select = int(input("Who will be revived? 1. Litrix 2. Albrich: "))
                    if revive_select == 1:
                        if litrix_health <= 0:
                            litrix_health = 1
                            print("Litrix rises")
                            inventory.update({"Revive": int(inventory.get("Revive")) - 1})
                            litrix_down = 0
                            print("\n")
                        else:
                            print("Litrix is already up")
                            print("\n")
                    if revive_select == 2:
                        if albrich_health <= 0:
                            albrich_health = 1
                            print("Albrich rises")
                            inventory.update({"Revive": int(inventory.get("Revive")) - 1})
                            albrich_down = 0
                            print("\n")
                        else:
                            print("Albrich is already up")
                            print("\n")
            
            if item_select == 3:
                if inventory.get("Bomb") == 0:
                    print("You are out of bombs!")
                
                if int(inventory.get("Bomb")) >= 1:
                    print("You throw a bomb at your enemy")
                    bomb_damage = 20
                    etranth_health = etranth_health - 20
                    print("You deal:", bomb_damage, "damage")
                    inventory.update({"Bomb": int(inventory.get("Bomb")) - 1})
                    
                
                            
        if action == 3:
            print("You examine the enemy")
            print("\n")
            print("Enemy health is:", etranth_health)
            
        if action >= 4:
            print("Please select a vaid number")
            nathan_turn()
        if action <=0:
            print("Please select a vaid number")
            nathan_turn()
        break
    
    while nathan_health <= 0:
        print("Nathan is down!")
        nathan_down = 1
        break
        
    #Litrix turn
def litrix_turn():
    global litrix_health
    global litrix_down
    while litrix_health >= 1:
        global etranth_health
        print("\n")
        print("Litrix's Turn")
        print("\n")
        action = int(input("Enter Action: 1. Attack 2. Inventory: "))
        print("\n")
    
        #attack
        if action == 1:
            print("You slash your sword at the enemy")
            print("\n")
            roll = random.randint(1, 21 + litrix_dex + prof_bonus)
            if roll >= etranth_ac:
                damage_roll = random.randint(1, 11)
                if roll == 20:
                    damage_roll = damage_roll * 2
                    print("You Crit!")
                damage = damage_roll + litrix_dex + prof_bonus
                etranth_health = etranth_health - damage 
                print("You deal", damage, "damage")
            
            if roll <= etranth_ac:
                print("You miss")
                print("\n")
            
        #Bouns action
            print("\n")
            print("Would you like to attack again")
            print("\n")
            bonus_action = int(input("1. Yes 2. No: "))
            print("\n")
            if bonus_action == 1:
                bonus_roll = random.randint(1, 21 + litrix_dex + prof_bonus)
                
                if bonus_roll >= etranth_ac:
                    bonus_damage_roll = random.randint(1, 11)
                    damage_bonus = bonus_damage_roll + litrix_dex + prof_bonus
                    etranth_health = etranth_health - damage_bonus
                    print("You deal", damage_bonus, "damage")
                    print("\n")
                if bonus_roll == 20:
                    bonus_damage_roll = damage_bonus * 2
                    print("You Crit!")
                    print("\n")
                
                if bonus_roll <= etranth_ac:
                    print("You miss")
                    pass
            
            if bonus_action == 2:
                print("You do not attack")
    
        if action == 2:
            for key in inventory:
                print(key)
                print(inventory[key])
        
            item_select = int(input("1. Potion 2. Revive 3. Bomb :"))
            if item_select == 1:
                print("\n")
                if inventory.get("Potion") == 0:
                    print("You are out of potions!")
                if int(inventory.get("Potion")) >= 0:
                    litrix_health = litrix_health + 10
                    print("Litrix recovers 10HP", "Litrix's Health: ", litrix_health)
                    inventory.update({"Potion": int(inventory.get("Potion")) - 1})
                
        
            if item_select == 2:
                print("\n")
                global nathan_health
                global albrich_health
                global nathan_down
                global albrich_down
                if inventory.get("Revive") == 0:
                    print("You are out of revives!")
                if int(inventory.get("Revive")) >= 0:
                    revive_select = int(input("Who will be revived? 1. Nathan 2. Albrich: "))
                    if revive_select == 1:
                        if nathan_health <= 0:
                            nathan_health = 1
                            print("Nathan rises")
                            inventory.update({"Revive": int(inventory.get("Revive")) - 1})
                            nathan_down = 0
                        else:
                            print("Nathan is already up")
                            print("\n")
                        if revive_select == 2:
                            if albrich_health <= 0:
                                albrich_health = 1
                                print("Albrich rises")
                                inventory.update({"Revive": int(inventory.get("Revive")) - 1})
                                albrich_down = 0
                                print("\n")
                            else:
                                print("Albrich is already up")
                                print("\n")
            
            if item_select == 3:
                if inventory.get("Bomb") == 0:
                    print("You are out of bombs!")
                
                if int(inventory.get("Bomb")) >= 1:
                    print("You throw a bomb at your enemy")
                    bomb_damage = 20
                    etranth_health = etranth_health - 20
                    print("You deal:", bomb_damage, "damage")
                    inventory.update({"Bomb": int(inventory.get("Bomb")) - 1})
        
        if action >= 3:
            print("Please select a vaid number")
            litrix_turn()
        if action <=0:
            print("Please select a vaid number")
            litrix_turn()
        break
        
    while litrix_health <= 0:
        print("Litrix is down!")
        print("\n")
        litrix_down = 1
        break
    #albrich turn
def albrich_turn():
    global albrich_health
    global albrich_down
    while albrich_health >= 1:
        global albrich_mp
        global albrich_magic_bonus
        global etranth_health
        global etranth_dex
        print("Albrich's Turn")
        print("\n")
        action = int(input("Choose a spell 1. Eldrich Blast 2. Fireball 3. Magic missle 4. Inventory"))
        print("\n")
    
        #eldrich blast cantip
        if action == 1:
            print("You hurl a beam of energy")
            print("\n")
            roll = random.randint(1, 21 + albrich_magic_bonus)
            if roll >= etranth_ac:
                damage_roll = random.randint(1, 11)
                if roll == 20:
                    damage_roll = damage_roll * 2
                    print("You Crit!")
                damage = damage_roll + albrich_magic_bonus
                etranth_health = etranth_health - damage
                print("You deal", damage, "damage")
                print("\n")
            if roll < etranth_ac:
                print("You miss")
                print("\n")
        #MP counter
        if albrich_mp <= 0:
            print("You're out MP")
            pass
    
        #Fireball
        if albrich_mp >= 0:        
            if action == 2:
                d1 = random.randint(1, 7)
                d2 = random.randint(1, 7)
                d3 = random.randint(1, 7)
                d4 = random.randint(1, 7)
                d5 = random.randint(1, 7)
                d6 = random.randint(1, 7)
                d7 = random.randint(1, 7)
                d8 = random.randint(1, 7)
                fireball_damage_roll = (d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8)
            
                etranth_check = random.randint(1, 21 + etranth_dex)
                
                #check pass
                if etranth_check >= 15:
                    damage_total = fireball_damage_roll / 2
                    etranth_health = etranth_health - damage_total
                    print("You hit him with that dollar store fireball")
                    print("\n")
                    print("You did", damage_total, "damage")
                    print("\n")
                    albrich_mp = albrich_mp - 10
                    print("Albrich_mp:", albrich_mp)
                
                #check fail
                if etranth_check <= 15:
                    etranth_health = etranth_health - fireball_damage_roll
                    print("You form a massive ball of flame")
                    print("\n")
                    print("You did", fireball_damage_roll, "damage")
                    print("\n")
                    albrich_mp = albrich_mp - 10
                print("Albrich mp:", albrich_mp)
                print("\n")
        
            #magic missle
            if action == 3:
                missle1 = random.randint(1, 5)
                missle2 = random.randint(1, 5)
                missle3 = random.randint(1, 5)
                missle_damage_total = (missle1 + missle2 + missle3)
                print("Three etheral missles fly towards your enemy")
                print("\n")
                print("You did", missle_damage_total, "damage")
                etranth_health = etranth_health - missle_damage_total
                albrich_mp = albrich_mp - 5
                print("\n")
                print("Albrich mp:", albrich_mp)
                print("\n")
                
        
                
        
        if action == 4:
            for key in inventory:
                print(key)
                print(inventory[key])
        
            item_select = int(input("1. Potion 2. Revive 3. Bomb :"))
            if item_select == 1:
                print("\n")
                if inventory.get("Potion") == 0:
                    print("You are out of potions!")
                if int(inventory.get("Potion")) >= 1:
                    albrich_health = albrich_health + 10
                    print("Albrich recovers 10HP", "Albrich's Health: ", albrich_health)
                    inventory.update({"Potion": int(inventory.get("Potion")) - 1})
                
            if item_select == 2:
                print("\n")
                global nathan_health
                global litrix_health
                global nathan_health
                global litrix_health
                if inventory.get("Revive") == 0:
                    print("You are out of revives!")
                if int(inventory.get("Revive")) >= 1:
                    revive_select = int(input("Who will be revived? 1. Nathan 2. Litrix: "))
                    if revive_select == 1:
                        if nathan_health <= 0:
                            nathan_health = 1
                            print("Nathan rises")
                            inventory.update({"Revive": int(inventory.get("Revive")) - 1})
                            nathan_down = 0
                        else:
                            print("Nathan is already up")
                            print("\n")
                        if revive_select == 2:
                            if albrich_health <= 0:
                                albrich_health = 1
                                print("Litrix rises")
                                inventory.update({"Revive": int(inventory.get("Revive")) - 1})
                                litrix_down = 0
                                print("\n")
                            else:
                                print("Litrix is already up")
                                print("\n")
                
            if item_select == 3:
                if inventory.get("Bomb") == 0:
                    print("You are out of bombs!")
                
                if int(inventory.get("Bomb")) >= 1:
                    print("You throw a bomb at your enemy")
                    bomb_damage = 20
                    etranth_health = etranth_health - 20
                    print("You deal:", bomb_damage, "damage")
                    inventory.update({"Bomb": int(inventory.get("Bomb")) - 1})
                    
        if action >= 5:
            print("Please select a vaid number")
            albrich_turn()
        if action <=0:
            print("Please select a vaid number")
            albrich_turn()
                        
        break
    while albrich_health <= 0:
        print("Albrich is down!")
        albrich_down = 1
        
        break
def game_over():
    print("All charecters are down")
    print("Game over!")
    exit()

if nathan_down + litrix_down + albrich_down == 3:
    game_over()

                
    #etranth           
def etranth_turn():
    
    
    global nathan_dex
    global litrix_dex
    global albrich_dex
    global nathan_health
    global litrix_health
    global albrich_health
        
    #bite
    def bite():
        target_player_ac = 0
        target_player_health = 0
        target_player = random.randint(1, 3)
        
        
        if target_player == 1:
            global nathan_stealth
            global nathan_health
            if nathan_stealth == True:
                print("Nathan is in stealth")
                bite_roll_total = 0
        if nathan_stealth == False:
            global nathan_ac
            target_player_ac = nathan_ac
            target_player_health = nathan_health
        
        if target_player == 2:
            global litrix_health
            global litrix_ac
            target_player_ac = litrix_ac
            target_player_health = litrix_health
        
        if target_player == 3:
            global albrich_health
            global albrich_ac
            target_player_ac = albrich_ac
            target_player_health = albrich_health
            
        
                
        bite_roll_to_hit = random.randint(1, 21) + 10
        if bite_roll_to_hit >= target_player_ac:
            print("Etranth's Turn")
            print("The dragon lunges forward with it's massive fangs")
            bite_roll1 = random.randint(1, 11)
            bite_roll2 = random.randint(1, 11)
            bonus_fire = random.randint(1, 11)
            bite_roll_total = bite_roll1 + bite_roll2 + bonus_fire
            print("The dragon deals", bite_roll_total, "damage")
            print("\n")
        
        if bite_roll_to_hit < target_player_ac:
            pass
                    
        if target_player == 1:
            if nathan_stealth == True:
                bite_roll_total = 0
            if bite_roll_to_hit >= target_player_ac:
                nathan_health = nathan_health - bite_roll_total
                print("Nathan's health is:", nathan_health)
                print("\n")
            if bite_roll_to_hit < target_player_ac:
                print("The beast misses")
                print("\n")
        
        if target_player == 2:
            if bite_roll_to_hit >= target_player_ac:
                litrix_health = litrix_health - bite_roll_total
                print("Litrix's health is:", litrix_health)
                print("\n")
            if bite_roll_to_hit < target_player_ac:
                print("The beast misses")
                print("\n")
        if target_player == 3:
            if bite_roll_to_hit >= target_player_ac:
                albrich_health = albrich_health - bite_roll_total
                print("Albrich's health is:", albrich_health)
                print("\n")
            if bite_roll_to_hit < target_player_ac:
                print("The beast misses")
                print("\n")
            
                
                

    #claw
    def claw():
        target_player_ac = 0
        target_player_health = 0
        target_player = random.randint(1, 3)
        
        
        if target_player == 1:
            global nathan_stealth
            global nathan_health
            if nathan_stealth == True:
                print("Nathan is in stealth")
                bite_roll_total = 0
        if nathan_stealth == False:
            global nathan_ac
            target_player_ac = nathan_ac
            target_player_health = nathan_health
        
        if target_player == 2:
            global litrix_health
            global litrix_ac
            target_player_ac = litrix_ac
            target_player_health = litrix_health
        
        if target_player == 3:
            global albrich_health
            global albrich_ac
            target_player_ac = albrich_ac
            target_player_health = albrich_health
        
       
        claw_roll_to_hit = random.randint(1, 21) + 10
        print("Eranth's Turn")
        print("The dragon swipes it's masssive claws")
        if claw_roll_to_hit >= target_player_ac:
            claw_roll1 = random.randint(1, 9)
            claw_roll2 = random.randint(1, 9)
            claw_total = claw_roll1 + claw_roll2
            print("The dragon deals", claw_total, "damage")
            print("\n")
        
        
        if claw_roll_to_hit < target_player_ac:
            pass
        
        
        if target_player == 1:
            if nathan_stealth == True:
                claw_total = 0
            if claw_roll_to_hit >= target_player_ac:
                nathan_health = nathan_health - claw_total
                print("Nathan's health is:", nathan_health)
                print("\n")
            if claw_roll_to_hit < target_player_ac:
                print("The beast misses")
                print("\n")
        
        if target_player == 2:
            if claw_roll_to_hit >= target_player_ac:
                litrix_health = litrix_health - claw_total
                print("Litrix's health is:", litrix_health)
                print("\n")
             
            if claw_roll_to_hit < target_player_ac:
                print("The beast misses")
                print("\n")
        
        if target_player == 3:
            if claw_roll_to_hit >= target_player_ac:
                albrich_health = albrich_health - claw_total
                print("Albrich's health is:", albrich_health)
                print("\n")
            if claw_roll_to_hit < target_player_ac:
                print("The beast misses")
                print("\n")
        
    #fire breath
    def fire_breath():
        global fire_breath_counter
        if fire_breath_counter >= 1:
            pass
        
        #fire breath counter
        if fire_breath_counter <= 1:
                fire_breath_counter = fire_breath_counter + 1
                print("Etranth's Turn")
                print("A massive ball of flame hurls toward you")
                print("\n")
                d1 = random.randint(1, 9)
                d2 = random.randint(1, 9)
                d3 = random.randint(1, 9)
                d4 = random.randint(1, 9)
                d5 = random.randint(1, 9)
                d6 = random.randint(1, 9)
                d7 = random.randint(1, 9)
                d8 = random.randint(1, 9)
                total_fire_breath = (d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8)
                
                #nathan check
                global nathan_dex
                global nathan_health
                nathan_check = random.randint(1, 21 + nathan_dex)
                if nathan_check >= 15:
                    print("Nathan dodges the brunt of the blast")
                    nathan_fire_damage = total_fire_breath / 2
                    nathan_health = nathan_health - nathan_fire_damage
                    print("Nathan's health: ", nathan_health)
                    print("\n")
                else:
                    print("Nathan engulfs in flames", total_fire_breath, "dealt")
                    nathan_health = nathan_health - total_fire_breath
                    print("Nathan's health: ", nathan_health)
                    print("\n")
                
                #litrix check
                global litrix_dex
                global litrix_health
                litrix_check = random.randint(1, 21 + litrix_dex)
                if litrix_check >= 15:
                    print("litrix dodges the brunt of the blast")
                    litrix_fire_damage = total_fire_breath / 2
                    litrix_health = litrix_health - litrix_fire_damage
                    print("Litrix's health: ", litrix_health)
                    print("\n")
                else:
                    print("Litrix is engulfed in flames", total_fire_breath, "damage dealt")
                    litrix_health = litrix_health - total_fire_breath
                    print("Litrix's health: ", litrix_health)
                    print("\n")
                
                #albrich check
                global albrich_dex
                global albrich_health
                albrich_check = random.randint(1, 21 + albrich_dex)
                if albrich_check >= 15:
                    print("Albrich dodges the blast")
                    albrich_fire_damage = total_fire_breath / 2
                    albrich_health = albrich_health - albrich_fire_damage
                    print("Albrich's health: ", albrich_health)
                    print("\n")
                else:
                    print("Albrich is engulfed in flames", total_fire_breath, "damage dealt")
                    albrich_health = albrich_health - total_fire_breath 
                    print("Albrich's health: ", albrich_health)
                    print("\n")
        
    attack_choice = random.randint(1, 3)

    if attack_choice == 1:
        bite()
        
    if attack_choice == 2:
        claw()
        
    if attack_choice == 3:
        fire_breath()
    
    
    
    
#actual game
print("Your party enters a massive cave, exhausted from the journey here.")
print("A massive dragon stares down at you from a great peak")
print("The beast lands in front of you and roars!")
print("\n")
while etranth_health >= 0:
    if nathan_down + litrix_down + albrich_down == 3:
        game_over()
    else:
        nathan_turn()
        litrix_turn()
        albrich_turn()
        etranth_turn()
    
    if etranth_health <= 0:
        print("As the dragon dies it utters his last words")
        print("Etranth: And so I return from whence I came, ashes.")
        print("Etranth: I wonder what will rise")
        
        
