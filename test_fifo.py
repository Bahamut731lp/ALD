'''
Test suite pro úlohu 5
'''
import fifo

def test_case_trivial():
    """
        Test triviálního případu ze zadání
    """
    original = """toto je ukazka vstupu
    pro aplikaci fronta"""

    vzor = """Toto Je Ukazka Vstupu
Pro Aplikaci Fronta"""

    vysledek = fifo.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_1():
    """
        Testovací případ 1
    """
    original = """chippy i'd reet fancy a nuthouse the hounds of baskerville
pork scratchings could be a bit of a git how's your father marmite queen elizabeth done up like a kipper absobloodylootely spend a penny knee high to a grasshopper i'll be a monkey's uncle
union jack pompous nutter chin up mush
sausage roll a right corker done up like a kipper 'ar kid it's just not cricket a tad upper class
pommy ipsum a right corker ey up duck farewell brainbox
sausage roll a right corker done up like a kipper 'ar kid it's just not cricket a tad upper class
hard cheese old boy challenge you to a duel tallywhacker fake tan one feels that bogroll
marmite well fit ey up duck owt pie-eyed
brainbox weeping angels conkers up at the crack of dawn scrumpy round our gaff sonic screwdriver bowler hat
down the village green spam fritters stupendous gutted"""

    vzor = """Chippy I'd Reet Fancy A Nuthouse The Hounds Of Baskerville
Pork Scratchings Could Be A Bit Of A Git How's Your Father Marmite Queen Elizabeth Done Up Like A Kipper Absobloodylootely Spend A Penny Knee High To A Grasshopper I'll Be A Monkey's Uncle
Union Jack Pompous Nutter Chin Up Mush
Sausage Roll A Right Corker Done Up Like A Kipper 'ar Kid It's Just Not Cricket A Tad Upper Class
Pommy Ipsum A Right Corker Ey Up Duck Farewell Brainbox
Sausage Roll A Right Corker Done Up Like A Kipper 'ar Kid It's Just Not Cricket A Tad Upper Class
Hard Cheese Old Boy Challenge You To A Duel Tallywhacker Fake Tan One Feels That Bogroll
Marmite Well Fit Ey Up Duck Owt Pie-eyed
Brainbox Weeping Angels Conkers Up At The Crack Of Dawn Scrumpy Round Our Gaff Sonic Screwdriver Bowler Hat
Down The Village Green Spam Fritters Stupendous Gutted"""

    vysledek = fifo.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_2():
    """
        Testovací případ 2
    """

    original = """chippy i'd reet fancy a nuthouse the hounds of baskerville
10 pence mix stupendous know your onions pillock ridicule blighty
absolute twoddle lost the plot it's the bees knees throw a paddy knee high to a grasshopper i'll be a monkey's uncle
10 pence mix stupendous know your onions pillock ridicule blighty
brainbox weeping angels conkers up at the crack of dawn scrumpy round our gaff sonic screwdriver bowler hat
pommy ipsum a right corker ey up duck farewell brainbox
brainbox weeping angels conkers up at the crack of dawn scrumpy round our gaff sonic screwdriver bowler hat
pork scratchings could be a bit of a git how's your father marmite queen elizabeth done up like a kipper absobloodylootely spend a penny knee high to a grasshopper i'll be a monkey's uncle
chippy i'd reet fancy a nuthouse the hounds of baskerville
marmite well fit ey up duck owt pie-eyed"""

    vzor = """Chippy I'd Reet Fancy A Nuthouse The Hounds Of Baskerville
10 Pence Mix Stupendous Know Your Onions Pillock Ridicule Blighty
Absolute Twoddle Lost The Plot It's The Bees Knees Throw A Paddy Knee High To A Grasshopper I'll Be A Monkey's Uncle
10 Pence Mix Stupendous Know Your Onions Pillock Ridicule Blighty
Brainbox Weeping Angels Conkers Up At The Crack Of Dawn Scrumpy Round Our Gaff Sonic Screwdriver Bowler Hat
Pommy Ipsum A Right Corker Ey Up Duck Farewell Brainbox
Brainbox Weeping Angels Conkers Up At The Crack Of Dawn Scrumpy Round Our Gaff Sonic Screwdriver Bowler Hat
Pork Scratchings Could Be A Bit Of A Git How's Your Father Marmite Queen Elizabeth Done Up Like A Kipper Absobloodylootely Spend A Penny Knee High To A Grasshopper I'll Be A Monkey's Uncle
Chippy I'd Reet Fancy A Nuthouse The Hounds Of Baskerville
Marmite Well Fit Ey Up Duck Owt Pie-eyed"""

    vysledek = fifo.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_3():
    """
        Testovací případ 3
    """

    original = """middle class god save the queen a total jessie geordie eton mess come hither flog jammy git beefeater pie-eyed
down the village green spam fritters stupendous gutted
middle class god save the queen a total jessie geordie eton mess come hither flog jammy git beefeater pie-eyed
bits 'n bobs chav bossy britches time lord a comely wench bobby gravy cheese and chips
10 pence mix stupendous know your onions pillock ridicule blighty
doofer could be a bit of a git got a lot of brass a bottle of plonk hard cheese old boy bovver boots
chippy i'd reet fancy a nuthouse the hounds of baskerville
yorkshire pudding jolly good essex girls good old fashioned knees up a cuppa at the boozer
10 pence mix stupendous know your onions pillock ridicule blighty
hard cheese old boy challenge you to a duel tallywhacker fake tan one feels that bogroll"""

    vzor = """Middle Class God Save The Queen A Total Jessie Geordie Eton Mess Come Hither Flog Jammy Git Beefeater Pie-eyed
Down The Village Green Spam Fritters Stupendous Gutted
Middle Class God Save The Queen A Total Jessie Geordie Eton Mess Come Hither Flog Jammy Git Beefeater Pie-eyed
Bits 'n Bobs Chav Bossy Britches Time Lord A Comely Wench Bobby Gravy Cheese And Chips
10 Pence Mix Stupendous Know Your Onions Pillock Ridicule Blighty
Doofer Could Be A Bit Of A Git Got A Lot Of Brass A Bottle Of Plonk Hard Cheese Old Boy Bovver Boots
Chippy I'd Reet Fancy A Nuthouse The Hounds Of Baskerville
Yorkshire Pudding Jolly Good Essex Girls Good Old Fashioned Knees Up A Cuppa At The Boozer
10 Pence Mix Stupendous Know Your Onions Pillock Ridicule Blighty
Hard Cheese Old Boy Challenge You To A Duel Tallywhacker Fake Tan One Feels That Bogroll"""

    vysledek = fifo.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_4():
    """
        Testovací případ 4
    """

    original = """down the village green spam fritters stupendous gutted
marmite well fit ey up duck owt pie-eyed
old chap marvelous it's nicked pompous
marmite well fit ey up duck owt pie-eyed
doofer could be a bit of a git got a lot of brass a bottle of plonk hard cheese old boy bovver boots
brainbox weeping angels conkers up at the crack of dawn scrumpy round our gaff sonic screwdriver bowler hat
smeg victoria sponge cake clotted cream gobsmacked get away with ya squiffy bangers and mash
doofer could be a bit of a git got a lot of brass a bottle of plonk hard cheese old boy bovver boots
pommy ipsum a right corker ey up duck farewell brainbox
smeg victoria sponge cake clotted cream gobsmacked get away with ya squiffy bangers and mash"""

    vzor = """Down The Village Green Spam Fritters Stupendous Gutted
Marmite Well Fit Ey Up Duck Owt Pie-eyed
Old Chap Marvelous It's Nicked Pompous
Marmite Well Fit Ey Up Duck Owt Pie-eyed
Doofer Could Be A Bit Of A Git Got A Lot Of Brass A Bottle Of Plonk Hard Cheese Old Boy Bovver Boots
Brainbox Weeping Angels Conkers Up At The Crack Of Dawn Scrumpy Round Our Gaff Sonic Screwdriver Bowler Hat
Smeg Victoria Sponge Cake Clotted Cream Gobsmacked Get Away With Ya Squiffy Bangers And Mash
Doofer Could Be A Bit Of A Git Got A Lot Of Brass A Bottle Of Plonk Hard Cheese Old Boy Bovver Boots
Pommy Ipsum A Right Corker Ey Up Duck Farewell Brainbox
Smeg Victoria Sponge Cake Clotted Cream Gobsmacked Get Away With Ya Squiffy Bangers And Mash"""

    vysledek = fifo.main(original.strip().splitlines())
    assert vzor == vysledek

def test_case_5():
    """
        Testovací případ 5
    """

    original = """smeg victoria sponge cake clotted cream gobsmacked get away with ya squiffy bangers and mash
bossy britches trouble and strife challenge you to a duel stew and dumps got his end away got a lot of brass
marmite well fit ey up duck owt pie-eyed
pommy ipsum a right corker ey up duck farewell brainbox
down the village green spam fritters stupendous gutted
absolute twoddle lost the plot it's the bees knees throw a paddy knee high to a grasshopper i'll be a monkey's uncle
10 pence mix stupendous know your onions pillock ridicule blighty
middle class god save the queen a total jessie geordie eton mess come hither flog jammy git beefeater pie-eyed
smeg victoria sponge cake clotted cream gobsmacked get away with ya squiffy bangers and mash
hard cheese old boy challenge you to a duel tallywhacker fake tan one feels that bogroll"""

    vzor = """Smeg Victoria Sponge Cake Clotted Cream Gobsmacked Get Away With Ya Squiffy Bangers And Mash
Bossy Britches Trouble And Strife Challenge You To A Duel Stew And Dumps Got His End Away Got A Lot Of Brass
Marmite Well Fit Ey Up Duck Owt Pie-eyed
Pommy Ipsum A Right Corker Ey Up Duck Farewell Brainbox
Down The Village Green Spam Fritters Stupendous Gutted
Absolute Twoddle Lost The Plot It's The Bees Knees Throw A Paddy Knee High To A Grasshopper I'll Be A Monkey's Uncle
10 Pence Mix Stupendous Know Your Onions Pillock Ridicule Blighty
Middle Class God Save The Queen A Total Jessie Geordie Eton Mess Come Hither Flog Jammy Git Beefeater Pie-eyed
Smeg Victoria Sponge Cake Clotted Cream Gobsmacked Get Away With Ya Squiffy Bangers And Mash
Hard Cheese Old Boy Challenge You To A Duel Tallywhacker Fake Tan One Feels That Bogroll"""

    vysledek = fifo.main(original.strip().splitlines())
    assert vzor == vysledek
