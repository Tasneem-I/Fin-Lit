# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Leon", image="leon")
define p = Character("[pname]", color="#7e538f")
define i = Character("Insurance Agent", color="#3c3235ff")
define n = Character("Hospital Receptionist", color="#b19fff")
define a = Character("Bank Representative", color="#f4f486")

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
default flex = False
default cred = False
default emf = False
default hcover = False
default mcover = False
default lcover = False

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
    scene bg new room
    if A:
        l frowning "This is it! My own place, right near work. No more long commutes"
        pause 0.3
        p "A great choice! But remember, with great convenience comes greater responsibility. Let's plan your budget and prioritize your expenses."
        pause 0.3
        "Leon unpacks and sets up his furniture"
        scene bg desk
        "Leon sits at a desk with bills and a calculator"
        pause
        l frowning "Budgeting... this is tougher than I thought. How do I make sure I have enough for everything?"
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
        l frowning "This place might be a bit far, but it's affordable. Let's make it home."
        pause 0.3
        p "A practical choice! Now, let's plan your budget and make sure you're set for the month."
        pause 0.3
        scene bg desk
        "Leon sits at a makeshift desk with bills and a calculator."
        pause 
        l frowning "Budgeting... this is tougher than I thought. How do I make sure I have enough for everything?"
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
        l frowning "A balanced choice. Let's make this place feel like home without breaking the bank"
        pause 0.3
        p "A thoughtful decision! Now, let's plan your budget and ensure you're financially comfortable."
        pause 0.3
        scene bg desk
        "Leon sits at a makeshift desk with bills and a calculator."
        pause
        l frowning "Budgeting... this is tougher than I thought. How do I make sure I have enough for everything?"
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
                show leon suit at right
                "Leon, with a spirited choice, decides to attend the social event hosted by MeoWorks."
                pause 0.3
                "The venue is aglow with soft lights, and the chatter of fellow colleagues fills the air. Leon, with a smile, engages in conversations, makes connections, and even shares a few laughs."
                pause 0.6          
                "As the event winds down, the secret spirit senses Leon's positive energy. It whispers in the unseen realm, pleased with the choice."
                pause 0.3
                jump scene4
            "Regretfully Decline":
                scene bg night room
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
    show accountant work at right
    show leon suit at left
    a "Welcome! How can I assist you today?"
    pause 0.5
    "Guide Leon through the options and help him choose a savings plan that aligns with his financial goals and current savings"
    pause 0.4
    a "{b}Tiered Savings - 2.0%% APY, Requires $1000 Minimum, 1.5 year commitment:{/b} I'm open to a bit of commitment. What's the deal with your Tiered Savings? Does it offer better returns with a higher balance?"
    pause 0.6
    a "{b}Flexible Savings - 1.2%% APY,  no commitment: {/b}I need some flexibility. Are there plans that allow withdrawals without penalties? A lower interest rate is fine if I can access my money when needed"
    pause 0.6
    a "{b}Long-Term Savings - 1.8%% APY, Requires $600 Minimum, 3-year commitment: {/b}I'm thinking long-term. Are there plans with better benefits if I commit to saving for a certain period? I'm willing to commit for three years."
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
                $ flex = True
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
                $ flex = True
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
                scene bg bike
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
    scene bg desk
    show leon frowning at right
    "Leon receives his credit card statement with a balance. The minimum payment is calculated at 2.5%% of the outstanding balance."
    pause 0.4
    hide leon frowning
    l frowning "What's the best approach to handle my credit card payment? How does this minimum payment affect my overall debt?"
    pause 0.3
    p "Credit card math can be tricky. Let's break down the numbers."
    pause 0.3
    l "{b}Minimum Pay: {/b}I'll pay only the minimum this month to free up some cash. It shouldn't be a big deal, right?"
    pause 0.6
    l "{b}More than Minimum: {/b}I'll pay more than the minimum to chip away at the balance faster. How much extra should I pay to make a significant impact?"
    pause 0.6
    l "{b}Change Card Plan: {/b}Maybe I can transfer the balance to a lower-interest card. How much will that save me in the long run?"
    pause 0.6
    menu:
        "Minimum Pay":
            show bg comm street
            l depressed "I should have paid my interests at time, now its spiraling more."
            pause 0.3
            "The spirit watches over leon worriedly, regretting its suggestion at that time."
            $ b_end = True
            jump end
        "More than Minimum":
            show bg busy streett
            l smiling "I'm so happy that I paid them properly!"
            pause 0.2
            jump scene7
        "Change Card Plan":
            if d_none:
                scene phone shop
                "Leon, seeking financial prudence, switches to a lower-interest credit card. However, as the need for a new phone arises, the realization hits hard—"
                pause 0.1
                "he's limited by his financial choices. A cloud of regret and depression looms over him as the desire for a necessary upgrade clashes with the constraints of his current situation"
                pause 0.2
                $ cred = True
                jump scene7
            else:
                scene bg busy streett
                l smiling "I'm so happy that I changed my card plan. I have enough allocated for extra charges, this makes life so easier!"
                pause 0.2
                jump scene7

label scene7:
    scene bg desk
    "Leon is evaluating his financial goals and considers setting a target for his emergency fund using his discretionary savings. He's uncertain about the right amount and how it aligns with his lifestyle and expenses."
    pause 0.2
    l frowning "I know having an emergency fund is important, but how much should I aim to save from my discretionary savings? What factors should I consider?"
    if d_1500:
        p "Setting an emergency fund target is a smart move. Let's break it down. Your monthly discretionary savings are $1,500. How much of it is essential?"
        pause 0.2
        l frowning "Well, I need to keep some for social events maybe around $50-100, and also save up some for furnishing our home"
        pause 0.2
        p "Great, consider how many months' worth of essential expenses you'd like to have in your emergency fund. A common recommendation is three to six months"
        pause 0.2
        l "Considering my job stability and the industry, aiming for a four-month emergency fund should be reasonable. That would be around $8,600."
        pause 0.3
        l "{b}Aggresive Saving: {/b}I'll cut down on discretionary spending and all of my $1,500 towards my emergency fund. It might mean sacrificing some extras, but it's worth the security."
        pause 0.6
        l "{b}Gradual Build-Up: {/b}I'll aim for the four-month target but gradually build it up over the next six months by allocating $400 initially and increase upto $700. This way, I can still enjoy some of the things I like without drastic lifestyle changes."
        pause 0.6
        l "{b}Split Debt: {/b}I have some debts to pay off. I'll allocate a portion of my discretionary savings, maybe around $800 to clear debts and the rest towards building up my emergency fund. How does that sound?"
        pause 0.6
        menu:
            "Aggresive Saving":
                scene bg busy streett
                show leon formals at right
                if cred:
                    l "I'm so happy to finally build up my emergency fund. It really takes a lot of weight off my shoulders that I didn't even realize I carried. Thank you!"
                    pause 0.2
                    hide leon formals
                    "The spirit is very pleased to see Leon jumping with joy"
                    $ emf = True
                    jump scene8
                else:
                    l "Ughh, I only have enough to spend for my bare essentials, my lifestyle keeps detoriating"
                    pause 0.2
                    "Frustrated and angry about his lost lifestyle, Leon becomes temperamental"
                    pause 0.1
                    "The spirit tries to comfort Leon but ultimately stops, hesistating and driven with guilt"
                    $ b_end = True
                    jump end
            "Gradual Build-Up":
                if cred:
                    scene bg night room
                    "Leon's choice of credit plan limits his financial options and in the end, he never gets to grow his emergency fund"
                    pause 0.2
                    "Frustrated and regretting his choices, Leon loses confidence in himself"
                    pause 0.3
                    "The spirit watches worriedly and guiltily as Leon becomes more indecisive"
                    $ b_end = True
                    jump end
                else:
                    scene bg busy streett
                    show leon formals at right
                    l "I'm so happy to finally build up my emergency fund. It really takes a lot of weight off my shoulders that I didn't even realize I carried. Thank you!"
                    pause 0.2
                    hide leon formals
                    "The spirit is very pleased to see Leon jumping with joy"
                    $ emf = True
                    jump scene8
            "Split Debt":
                if cred:
                    scene bg busy streett
                    show leon formals at right
                    l "I'm so happy to finally build up my emergency fund. It really takes a lot of weight off my shoulders that I didn't even realize I carried. Thank you!"
                    pause 0.2
                    hide leon formals
                    "The spirit is very pleased to see Leon jumping with joy"
                    $ emf = True
                    jump scene8
                if not cred:
                    scene bg night room
                    "Leon has not built up even half his emergency fund when rumours of recession started going around."
                    pause 0.2
                    "Frustrated about his wrong choice, Leon becomes anxious about the future"
                    pause 0.3
                    "The spirit watches worriedly and guiltily as Leon's anxiety grows"
                    $ b_end = True
                    jump end
    elif d_1200:
        p "Setting an emergency fund target is a smart move. Let's break it down. Your monthly discretionary savings are $1,500. How much of it is essential?"
        pause 0.1
        "{b}Aggressive Saving: {/b}I'll cut down on discretionary spending and allocate the majority of my $1,000 towards my emergency fund. It might mean sacrificing some extras, but it's worth the security."
        pause 0.6
        "{b}Gradual Build-Up: {/b}I'll aim for the four-month target but gradually build it up over the next six months from $200 to $600. This way, I can still enjoy some of the things I like without drastic lifestyle changes."
        pause 0.6
        "{b}Split Debt{/b} :I have some debts to pay off. I'll allocate a portion of my discretionary savings to clear debts  for $800 and the rest of $400 towards building up my emergency fund. How does that sound?"
        pause 0.6
        menu:
            "Aggresive Saving":
                scene bg busy streett
                show leon formals at right
                if cred:
                    l "I'm so happy to finally build up my emergency fund. It really takes a lot of weight off my shoulders that I didn't even realize I carried. Thank you!"
                    pause 0.2
                    hide leon formals
                    "The spirit is very pleased to see Leon jumping with joy"
                    $ emf = True
                    jump scene8
                else:
                    scene bg night room
                    show leon depressed
                    l "Ughh, I only have enough to spend for my bare essentials, my lifestyle keeps detoriating"
                    pause 0.2
                    "Frustrated and angry about his lost lifestyle, Leon becomes temperamental"
                    pause 0.1
                    "The spirit tries to comfort Leon but ultimately stops, hesistating and driven with guilt"
                    $ b_end = True
                    jump end
            "Gradual Build-Up":
                if cred:
                    scene bg night room
                    show leon depressed
                    "Leon's choice of credit plan limits his financial options and in the end, he never gets to grow his emergency fund"
                    pause 0.2
                    "Frustrated and regretting his choices, Leon loses confidence in himself"
                    pause 0.3
                    "The spirit watches worriedly and guiltily as Leon becomes more indecisive"
                    $ b_end = True
                    jump end
                else:
                    scene bg busy streett
                    show leon formals at right
                    l "I'm so happy to finally build up my emergency fund. It really takes a lot of weight off my shoulders that I didn't even realize I carried. Thank you!"
                    pause 0.2
                    hide leon formals
                    "The spirit is very pleased to see Leon jumping with joy"
                    $ emf = True
                    jump scene8
            "Split Debt":
                if cred:
                    scene bg busy streett
                    show leon formals at right
                    l "I'm so happy to finally build up my emergency fund. It really takes a lot of weight off my shoulders that I didn't even realize I carried. Thank you!"
                    pause 0.2
                    hide leon formals
                    "The spirit is very pleased to see Leon jumping with joy"
                    $ emf = True
                    jump scene8
                if not cred:
                    scene bg night room
                    show leon depressed
                    "Leon has not built up even half his emergency fund when rumours of recession started going around."
                    pause 0.2
                    "Frustrated about his wrong choice, Leon becomes anxious about the future"
                    pause 0.3
                    "The spirit watches worriedly and guiltily as Leon's anxiety grows"
                    $ b_end = True
                    jump end
    else:
        p "Setting an emergency fund target is a smart move. Let's break it down. Your monthly discretionary savings are $800. How much of it is essential?"
        pause 0.1
        "{b}Aggressive Saving: {/b}I'll cut down on discretionary spending and allocate the majority of my $800 towards my emergency fund. It might mean sacrificing some extras, but it's worth the security."
        pause 0.6
        "{b}Gradual Build-Up: {/b}I'll aim for the four-month target but gradually build it up over the next six months from $100 to $500. This way, I can still enjoy some of the things I like without drastic lifestyle changes."
        pause 0.6
        "{b}Split Debt{/b} :I have some debts to pay off. I'll allocate a portion of my discretionary savings to clear debts  for $400 and the rest of $400 towards building up my emergency fund. How does that sound?"
        pause 0.6
        menu:
            "Aggresive Saving":
                scene bg busy streett
                show leon formals at right
                if cred:
                    l "I'm so happy to finally build up my emergency fund. It really takes a lot of weight off my shoulders that I didn't even realize I carried. Thank you!"
                    pause 0.2
                    hide leon formals
                    "The spirit is very pleased to see Leon jumping with joy"
                    $ emf = True
                    jump scene8
                else:
                    scene bg night room
                    show leon depressed
                    l "Ughh, I only have enough to spend for my bare essentials, my lifestyle keeps detoriating"
                    pause 0.2
                    "Frustrated and angry about his lost lifestyle, Leon becomes temperamental"
                    pause 0.1
                    "The spirit tries to comfort Leon but ultimately stops, hesistating and driven with guilt"
                    $ b_end = True
                    jump end
            "Gradual Build-Up":
                if cred:
                    scene bg night room
                    show leon depressed
                    "Leon's choice of credit plan limits his financial options and in the end, he never gets to grow his emergency fund"
                    pause 0.2
                    "Frustrated and regretting his choices, Leon loses confidence in himself"
                    pause 0.3
                    "The spirit watches worriedly and guiltily as Leon becomes more indecisive"
                    $ b_end = True
                    jump end
                else:
                    scene bg busy streett
                    show leon formals at right
                    l "I'm so happy to finally build up my emergency fund. It really takes a lot of weight off my shoulders that I didn't even realize I carried. Thank you!"
                    pause 0.2
                    hide leon formals
                    "The spirit is very pleased to see Leon jumping with joy"
                    $ emf = True
                    jump scene8
            "Split Debt":
                if cred:
                    scene bg busy streett
                    show leon formals at right
                    l "I'm so happy to finally build up my emergency fund. It really takes a lot of weight off my shoulders that I didn't even realize I carried. Thank you!"
                    pause 0.2
                    hide leon formals
                    "The spirit is very pleased to see Leon jumping with joy"
                    $ emf = True
                    jump scene8
                if not cred:
                    scene bg night room
                    show leon depressed
                    "Leon has not built up even half his emergency fund when rumours of recession started going around."
                    pause 0.2
                    "Frustrated about his wrong choice, Leon becomes anxious about the future"
                    pause 0.3
                    "The spirit watches worriedly and guiltily as Leon's anxiety grows"
                    $ b_end = True
                    jump end
        

label scene8:
    scene bg laptop shop out
    "Leon finds himself in a tech upgrade dilemma. His laptop, essential for his work as a software engineer, is getting outdated. He ponders whether to invest in a new one, repair the existing one, or explore budget-friendly alternatives."
    pause 0.5
    l frowning "My laptop is definitely showing signs of age. Should I invest in a new one, try to repair this one, or explore more budget-friendly alternatives?"
    pause 0.1
    p "A tech upgrade is a significant decision. Let's weigh the options. What's the current state of your laptop, and how critical is it for your work?"
    pause 0.2
    l "It's slowing down, and I've noticed lag during my coding sessions. It's crucial for my work as a software engineer, and I can't afford significant downtime."
    pause 0.2
    p "Understood. Now, let's explore your options for resolving this tech upgrade dilemma."
    pause 0.1
    "{b}Invest in a High-End Laptop:{/b}Considering your work demands, investing in a high-end laptop with powerful specs might ensure smooth performance and longevity. It's a significant upfront cost but could be a solid investment, cost $1500."
    pause 0.5
    "{b}Repair and Upgrade Current Laptop: {/b}If your current laptop has potential and sentimental value, investing in repairs and upgrades might be a cost-effective option. It could extend its lifespan for another year or two. Option Cost:$300"
    pause 0.5
    "{b}Explore Budget-Friendly Alternatives: {/b}Consider exploring budget-friendly alternatives. This could be a mid-range laptop that meets your essential needs without the hefty price tag. It might not have all the bells and whistles but could get the job done. Option Cost:$800"
    pause 0.5
    menu:
        "Invest in High-End Laptop":
            if not d_1200 and not flex:
                scene bg night room
                show leon depressed
                "Leon succumbs to the allure of a high-priced laptop, investing a significant chunk of his funds. The aftermath is an overworked and tired Leon, with dwindling resources."
                pause 0.2
                "Strained by the weight of financial decisions, he reluctantly turns to his parents for assistance. The convergence of exhaustion and financial pressure casts a shadow of depression over him."
                pause 0.2
                $ b_end = True
                jump end
            else:
                scene bg laptop shop
                show leon formals at left
                l "I'd like to get the latest V21 Laptop on display 9"
                pause 0.1
                "......."
                "......."
                scene bg comm street
                show leon formals at center with move
                l "Yes! This is the laptop I bought on my own! I'm so happy"
                pause 0.1
                "The spirit watches Leon fondly as he excitedly went home"
                jump scene9
        "Repair and Upgrade Current Laptop":
            scene bg laptop shop
            show leon formals at left
            l "Hello, I'd like to have my laptop repaired, is that service available?"
            pause 0.1
            "......."
            "......."
            scene bg comm street
            show leon formals at center with move
            l "Yes! This one is finally fixed! It's faster than ever, I'm so happy"
            pause 0.1
            "The spirit watches Leon fondly as he excitedly went home"
            jump scene9
        "Explore Budget-Friendly Alternatives":
            scene bg laptop shop
            show leon formals at left
            l "Hello, I'd like to buy the older versioned Zen8 Laptop, is that Available?"
            pause 0.1
            "......."
            "......."
            scene bg comm street
            show leon formals at center with move
            l "Yes! This one was what I wanted to get in my college days! And now, I bought it with my own money!"
            pause 0.1
            "The spirit watches Leon fondly as he excitedly went home"
            jump scene9

label scene9:
    scene bg insurance building
    "Leon realizes that he needs to choose a health insurance plan. He’s never had to do this before and is unsure about how much coverage he needs and how much he can afford."
    pause 0.4
    show leon formals at left
    l "I need to choose a health insurance plan, but I’m not sure what to look for. How much coverage do I need? And how much can I afford?"
    pause 0.2
    p "Choosing a health insurance plan is an important decision, Leon. Let’s consider your options based on your health needs and budget."
    pause 0.2
    scene bg insurance inside
    show insurance agent work at right
    show leon formals at left
    i "{b}High Coverage Plan:{/b} A high coverage plan would have higher premiums, but it would cover most of your medical expenses. This could be a good option if you have ongoing health issues or want peace of mind knowing you’re covered for most health situations."
    pause 0.5
    i "{b}Medium Coverage Plan:{/b} A medium coverage plan would have lower premiums than a high coverage plan, but it wouldn’t cover as much. This could be a good option if you’re generally healthy but want to be covered for common health issues."
    pause 0.5
    i "{b}Low Coverage Plan:{/b} A low coverage plan would have the lowest premiums, but it would also provide the least coverage. This could be a good option if you’re very healthy and only want coverage for emergency situations."
    pause 0.5
    hide insurance agent work
    menu:
        "High Coverage Plan":
            if d_none or not flex:
                scene bg night room
                show leon depressed at center
                "Leon, unable to afford high-coverage insurance, overworks to make ends meet. The relentless grind takes a toll, leaving him fatigued and impacting his performance at work."
                "As mistakes accumulate, a sense of depression envelops Leon, a consequence of the challenging balance between financial constraints and professional demands."
                pause 0.2
                "The spirit grows increasingly worried and beats itself up for its wrong guidance"
                $ b_end = True
                jump end
            else:
                show bg busy streett
                show leon formals
                "Leon, elated with his decision for a high-coverage insurance plan, walks home with a newfound sense of security."
                "The weight of financial worry lifted, he carries a lightness in his steps, savoring the contentment that comes with making thoughtful and beneficial choices."
                pause 0.3
                $ hcover = True
                jump scene10
        "Medium Coverage Plan":
            show bg busy streett
            show leon formals
            "Leon, elated with his decision for a medium-coverage insurance plan, walks home with a newfound sense of security."
            "The weight of financial worry lifted, he carries a lightness in his steps, savoring the contentment that comes with making thoughtful and beneficial choices."
            pause 0.1
            $ mcover = True
            jump scene10
        "Low Coverage Plan":
            if not cred and not d_none:
                scene bg busy streett
                show leon sad
                "As summer intensifies, Leon begins to regret his choice of a low-coverage insurance plan. The scorching heat exposes the gaps in his coverage, leaving him uneasy and wishing he had opted for a more comprehensive policy."
                pause 0.1
                "The realization dawns as regret casts a shadow over his sense of security."
                $ lcover = True
                jump scene10
            else:
                show bg busy streett
                show leon formals
                "Leon, elated with his decision for a low-coverage insurance plan, walks home with a newfound sense of security."
                "The weight of financial worry lifted, he carries a lightness in his steps, savoring the contentment that comes with making thoughtful and beneficial choices."
                pause 0.3
                $ lcover = True
                jump scene10

label scene10:
    scene bg hospital in
    "After choosing his health insurance plan, Leon faces his first health crisis. He had a minor accident at home and had to visit the emergency room. Now, he’s faced with a significant medical bill and needs to figure out how to handle it."
    scene bg hospital room
    show leon injured at left
    show hospital nurse work at right
    if hcover:
        n "Since you chose the high coverage plan, most of your medical expenses should be covered. You’ll need to pay the deductible and any copayments, but the insurance should cover the rest."
        pause 0.2
        scene bg hospital out
        show leon injured at right
        l "Thank god, I chose the high coverage plan! I would be toast if I chose a wrong plan!"
        pause 0.2
        p "The spirit follows Leon home, worried and amused"
        pause 0.2
        

    elif mcover:
        if (d_none or not flex and s_1500) or not emf:
            n "With the medium coverage plan, common medical expenses are covered. You’ll need to pay the deductible, any copayments, and possibly some additional costs if not everything is covered"
            pause 0.2
            scene bg hospital out
            show leon injured at left
            "With a medium-coverage insurance plan, Leon faces a minor emergency requiring deductibles. However, lacking quick cash on hand, regret seeps in."
            "He wishes he had prepared better for unforeseen situations, realizing the importance of having immediate funds for unexpected emergencies."
            $ b_end = True
            jump end
        else:
            n "With the medium coverage plan, common medical expenses are covered."
            "You’ll need to pay the deductible, any copayments, and possibly some additional costs if not everything is covered"
            pause 0.2
            scene bg hospital out
            show leon injured at right
            l "Thank god, I chose the medium coverage plan and had some emergency fund at hand! I would be toast if I chose a wrong plan!"
            pause 0.2
            p "The spirit follows Leon home, worried and amused"
            pause 0.2
        
    elif lcover:
        if (d_none and s_1500 ) or (not cred and not flex) or (not emf):
            n "The low coverage plan only covers emergency medical expenses. Depending on the specifics of your plan, you may need to pay a significant portion of the bill yourself."
            scene bg hospital out
            show leon injured at left
            "Leon, burdened by a low-coverage insurance plan that falls short, faces a situation demanding more than it offers."
            pause 0.1
            "With no cash at hand, he reluctantly turns to his parents for financial help. The weight of dependence and limited coverage sinks him into a state of depression, highlighting the consequences of financial vulnerability."
            pause 0.4
            $ b_end = True
            jump end
        else:
            n "The low coverage plan only covers emergency medical expenses. Depending on the specifics of your plan, you may need to pay a significant portion of the bill yourself."
            scene bg hospital out
            show leon injured at left
            l "Thank goodness, I kept some money at hand, I should definitely upgrade my insurance plan!"
            pause 0.4
            jump end


label end:
    if b_end:
        '{color=#fd1200}{b}Bad Ending{/b}{/color}'
        pause 0.8
        return
    else:
        '{b}{color=#0a6522}Happy Ending{/b}{/color}'
        "Congratulations on reaching the end! But hey, more trickier questions will come up soon."
        pause 0.4
        "Along with more interesting people to help......"
        return