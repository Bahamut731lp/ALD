'''
Test suite pro úlohu 6
'''
import lifo

def test_case_trivial():
    """
        Test triviálního případu ze zadání
    """
    original = """pro aplikaci zasobnik
toto je ukazka vstupu"""

    vzor = """Toto Je Ukazka Vstupu
Pro Aplikaci Zasobnik"""

    vysledek = lifo.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_1():
    """
        Testovací případ 1
    """
    original = """middle class god save the queen a total jessie geordie eton mess come hither flog jammy git beefeater pie-eyed
hard cheese old boy challenge you to a duel tallywhacker fake tan one feels that bogroll
old chap marvelous it's nicked pompous
absolute twoddle lost the plot it's the bees knees throw a paddy knee high to a grasshopper i'll be a monkey's uncle
marmite well fit ey up duck owt pie-eyed
smeg victoria sponge cake clotted cream gobsmacked get away with ya squiffy bangers and mash
doofer could be a bit of a git got a lot of brass a bottle of plonk hard cheese old boy bovver boots
sausage roll a right corker done up like a kipper 'ar kid it's just not cricket a tad upper class
down the village green spam fritters stupendous gutted
union jack pompous nutter chin up mush"""

    vzor = """Union Jack Pompous Nutter Chin Up Mush
Down The Village Green Spam Fritters Stupendous Gutted
Sausage Roll A Right Corker Done Up Like A Kipper 'ar Kid It's Just Not Cricket A Tad Upper Class
Doofer Could Be A Bit Of A Git Got A Lot Of Brass A Bottle Of Plonk Hard Cheese Old Boy Bovver Boots
Smeg Victoria Sponge Cake Clotted Cream Gobsmacked Get Away With Ya Squiffy Bangers And Mash
Marmite Well Fit Ey Up Duck Owt Pie-eyed
Absolute Twoddle Lost The Plot It's The Bees Knees Throw A Paddy Knee High To A Grasshopper I'll Be A Monkey's Uncle
Old Chap Marvelous It's Nicked Pompous
Hard Cheese Old Boy Challenge You To A Duel Tallywhacker Fake Tan One Feels That Bogroll
Middle Class God Save The Queen A Total Jessie Geordie Eton Mess Come Hither Flog Jammy Git Beefeater Pie-eyed"""

    vysledek = lifo.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_2():
    """
        Testovací případ 2
    """
    original = """sausage roll a right corker done up like a kipper 'ar kid it's just not cricket a tad upper class
smeg victoria sponge cake clotted cream gobsmacked get away with ya squiffy bangers and mash
marmite well fit ey up duck owt pie-eyed
pommy ipsum a right corker ey up duck farewell brainbox
brainbox weeping angels conkers up at the crack of dawn scrumpy round our gaff sonic screwdriver bowler hat
absolute twoddle lost the plot it's the bees knees throw a paddy knee high to a grasshopper i'll be a monkey's uncle
yorkshire pudding jolly good essex girls good old fashioned knees up a cuppa at the boozer
brainbox weeping angels conkers up at the crack of dawn scrumpy round our gaff sonic screwdriver bowler hat
absolute twoddle lost the plot it's the bees knees throw a paddy knee high to a grasshopper i'll be a monkey's uncle
old chap marvelous it's nicked pompous"""

    vzor = """Old Chap Marvelous It's Nicked Pompous
Absolute Twoddle Lost The Plot It's The Bees Knees Throw A Paddy Knee High To A Grasshopper I'll Be A Monkey's Uncle
Brainbox Weeping Angels Conkers Up At The Crack Of Dawn Scrumpy Round Our Gaff Sonic Screwdriver Bowler Hat
Yorkshire Pudding Jolly Good Essex Girls Good Old Fashioned Knees Up A Cuppa At The Boozer
Absolute Twoddle Lost The Plot It's The Bees Knees Throw A Paddy Knee High To A Grasshopper I'll Be A Monkey's Uncle
Brainbox Weeping Angels Conkers Up At The Crack Of Dawn Scrumpy Round Our Gaff Sonic Screwdriver Bowler Hat
Pommy Ipsum A Right Corker Ey Up Duck Farewell Brainbox
Marmite Well Fit Ey Up Duck Owt Pie-eyed
Smeg Victoria Sponge Cake Clotted Cream Gobsmacked Get Away With Ya Squiffy Bangers And Mash
Sausage Roll A Right Corker Done Up Like A Kipper 'ar Kid It's Just Not Cricket A Tad Upper Class"""

    vysledek = lifo.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_3():
    """
        Testovací případ 3
    """
    original = """chippy i'd reet fancy a nuthouse the hounds of baskerville
hard cheese old boy challenge you to a duel tallywhacker fake tan one feels that bogroll
sausage roll a right corker done up like a kipper 'ar kid it's just not cricket a tad upper class
yorkshire pudding jolly good essex girls good old fashioned knees up a cuppa at the boozer
old chap marvelous it's nicked pompous
pork scratchings could be a bit of a git how's your father marmite queen elizabeth done up like a kipper absobloodylootely spend a penny knee high to a grasshopper i'll be a monkey's uncle
down the village green spam fritters stupendous gutted
sausage roll a right corker done up like a kipper 'ar kid it's just not cricket a tad upper class
10 pence mix stupendous know your onions pillock ridicule blighty
doofer could be a bit of a git got a lot of brass a bottle of plonk hard cheese old boy bovver boots"""

    vzor = """Doofer Could Be A Bit Of A Git Got A Lot Of Brass A Bottle Of Plonk Hard Cheese Old Boy Bovver Boots
10 Pence Mix Stupendous Know Your Onions Pillock Ridicule Blighty
Sausage Roll A Right Corker Done Up Like A Kipper 'ar Kid It's Just Not Cricket A Tad Upper Class
Down The Village Green Spam Fritters Stupendous Gutted
Pork Scratchings Could Be A Bit Of A Git How's Your Father Marmite Queen Elizabeth Done Up Like A Kipper Absobloodylootely Spend A Penny Knee High To A Grasshopper I'll Be A Monkey's Uncle
Old Chap Marvelous It's Nicked Pompous
Yorkshire Pudding Jolly Good Essex Girls Good Old Fashioned Knees Up A Cuppa At The Boozer
Sausage Roll A Right Corker Done Up Like A Kipper 'ar Kid It's Just Not Cricket A Tad Upper Class
Hard Cheese Old Boy Challenge You To A Duel Tallywhacker Fake Tan One Feels That Bogroll
Chippy I'd Reet Fancy A Nuthouse The Hounds Of Baskerville"""

    vysledek = lifo.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_4():
    """
        Testovací případ 4
    """
    original = """middle class god save the queen a total jessie geordie eton mess come hither flog jammy git beefeater pie-eyed
10 pence mix stupendous know your onions pillock ridicule blighty
bossy britches trouble and strife challenge you to a duel stew and dumps got his end away got a lot of brass
hard cheese old boy challenge you to a duel tallywhacker fake tan one feels that bogroll
pork scratchings could be a bit of a git how's your father marmite queen elizabeth done up like a kipper absobloodylootely spend a penny knee high to a grasshopper i'll be a monkey's uncle
smeg victoria sponge cake clotted cream gobsmacked get away with ya squiffy bangers and mash
marmite well fit ey up duck owt pie-eyed
pork scratchings could be a bit of a git how's your father marmite queen elizabeth done up like a kipper absobloodylootely spend a penny knee high to a grasshopper i'll be a monkey's uncle
middle class god save the queen a total jessie geordie eton mess come hither flog jammy git beefeater pie-eyed
sausage roll a right corker done up like a kipper 'ar kid it's just not cricket a tad upper class"""

    vzor = """Sausage Roll A Right Corker Done Up Like A Kipper 'ar Kid It's Just Not Cricket A Tad Upper Class
Middle Class God Save The Queen A Total Jessie Geordie Eton Mess Come Hither Flog Jammy Git Beefeater Pie-eyed
Pork Scratchings Could Be A Bit Of A Git How's Your Father Marmite Queen Elizabeth Done Up Like A Kipper Absobloodylootely Spend A Penny Knee High To A Grasshopper I'll Be A Monkey's Uncle
Marmite Well Fit Ey Up Duck Owt Pie-eyed
Smeg Victoria Sponge Cake Clotted Cream Gobsmacked Get Away With Ya Squiffy Bangers And Mash
Pork Scratchings Could Be A Bit Of A Git How's Your Father Marmite Queen Elizabeth Done Up Like A Kipper Absobloodylootely Spend A Penny Knee High To A Grasshopper I'll Be A Monkey's Uncle
Hard Cheese Old Boy Challenge You To A Duel Tallywhacker Fake Tan One Feels That Bogroll
Bossy Britches Trouble And Strife Challenge You To A Duel Stew And Dumps Got His End Away Got A Lot Of Brass
10 Pence Mix Stupendous Know Your Onions Pillock Ridicule Blighty
Middle Class God Save The Queen A Total Jessie Geordie Eton Mess Come Hither Flog Jammy Git Beefeater Pie-eyed"""

    vysledek = lifo.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_5():
    """
        Testovací případ 4
    """
    original = """yorkshire pudding jolly good essex girls good old fashioned knees up a cuppa at the boozer
union jack pompous nutter chin up mush
bossy britches trouble and strife challenge you to a duel stew and dumps got his end away got a lot of brass
middle class god save the queen a total jessie geordie eton mess come hither flog jammy git beefeater pie-eyed
brainbox weeping angels conkers up at the crack of dawn scrumpy round our gaff sonic screwdriver bowler hat
down the village green spam fritters stupendous gutted
bossy britches trouble and strife challenge you to a duel stew and dumps got his end away got a lot of brass
pork scratchings could be a bit of a git how's your father marmite queen elizabeth done up like a kipper absobloodylootely spend a penny knee high to a grasshopper i'll be a monkey's uncle
smeg victoria sponge cake clotted cream gobsmacked get away with ya squiffy bangers and mash
yorkshire pudding jolly good essex girls good old fashioned knees up a cuppa at the boozer"""

    vzor = """Yorkshire Pudding Jolly Good Essex Girls Good Old Fashioned Knees Up A Cuppa At The Boozer
Smeg Victoria Sponge Cake Clotted Cream Gobsmacked Get Away With Ya Squiffy Bangers And Mash
Pork Scratchings Could Be A Bit Of A Git How's Your Father Marmite Queen Elizabeth Done Up Like A Kipper Absobloodylootely Spend A Penny Knee High To A Grasshopper I'll Be A Monkey's Uncle
Bossy Britches Trouble And Strife Challenge You To A Duel Stew And Dumps Got His End Away Got A Lot Of Brass
Down The Village Green Spam Fritters Stupendous Gutted
Brainbox Weeping Angels Conkers Up At The Crack Of Dawn Scrumpy Round Our Gaff Sonic Screwdriver Bowler Hat
Middle Class God Save The Queen A Total Jessie Geordie Eton Mess Come Hither Flog Jammy Git Beefeater Pie-eyed
Bossy Britches Trouble And Strife Challenge You To A Duel Stew And Dumps Got His End Away Got A Lot Of Brass
Union Jack Pompous Nutter Chin Up Mush
Yorkshire Pudding Jolly Good Essex Girls Good Old Fashioned Knees Up A Cuppa At The Boozer"""

    vysledek = lifo.main(original.strip().splitlines())
    assert vzor == vysledek
