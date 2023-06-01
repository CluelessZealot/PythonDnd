# CSC160_Final_Create <br>
You have been tasked with creating a Python game that allows the user to traverse several levels and become a hero . But first, a few quick notes: <br>
-Your assignment should be completed in IDLE on your machine, not in GitHub. <br>
-You will only be using GitHub to get the URL for your repository. That is the URL in the address bar right now! <br>
---Don't worry right now if those terms seem unfamiliar. We will learn them in time! Just know that you do not need to leave this page to get started. <br>

The first thing that you should do is reference the [Submitting an Assignment using Github](https://otc.instructure.com/courses/50195/files/8233081?wrap=1) document. This will walk you through the process of ensuring that Git is installed on your computer and that you can download your assignment. Once you have completed step 3 in the instruction, you will be ready to begin programming. Please use the below instructions as a point of reference. <br>

To begin the assignment, open the CreateFinal.py file in IDLE. <br>
There is no example output for this file. I encourage you to engage with your team creatively to make a suitable output <br>
Your completed program should reflect the following: <br>

# Group Assignment <br>
-This is a group assignment, ensure that you are working with your group to meet the objectives. <br>
-Decide on one person, and submit their repository link to Canvas for grading. <br>
-All team members will receieve the same base grade with adjustments made for individual performance <br>
-You can see who your team members are in Canvas, or on Microsoft Teams. <br>
---In Canvas, go to "People" and look in the Final Project Groups.

# Program Description <br>
-This program is a very small text-based video game where a single player traverses five levels where they will battle monsters, find treasure, and eventually defeat the boss <br>

# Program Flow <br>
-The player is presented with a character creation screen where they can choose their name and starter "class" <br>
-Upon creating their character the user is presented with their options for the first level: <br>
--Battle a monster- The user enters a battle sequence with a monster <br>
--Search for treasure- The user has a chance to be healed, find treasure, or encounter a monster <br>
--Advance to next level- The user advances to the next level (This should only be availble after defeating a certain number of monsters) <br>
--Check current stats- The user should be able to see their current action options as well as their stats and weapon <br>
-Upon reaching level 5 the user is presented with only the option to challenge the boss <br>
-Once the boss is defeated the game is over and the user should be a shown a graph demonstrating the monsters defeated and treasures obtained per level before the user is given the option to play again with a new character <br>

# Battling <br>
-When in the battle sequence the user should have the following options: <br>
--Attack: A generic attack (damage is calculated using weapon damage and attack stat. There is not base damage for general attacks) <br>
--Action: The player uses one of their actions (If doing damage this should take into account weapon damage, attack stat, and base power) <br>
---Actions are powerful, so they are limited in use. Each action should have a limited number of uses per a level <br>
---You can include a treasure option that replenishes action uses <br>
--Inspect: Examine the information for the monster (actions and stats) <br>
--Run: Have a certain percent chance to flee an encounter and return to the level menu <br>
-Upon defeating an enemy, the user should be granted experience points that contribute to their level <br>
-The amount of health the character has should carry over between battles. If the character ends a battle with 75/100 health, they should start the next encounter with 75/100 health. <br>
-Advancing to the next level restores all health and action uses <br>

# Treasure <br>
-When searching for treasure, the user should have a chance to have any one of the following interactions <br>
--Encounter a monster (should be scaled as if the player is on the next level. (if encounter is on level 1, then the monster should be scaled for level 2) <br>
--Find Treasure- treasure can be: <br>
---A new action for the character to learn <br>
---A way for the characters health to be restored <br>
---A way for action uses to be restored <br>
---A new weapon for the character to equip (Let them choose if they would like to drop their current weapon for the new one) <br>

# Weapons <br>
-Weapons only have one stat value, which is damage <br>
--Damage is a non-magic attack value that should be used in formulas for determining non-magic attacks/actions <br>

# Characters <br>
-The character should have a level of their own that goes up upon collecting enough experience <br>
--When a characters level increases they should receive a boost to some or all stats <br>
-When saving the game, all information for the character and current level should be saved to a file so that the player can continue later <br>
-When opening the program, if there is a character available, they can continue that campaign or begin a new one. A new campaign should not overwrite an old one <br>
--Save files can be deleted when the boss is defeated <br>

# Technical Requirements <br>
-Players must be given a choice of four classes, each with a different speciality and name <br>
--Speciality will be determined by stats and weapon. <br>

-Each character and monster has six stats <br>
--Attack: Determines how strong an attack action is <br>
--Magic: Determines how strong a spell action is <br>
--Defence: Determines how much the character/monster will resist an opposing attack action <br>
--Resistance: Determines how much the character/monster will resist an opposing magic action <br>
--Speed: Determines how fast the character/monster can move <br>
--HP (Health Points): When health points reach 0, the character/monster is knocked out <br>

-Each character/monster should have it's stats randomized within a certain range <br>
--Instead of assigning a static stat value for each character/monster each time the program is run, a random value should be given <br>
--This random value will be detailed further when discussing specialty <br>

-This time, you get to create four different classes of characters and monster for your users to engage with <br>
--Create 4 character classes that each have different specialties and a unique starting weapon <br>
---Due to the nature of how regular attack damage is calculated. A class that relies soley on the magic stat for damage should start with a third action that can be used an unlimited number of times per a level. This action should do comparable damage to a regular attack from any of the other classes <br>
--Create 4 monster classes that each have different specialties

-Each of the above stats should be a number value tied to an object. The number value should be randomly generated within a range. <br>
--You get to decide what the number range is for each category <br>

-You need to program no fewer than 20 unique actions for your characters and monsters to learn. <br>
--Each monster should know a minimum of two actions. This means that some moves can be repeated across monsters <br>
--Characters can learn up to 5 actions, an should start with just 2 <br>
----More character actions can be unlocked when finding treasure <br>
--Each action should have a unique name and effect, as well as a designation of if it does attack or magic damage <br>
--Example Action: <br>
[Valient Lance] <br>
-Description: A shining lance pierces the opponent's hopes. The opponent takes medium damage and cries through their next turn <br>
-Programming: Action has 50 base-power. Enemy HP is reduced upon use, next turn for opponent is skipped <br>

-All actions and effects should be programmed into individual functions <br>
--Calculate damage dealt using a formula of your own creation. The required varaibles for the formula are: <br>
---Attacking user's attack stat or magic stat<br>
---Defencing user's defence stat or resistance stat <br>
---Attacking user's action's base power (not applicable for regular attacks)<br>
--The result of your formula should be subtracted from the defending user's HP <br>

-Battle sequences should end once the monster or the character reaches 0 HP <br>

-There is a lot to do here, but if you divide the tasks amongst your group and plan accordingly you will be succesful! <br>

-Be sure to give your users the following options: <br>
--Allow user to examine the actions of their character before selecting them <br>
--Allow the user to check their current stats during a batte, as well as their action descriptions<br>


-Please see the rubric in Canvas for grading criteria 
