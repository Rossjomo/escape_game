# ESCAPE

#### Ross Morton
#### Edx: RossMorton
#### Github: Rossjomo
#### Video Demo: https://youtu.be/_EeMcXNJJrM
#### 24.07.24
#### Description:
Escape is a game based on a "choose your own adventure" kind of book where you have to choose doors in order to escape a dungeon. Behind the doors may be an empty hallway or a monster. If you encounter a monster it triggers a D&D or Warhammer style dice rolling battle.

I chose this type of game as it would require using collections of data in lists and dictionaries of players and monsters statistics. It would also require input from the user which would need to be cleaned and verified. I used while loops with Try and Except with ValueErrors to ensure that there was an input from the name and that the type of warrior was in the list. I used regex to recognise either the words left or right or the first letters of these words but reject other or no inputs.

I created three player types with small variation in their statistics to make them more attacking, more defensive or balanced. Although the game is based on dice rolling and therefore down to chance there could be some benefit to picking certain player types.

Initially I used the idea of a single monster called monster but I choose to change this to Ogre, Gremlin and Troll so they could have different health and attack stats. This means that replaying the game will be less repetitive and ideally more fun. This will also allow for easy future development (for example an dragon or a werewolf, etc)

I used pyfiglet to give the intro and key events a bit of style as well as an appropriate blood font for the game over text. I choose this as I want the game to have a bit of style and not just be text. I also remembered using the tabulate module during the course, this allowed me to present statistics in a clean and readable way and separate blocks of text too.

I looked into the time module as I found that all the text arriving on the screen at the same time was hard to read and follow. The sleep function allowed me to stagger the arrival of the text on the screen.

The Dice rolling function was initially two functions but combined with the default to make just one, using the default for the warrior and passing the monster attack stat to create the dice rolling range.

When I first created the choose_door function it only served to interact with the user as the monster was then randomly chosen. However I wanted to have this have an impact, so for this reason I changed the program to randomly choose from the list of opponents. Using pop, remove these two options from the list and return them so there are two doors with set with two randomly selected opponents. I did this using global to allow me to enter and edit this variable. This also feels more accurate to how the books work.

During the testing phase I realised that I had an anomaly in the code. When the defence was reducing the the attack of the monster, if the attack was very weak and less than the defence the warriors health would increase. I added the max function to make sure that the warrior health was not being added to.

I added some other functions to make the code more modular as this then made the test file far simpler to write, execute and test.

Also while writing the tests I realised that I would have to research unittest and learn about mock in order to patch/control the random elements and be able to test for the expected output from the fight function.
