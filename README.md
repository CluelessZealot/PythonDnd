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

