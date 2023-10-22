# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Leon", image="leon")
define p = Character("[pname]", color="#7e538f")
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
default reg_dec =False
default b_end = False
# The game starts here.

label start:
    scene bg bright cityy
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
    show leon smiling at left with dissolve
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

    scene bg apmt list
    show leon smiling at right
    "Leon stands in front of a bulletin board, scanning through apartment listings."
    pause
    "The player, the secret spirit, appears beside him."
    "Leon furrows his brows, contemplating the apartment listings"
    hide leon smiling
    pause 0.3
    l frowning "Alright, I need to make a decision. Let's break these down. Option A is close but pricier. Option B is affordable, but that commute... and Option C seems like a middle ground. What do you think?"
    p "Let's factor in your budget. How much are these places approximately, and what's your monthly salary?"
    l"My salary for this month is $3500"
    l"Option A ,This one is just a short walk from the office. No more long commutes, but it's a bit expensive . But its a quite residential area with everything available at hand. Can I afford it?"
    pause 0.6
    l"Option B, This place is much more budget-friendly, but the commute would be longer. It has a commercial street nearby though with cheaper goods. Will it be worth the savings?"
    pause 0.6
    l"Option C, This one seems balanced—affordable and not too far from work, but I still need to spend time commuting. It is also in a busy street. But is it the right compromise?"
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
    scene bg apmt door
    "Leon stands in front of his new apartment building, key in hand. Excitement fills the air as he opens the door to his new home."
    hide bg apmt door with dissolve
    scene bg new room
    if A:
        l"This is it! My own place, right near work. No more long commutes"
        pause 0.3
        p "A great choice! But remember, with great convenience comes greater responsibility. Let's plan your budget and prioritize your expenses."
        pause 0.3
        "Leon unpacks and sets up his furniture"
        scene bg desk
        "Leon sits at a desk with bills and a calculator"
        pause
        l"Budgeting... this is tougher than I thought. How do I make sure I have enough for everything?"
        pause 0.3
        p "Let's break it down. After paying rent, you have $2,200 left. How would you like to distribute this?"
        pause 0.5
        l"{b}Prioritize Savings and Essentials:{/b} I'll allocate $700 for essentials like insurance, utilities, and groceries, and $1,500 for savings."
        pause 0.6
        l"{b}Balanced Approach:{/b} I'll distribute my income evenly. $600 for essentials, $800 for savings, and $800 for discretionary spending."
        pause 0.6
        l"{b}Focus on Comfort and Discretionary Spending:{/b} I want my place to be comfortable. I'll allocate $500 for essentials, $500 for savings, and $1,200 for discretionary spending."
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
        l"This place might be a bit far, but it's affordable. Let's make it home."
        pause 0.3
        p "A practical choice! Now, let's plan your budget and make sure you're set for the month."
        pause 0.3
        scene bg desk
        "Leon sits at a makeshift desk with bills and a calculator."
        pause 
        l"Budgeting... this is tougher than I thought. How do I make sure I have enough for everything?"
        pause 0.3
        p "After paying rent, insurance, and other essentials, you have $2,700 left. How would you like to distribute this?"
        pause 0.6
        l"{b}Prioritize Savings and Essentials:{/b} I'll allocate $1,000 for essentials like insurance, utilities, commute and groceries, $200 for emergencies and $1,500 for savings."
        pause 0.6
        l"{b}Balanced Approach:{/b} I'll distribute my income evenly. $700 for essentials, $800 for savings, and $1200 for discretionary spending."
        pause 0.6
        l"{b}Focus on Comfort and Discretionary Spending: {/b}I want to enjoy life too. I'll allocate $700 for essentials, $500 for savings, and $1,500 for discretionary spending."
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
        l"A balanced choice. Let's make this place feel like home without breaking the bank"
        pause 0.3
        p "A thoughtful decision! Now, let's plan your budget and ensure you're financially comfortable."
        pause 0.3
        #scene bg
        "Leon sits at a makeshift desk with bills and a calculator."
        pause
        l"Budgeting... this is tougher than I thought. How do I make sure I have enough for everything?"
        pause 0.3
        p "After paying rent, insurance, and other essentials, you have $2,300 left. How would you like to distribute this?"
        pause 0.6
        l"{b}Balanced Approach:{/b} I'll distribute my income evenly. $700 for essentials, $800 for savings, and $800 for discretionary spending."
        pause 0.6
        l"{b}Prioritize Savings and Essentials:{/b} I'll allocate $800 for essentials like insurance, utilities, and groceries, and $1,500 for savings."
        pause 0.6
        l"{b}Focus on Comfort and Discretionary Spending:{/b} I want to enjoy life too. I'll allocate $300 for essentials, $500 for savings, and $1,500 for discretionary spending."
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
    scene bg comm street
    "Leon receives an invitation to a colleague's dinner party. He contemplates whether to attend or not."
    pause 0.4
    l frowning "A dinner party from work... it sounds fun, but with my budget, should I go?"
    pause 0.4
    p "Socializing is important. Let's figure out how you can attend without jeopardizing your budget."
    pause 0.4
    l"I want to be a part of the team, but I also need to be mindful of my budget. What should I do?"
    pause 0.4
    p "You can attend without overspending. How would you like to approach this?"
    pause 0.4
    if d_800 or d_1200 or d_1500:
        p "How can you strike a balance and enjoy the evening without overspending? Consider your allocated $800 budget for discretionary spending when deciding on the amount for this event."
        pause 0.6
        l frowning"{b}Attend with a Budget:{/b} I'll allocate $150 for the dinner party. Maybe eat something light before going to save on expenses."
        pause 0.6
        l"{b}Regretfully Decline: {/b}I'll skip this one to stay within my budget. I'll explain to my colleagues later. It's unfortunate, but necessary."
        pause 0.6
        l"{b}Attend Splendidly: {/b}It's a special occasion. I'll allocate $300 for the dinner party and enjoy myself. I'll figure out the budget later"
        pause 0.6
        menu:
            "Attend with a Budget":
                scene bg restaurant
                show leon suit at right with fade
                "Leon, with a spirited choice, decides to attend the social event hosted by MeoWorks."
                pause 0.3
                "The venue is aglow with soft lights, and the chatter of fellow colleagues fills the air. Leon, with a smile, engages in conversations, makes connections, and even shares a few laughs."
                pause 0.6          
                "As the event winds down, the secret spirit senses Leon's positive energy. It whispers in the unseen realm, pleased with the choice."
                pause 0.3
                jump scene4
            "Regretfully Decline":
                scene bg full room
                show leon depressed at center
                "Leon, hesitating, decides not to attend the MeoWorks social event. As the night unfolds without him, a sense of regret lingers in the air."
                l"Maybe I should have gone. Missed out on a chance to connect. Well, there's always next time, right?"
                "The secret spirit, observing silently, notes the subtle pang of remorse in Leon's voice, feeling regretful"
                $ reg_dec = True
                jump scene3_alias
            "Attend Splendidly":
                scene bg restaurant
                show leon suit at right
                "Leon, with a hesistant attitude, decides to attend the social event hosted by MeoWorks."
                pause 0.3
                "The venue is aglow with soft lights, and the chatter of fellow colleagues fills the air. Leon, with a smile, engages in conversations, makes connections, and even shares a few laughs."
                pause 0.6          
                "As the event winds down, the secret spirit senses Leon's depressed energy. It whispers in the unseen realm, regretting the choice."
                pause 0.3
                jump scene4
    else:
        jump scene3_alias        
label scene3_alias:         
    if d_none or reg_dec:
        "Leon, torn by budget concerns, since he did not allocate a discretionary budget, decides to forego the dinner party to stay within his financial limits."
        pause 0.4
        "The next day at work, he overhears excited chatter about the dinner party—discussions about potential projects and networking opportunities that he missed out on. The company announces its annual meet, another chance for crucial connections and discussions."
        pause 0.6
        "Colleagues encourage him to attend, emphasizing its importance for career growth. Leon, still constrained by his budget, faces a difficult decision."
        pause 0.6
        l frowning "{b}Attend:{/b} Leon chooses to attend the annual meet with a tight budget, compromising on potential networking opportunities."
        pause 0.6
        l "{b}Regretfully Decline Again:{/b} Leon, sticking to his financial plan, decides to skip the annual meet, sacrificing potential career advancements."
        pause 0.6
        l "{b}Attend and Overstep Budget:{/b} Desperate not to miss out, Leon allocates extra funds for the meet, even if it means jeopardizing his financial stability. "
        menu:
            "Attend":
                scene annual party
                show leon formals at center
                jump scene4
            "Regretfully Decline Again":
                scene bg office
                show leon formals at left
                "Leon overhears excited whispers in the office—the buzz of a close colleague securing a golden opportunity from the social event. Regret creeps in, gnawing at him, as he reflects on missed chances."
                pause 0.8
                l"I could have been there, made an impression. Now, I'm stuck, and opportunities slip away. If only I had budgeted better."
                pause 0.6
                l"Melancholy shadows Leon's expression as the realization of financial choices weighs heavily on his aspirations."
                pause 0.6
                $ b_end = True
                jump end
            "Attend and Overstep Budget":
                scene bg night room
                show leon depressed at right
                "In the dimly lit confines of his one-bedroom rental, Leon grapples with financial strain. The empty fridge echoes his struggle as he dials his parents, swallowing pride, to borrow a lifeline."
                pause 0.8
                l"This is tougher than I thought. A missed paycheck and now this... Maybe I'm not cut out for this adulting thing."
                pause 0.6
                l"As the weight of financial pressure bears down, a cloud of depression settles over Leon's once hopeful spirit."
                pause 0.6
                $ b_end = True
                jump end 
        

label scene4:
    scene bg bank
    show leon smiling at right
    pause
    "Leon, ready with his savings, found a pleasant day to visit the bank for creating a savings account"
    pause 0.6
    hide leon smiling
    l frowning "It's time to make my money work for me. Let's check out some savings account plans"
    pause 0.4
    p "Absolutely! Let's look for a plan that aligns with your financial goals and helps your money grow."
    pause 0.4
    scene bg front desk
    "Leon walks into a local bank to inquire about savings account plans."
    pause 0.4
    "Bank Representative" "Welcome! How can I assist you today?"
    pause 0.5
    "Guide Leon through the options and help him choose a savings plan that aligns with his financial goals and current savings"
    pause 0.4
    l frowning"{b}Tiered Savings - 2.0%% APY, Requires $1000 Minimum, 1.5 year commitment:{/b} I'm open to a bit of commitment. What's the deal with your Tiered Savings? Does it offer better returns with a higher balance?"
    pause 0.6
    l "{b}Flexible Savings - 1.2%% APY,  no commitment: {/b}I need some flexibility. Are there plans that allow withdrawals without penalties? A lower interest rate is fine if I can access my money when needed"
    pause 0.6
    l "{b}Long-Term Savings - 1.8%% APY, Requires $600 Minimum, 3-year commitment: {/b}I'm thinking long-term. Are there plans with better benefits if I commit to saving for a certain period? I'm willing to commit for three years."
    pause 0.6
    if s_800:
        menu:
            "Tiered Savings":
                scene bg night room
                show leon depressed at center
                pause 0.8
                hide leon with dissolve
                "Leon, opting for a challenging savings plan, finds himself struggling to make ends meet. Overwhelmed, he reluctantly seeks financial help from his parents, his pride wounded."
                pause 0.7
                "The weight of financial strain casts a shadow over his once optimistic spirit, leaving him in a state of deep depression."
                pause 0.6
                $ b_end= True
                jump end
            "Flexible Savings":
                scene bg comm street
                show leon smiling at right
                "Leon, content with his thoughtful financial decisions, revels in the satisfaction of achieving stability."
                "A sense of pride lights up his face, and the secret spirit silently applauds the success of wise choice"
                pause 0.5
                jump scene5
            "Long Term Savings":
                scene bg comm street
                show leon smiling at left
                "Leon, content with his thoughtful financial decisions, revels in the satisfaction of achieving stability."
                "A sense of pride lights up his face, and the secret spirit silently applauds the success of wise choice"
                pause 0.5
                jump scene5
    elif s_1500:
        menu:
            "Tiered Savings":
                scene bg comm street
                show leon smiling at center
                "Leon, content with his thoughtful financial decisions, revels in the satisfaction of achieving stability."
                "A sense of pride lights up his face, and the secret spirit silently applauds the success of wise choice"
                pause 0.5
                jump scene5
            "Flexible Savings":
                scene bg night room
                show leon depressed
                "Leon, disheartened, examines his meager savings from the simple plan. The pitifully small amount falls short of his expectations, fueling a sense of disappointment and financial frustration."
                pause 0.5
                "Leon, immersed in regret, grapples with a cloud of depression. The weight of missed opportunities and the thought of potential savings with a different plan haunt him, casting a shadow over his once hopeful demeanor."
                pause 0.6
                $ b_end = True
                jump end
            "Long Term Savings":
                scene bg comm street
                show leon smiling at right
                "Leon, content with his thoughtful financial decisions, revels in the satisfaction of achieving stability."
                "A sense of pride lights up his face, and the secret spirit silently applauds the success of wise choice"
                pause 0.5
                jump scene5
    elif s_500:
        menu:
            "Tiered Savings":
                #scene bg
                #show 
                "Leon, opting for a challenging savings plan, finds himself struggling to make ends meet. Overwhelmed, he reluctantly seeks financial help from his parents, his pride wounded."
                pause 0.7
                "The weight of financial strain casts a shadow over his once optimistic spirit, leaving him in a state of deep depression."
                pause 0.6
                $ b_end= True
                jump end
            "Flexible Savings":
                scene bg comm street
                show leon smiling at right
                "Leon, content with his thoughtful financial decisions, revels in the satisfaction of achieving stability."
                "A sense of pride lights up his face, and the secret spirit silently applauds the success of wise choice"
                pause 0.5
                jump scene5
            "Long Term Savings":
                "Leon, opting for a challenging savings plan, finds himself struggling to make ends meet. Overwhelmed, he reluctantly seeks financial help from his parents, his pride wounded."
                pause 0.7
                "The weight of financial strain casts a shadow over his once optimistic spirit, leaving him in a state of deep depression."
                pause 0.6
                $ b_end= True
                jump end

label scene5:
    scene bg busy streett
    show leon sad at right
    "Leon is facing a dilemma regarding his daily commute to work. His choices impact both his time and budget."
    hide leon sad
    l frowning "My commute is taking a toll. How can I optimize it without breaking the bank?"
    p "Balancing time and budget for your commute is crucial. Let's explore your options."
    l "{b}Public Transportation:{/b} I can take public transportation. It's cost-effective, but it might take longer. How does it align with my budget?"
    pause 0.6
    l "{b}Carpooling or Ride Sharing:{/b} Maybe carpooling or ride-sharing can help. How do these options impact both time and cost?"
    pause 0.6
    l "{b}Biking or Walking:{/b} What about biking or walking? It's healthy, but how practical is it for my daily commute?"
    pause 0.6
    menu:
        "Public Transportation":
            if C or B:
                scene bg train 
                show leon smiling at right
                "Leon, content with his commute choice, enjoys a smooth balance between time and budget. A satisfied smile graces his face as he navigates the city, appreciating the thoughtful decision that enhances both his work-life balance and financial stability."
                pause 0.7
                jump scene6
            elif A:
                scene bg train 
                show leon sad at right
                "Leon, discontented with his public transportation choice, weaves through crowded buses and bustling stations for his closeby office. Frustration etches his face as the once-easy commute turns into a daily struggle, overshadowing the satisfaction he sought."
                pause 0.7
                jump scene6
        "Carpooling or Ride Sharing":
            "Leon, content with his commute choice, enjoys a smooth balance between time and budget. A satisfied smile graces his face as he navigates the city, appreciating the thoughtful decision that enhances both his work-life balance and financial stability."
            pause 0.7
            jump scene6
        "Biking or Walking":
            if B:
                scene bg 
                show leon depressed
                "Leon, worn and haggard from the long biking or walking commute to his distant office, arrives fatigued. The extended travel time takes a toll, leaving him drained and impacting his productivity."
                pause 0.6
                "A cloud of depression settles over him as the daily grind becomes an overwhelming struggle."
                pause 0.4
                $ b_end= True
                jump end
            elif A:
                "Leon, content with his commute choice, enjoys a smooth balance between time and budget. A satisfied smile graces his face as he navigates the city, appreciating the thoughtful decision that enhances both his work-life balance and financial stability."
                pause 0.7
                jump scene6
            elif C:
                "Leon, slightly fatigued from his commute choices, sacrifices personal time for efficiency. With weariness in his steps, he opts for takeout for dinner, a small compromise in the pursuit of a smoother, albeit tiring, daily routine."
                pause 0.7
                jump scene6


label scene6:
    return


label end:
    if b_end:
        '{color=#fd1200}{b}Bad Ending{/b}{/color}'
       
        pause 0.8
        return
    else:
        return