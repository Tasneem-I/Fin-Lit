# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Leon", image="leon")
define p = Character("[pname]", color="#1aa7ec")
default A = False
default B = False
default C = False
default d_1500 = False
default d_800 = False
default d_1200 = False
default d_none = False
default s_800 = False
default s_500 = False
default s_1500 = False

# The game starts here.

label start:
    "In the bustling city of Byteville, where neon lights dance along the digital skyline, our protagonist, Leon the cat, is embarking on a new chapter of his life."
    pause 0.8
    "Fresh out of university with a degree in computer science, Leon has landed a job offer as an entry-level software engineer at MeoWorks, a tech powerhouse located in a different state."
    pause 0.8
    "Excitement bubbles within Leon as he leaves the comfort of his parent's house, ready to embrace the challenges and adventures of adulthood."
    pause 0.8
    "His journey begins in a small one-bedroom rental house just a few kilometers away from his new workplace."
    pause 0.8
    "But, little does Leon know, fate has a twist in store for him. As he settles into his new life, he stumbles upon a mysterious encounter—a secret spirit, unseen by the naked eye but deeply connected to his journey."
    pause 0.8
    "This spirit, known only to the player, becomes Leon's unseen guide in the chaotic world of cathood. The goal? To help Leon navigate the complexities of adulthood, make pivotal financial decisions, and ultimately grow into a successful and well-rounded individual."
    pause 0.8
    "As the player, you are the secret spirit, shaping Leon's destiny through choices, advice, and a sprinkle of mysterious guidance. Will you guide Leon towards financial triumph, or will the challenges of adulting prove too formidable?"
    pause 0.8
    "The journey awaits, and the choices are yours to make in this thrilling visual novel—Leon's Cathood Chronicles."
    pause 0.8
    menu:
        "yes!":
            jump scene1
        "noo":
            return

label scene1:
    $ pname = renpy.input("What would you like to be called as?: ", length=45)
    #$ pc = renpy.input("Choose color -pink or blue?: ")
    #if pc.lower() == "blue":
    #    $ pcolor = "#1aa7ec"
    #else:
    #    $ pcolor = "#1aa7ec"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    "Leon stands in front of a bulletin board, scanning through apartment listings."
    pause
    "The player, the secret spirit, appears beside him."
    "Leon furrows his brows, contemplating the apartment listings"
    pause 0.3
    l "Alright, I need to make a decision. Let's break these down. Option A is close but pricier. Option B is affordable, but that commute... and Option C seems like a middle ground. What do you think?"
    p "Let's factor in your budget. How much are these places approximately, and what's your monthly salary?"
    l "My salary for this month is $3500"
    l "Option A ,This one is just a short walk from the office. No more long commutes, but it's a bit expensive . But its a quite residential area with everything available at hand. Can I afford it?"
    pause 0.6
    l "Option B, This place is much more budget-friendly, but the commute would be longer. It has a commercial street nearby though with cheaper goods. Will it be worth the savings?"
    pause 0.6
    l "Option C, This one seems balanced—affordable and not too far from work, but I still need to spend time commuting. It is also in a busy street. But is it the right compromise?"
    pause 0.6
    menu:
        "Closer to work":
            $ A = True
            jump scene2
        "Budget friendly":
            $ B = True
            jump scene2
        "Middle ground":
            $ C = True
            jump scene2


label scene2:
    #scene bg 
    "Leon stands in front of his new apartment building, key in hand. Excitement fills the air as he opens the door to his new home."
    if A:
        l "This is it! My own place, right near work. No more long commutes"
        pause 0.3
        p "A great choice! But remember, with great convenience comes greater responsibility. Let's plan your budget and prioritize your expenses."
        pause 0.3
        #scene bg
        "Leon sits at a makeshift desk with bills and a calculator"
        pause
        l "Budgeting... this is tougher than I thought. How do I make sure I have enough for everything?"
        pause 0.3
        p "Let's break it down. After paying rent, you have $2,200 left. How would you like to distribute this?"
        pause 0.5
        l "{b}Prioritize Savings and Essentials:{/b} I'll allocate $700 for essentials like insurance, utilities, and groceries, and $1,500 for savings."
        pause 0.6
        l "{b}Balanced Approach:{/b} I'll distribute my income evenly. $600 for essentials, $800 for savings, and $800 for discretionary spending."
        pause 0.6
        l "{b}Focus on Comfort and Discretionary Spending:{/b} I want my place to be comfortable. I'll allocate $500 for essentials, $500 for savings, and $1,200 for discretionary spending."
        pause 0.6
        "Your choices here will shape your financial stability. What's most important to you right now, and how can we balance your priorities with the remaining budget"
        pause 0.6
        menu:
            "Prioritize Savings and Essentials":
                $ d_none = True
                $ s_1500 = True
                jump scene3
            "Balanced Approach":
                $ d_800 = True
                $ s_800 = True
                jump scene3
            "Focus on Comfort and Discretionary Spending":
                $ d_1200 = True
                $ s_500 = True
                jump scene3
    elif B:
        l "This place might be a bit far, but it's affordable. Let's make it home."
        pause 0.3
        p "A practical choice! Now, let's plan your budget and make sure you're set for the month."
        pause 0.3
        #scene bg 
        "Leon sits at a makeshift desk with bills and a calculator."
        pause 
        l "Budgeting... this is tougher than I thought. How do I make sure I have enough for everything?"
        pause 0.3
        p "After paying rent, insurance, and other essentials, you have $2,700 left. How would you like to distribute this?"
        pause 0.6
        l "{b}Prioritize Savings and Essentials:{/b} I'll allocate $1,000 for essentials like insurance, utilities, commute and groceries, $200 for emergencies and $1,500 for savings."
        pause 0.6
        l "{b}Balanced Approach:{/b} I'll distribute my income evenly. $700 for essentials, $800 for savings, and $1200 for discretionary spending."
        pause 0.6
        l "{b}Focus on Comfort and Discretionary Spending: {/b}I want to enjoy life too. I'll allocate $700 for essentials, $500 for savings, and $1,500 for discretionary spending."
        pause 0.6
        "Your choices here will shape your financial stability. What's most important to you right now, and how can we balance your priorities with the remaining budget"
        pause 0.6
        menu:
            "Prioritize Savings and Essentials":
                $ d_none = True
                $ s_1500 = True
                jump scene3
            "Balanced Approach":
                $ d_1200 = True
                $ s_800 = True
                jump scene3
            "Focus on Comfort and Discretionary Spending":
                $ d_1500 = True
                $ s_500 = True
                jump scene3
    elif C:
        l "A balanced choice. Let's make this place feel like home without breaking the bank"
        pause 0.3
        p "A thoughtful decision! Now, let's plan your budget and ensure you're financially comfortable."
        pause 0.3
        #scene bg
        "Leon sits at a makeshift desk with bills and a calculator."
        pause
        l "Budgeting... this is tougher than I thought. How do I make sure I have enough for everything?"
        pause 0.3
        p "After paying rent, insurance, and other essentials, you have $2,300 left. How would you like to distribute this?"
        pause 0.6
        l "{b}Balanced Approach:{/b} I'll distribute my income evenly. $700 for essentials, $800 for savings, and $800 for discretionary spending."
        pause 0.6
        l "{b}Prioritize Savings and Essentials:{/b} I'll allocate $800 for essentials like insurance, utilities, and groceries, and $1,500 for savings."
        pause 0.6
        l "{b}Focus on Comfort and Discretionary Spending:{/b} I want to enjoy life too. I'll allocate $300 for essentials, $500 for savings, and $1,500 for discretionary spending."
        pause 0.6
        "Your choices here will shape your financial stability. What's most important to you right now, and how can we balance your priorities with the remaining budget"
        pause 0.6
        menu:
            "Balanced Approach":
                $ d_800 = True
                $ s_800 = True
                jump scene3
            "Prioritize Savings and Essentials":
                $ d_none = True
                $ s_1500 = True
                jump scene3
            "Focus on Comfort and Discretionary Spending":
                $ d_1500 = True
                $ s_500 = True
                jump scene3

label scene3:
    return