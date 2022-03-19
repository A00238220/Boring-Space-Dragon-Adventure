#Brief introduction about game and how to navigate.
print("\nWelcome to Boring Space Dragon Adventure!\nImagine finding love in a party out of space, amazing right!?\nI'm the author of this game, my name is 47 and I'll be your guide to either find love or not\nYou'll be able to navigate rooms and win points in this game based on the decisions you make.\nEnough talk for now, let's get the fun started already.")
print("\nRules: The rules are simple and straightforward\nlove found = win game!\nlove not found = lose game")

while True:
  name = input("\nplease input your username to begin: ")

  print(f"\n47: Hello, {name.title()}!, you'll make your first party-decision by selecting out of two (2) room options\nRoom[a]: play party games\nRoom[b]: make a new acquaintance")

  decision1 = input(f"\n47: please select your party room of interest by inputting either 'a' or 'b': ")
  if decision1 == 'a':
    print(f"\n\n47:yay! you just earned 50 party game tokens. Room D unlocked!")

    print(f"\n\n47: you made it! welcome to the party game room!")

    print(f"\n47: please select an option to proceed by inputting either 1 or 2\n\noption[1]: I'm having fun, I'd like to continue playing party games\noption[2]: I'm tired, I'd like to proceed to Room B to make a new acquaintance")

    sub_decision2 = input(f"\n47: please enter your decision: ")
    sub_decision22 = int(sub_decision2)
    if sub_decision22 == 1:
      print(f"\n47: You lose! Love not found!\nGame over!!")
      break
    elif sub_decision22 == 2:
      print(f"\n47: yay! you just made a new friend named Saraphina. Room C unlocked!")

      print(f"\n\n47: Hi there! Glad you made it! welcome to the curiosity/attraction room!")

      print(f"\n47: please select an option to proceed by inputting either 1 or 2\n\noption[1]: I'm feeling Saraphina's vibe, I'd like to proceed on a date\noption[2]: I would rather just make-out with Saraphina")

      sub_decision5 = input(f"\n47: please enter your decision: ")
      sub_decision55 = int(sub_decision5)
      if sub_decision55 == 1:
        print(f"\n47: Nice going! you just earned $100 to take Saraphina out on a date. Room F unlocked!")

        print(f"\n\n47: Good choice! Glad you made it! welcome to the dating room!")

        print(f"\n47: please select an option to proceed by inputting either 1 or 2\n\noption[1]: The date with Saraphina was lovely, I see us going the distance\noption[2]: I don't think we are compatible, I'd rather we stayed as friends")

        sub_decision4 = input(f"\n47: please enter your decision: ")
        sub_decision44 = int(sub_decision4)
        if sub_decision44 == 1:
          print(f"\n47: Congratulations! Love found!\nYou winn!!")
          break
        elif sub_decision44 == 2:
          print(f"\n47: You lose! Love not found!\nGame over!!")
        else:
          print("incorrect input. please try again")
          continue
      elif sub_decision55 == 2:

        print(f"\n47: Smooth! Saraphina consented to your request. Room E unlocked!")

        print(f"\n\n47: Hello there! Happy you made it! welcome to the make-out room!")

        print(f"\n47: please select an option to proceed by inputting either 1 or 2\n\noption[1]: I'd like to keep things between me and Saraphina casual.\noption[2]: I think I see a connection, I would like to take Saraphina out on a date")

        sub_decision3 = input(f"\n47: please enter your decision: ")
        sub_decision33 = int(sub_decision3)
        if sub_decision33 == 1:
          print(f"\n47: You lose! Love not found!\nGame over!!")
          break
        elif sub_decision33 == 2:

          print(f"\n47: Nice going! you just earned $100 to take Saraphina out on a date. Room F unlocked!")

          print(f"\n\n47: Good choice! Glad you made it! welcome to the dating room!")

          print(f"\n47: please select an option to proceed by inputting either 1 or 2\n\noption[1]: The date with Saraphina was lovely, I see us going the distance\noption[2]: I don't think we are compatible, I'd rather we stayed as friends")

          sub_decision4 = input(f"\n47: please enter your decision: ")
          sub_decision44 = int(sub_decision4)
          if sub_decision44 == 1:
            print(f"\n47: Congratulations! Love found!\nYou winn!!")
            break
          elif sub_decision44 == 2:
            print(f"\n47: You lose! Love not found!\nGame over!!")
          else:
            print("incorrect input. please try again")
            continue
      else:
        break  
    else:
      break
  elif decision1 == 'b':
    print(f"\n\n47: yay! you just made a new friend named Saraphina. Room C unlocked!")

    print(f"\n\n47: Hi there! Glad you made it! welcome to the curiosity/attraction room!")

    print(f"\n47: please select an option to proceed by inputting either 1 or 2\n\noption[1]: I'm feeling Saraphina's vibe, I'd like to proceed on a date\noption[2]: I would rather just make-out with Saraphina")

    sub_decision1 = input(f"\n47: please enter your decision: ")
    sub_decision11 = int(sub_decision1)
    if sub_decision11 == 1:
      print(f"\n47: Nice going! you just earned $100 to take Saraphina out on a date. Room F unlocked!")

      print(f"\n\n47: Good choice! Glad you made it! welcome to the dating room!")

      print(f"\n47: please select an option to proceed by inputting either 1 or 2\n\noption[1]: The date with Saraphina was lovely, I see us going the distance\noption[2]: I don't think we are compatible, I'd rather we stayed as friends")

      sub_decision4 = input(f"\n47: please enter your decision: ")
      sub_decision44 = int(sub_decision4)
      if sub_decision44 == 1:
        print(f"\n47: Congratulations! Love found!\nYou winn!!")
        break
      elif sub_decision44 == 2:
        print(f"\n47: You lose! Love not found!\nGame over!!")
        break
      else:
        print("incorrect input. please try again")
        continue

    elif sub_decision11 == 2:

      print(f"\n47: Smooth! Saraphina consented to your request. Room E unlocked!")

      print(f"\n\n47: Hello there! Happy you made it! welcome to the make-out room!")

      print(f"\n47: please select an option to proceed by inputting either 1 or 2\n\noption[1]: I'd like to keep things between me and Saraphina casual.\noption[2]: I think I see a connection, I would like to take Saraphina out on a date")

      sub_decision3 = input(f"\n47: please enter your decision: ")
      sub_decision33 = int(sub_decision3)
      if sub_decision33 == 1:
        print(f"\n47: You lose! Love not found!\nGame over!!")
        break
      elif sub_decision33 == 2:
        print(f"\n47: Nice going! you just earned $100 to take Saraphina out on a date. Room F unlocked!")

        print(f"\n\n47: Good choice! Glad you made it! welcome to the dating room!")

        print(f"\n47: please select an option to proceed by inputting either 1 or 2\n\noption[1]: The date with Saraphina was lovely, I see us going the distance\noption[2]: I don't think we are compatible, I'd rather we stayed as friends")

        sub_decision4 = input(f"\n47: please enter your decision: ")
        sub_decision44 = int(sub_decision4)
        if sub_decision44 == 1:
          print(f"\n47: Congratulations! Love found!\nYou winn!!")
          break
        elif sub_decision44 == 2:
          print(f"\n47: You lose! Love not found!\nGame over!!")
        else:
          print("incorrect input. please try again")
          continue
      else:
        break    
    else:
      break      
  else:
    break
