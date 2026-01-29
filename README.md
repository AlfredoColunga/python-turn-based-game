# 🧙‍♂️ Wizard Tower Defense

A turn-based terminal game where you play as a wizard defending Lady Elianor's tower from invading enemies using powerful and dangerous spells.

## 📖 Story

All your companions have died at the hands of five enemies who broke into the wizard tower. Lady Elianor, the plump, furry cat who leads the wizard clan, has given you only one order: **Kill them all.**

As the last surviving wizard, you must face each enemy in turn-based combat using forbidden magic. But every spell comes with a price, and failure can cost you dearly.

## ✨ Features

- **Turn-based combat system** - Strategic spell casting against waves of enemies
- **5 unique spells** with dynamic success rates that evolve based on your performance
- **Risk-reward gameplay** - Powerful spells can backfire with devastating consequences
- **Status effects** - Apply debilitating effects to enemies or suffer permanent disabilities

## 🎮 Gameplay

### Combat
1. View your current health and available spells
2. Choose a spell to cast against the current enemy
3. Spell success is determined by its current success rate
4. Successful spells damage or debuff enemies; failures harm you
5. If the enemy survives, they counterattack
6. Repeat until all enemies are defeated or you die

### Spell System

Each spell has a **dynamic success rate** that starts at 50%:
- ✅ **Success**: Rate increases by 10% (max 90%)
- ❌ **Failure**: Rate decreases by 10% (min 10%)

## 🔮 Spells

| Spell | Type | Effect (Success) | Effect (Failure) | Requirement |
|-------|------|------------------|------------------|-------------|
| **Agony** | Attack | Instantly kills the enemy | Destroys your hands permanently | Hands |
| **Cadaver** | Attack | Kills the enemy | Rots your mouth permanently | Mouth |
| **Denial** | Healing | Restores health to maximum | Enemy kills you | Hands |
| **Paranoid** | Debuff | Enemy becomes inanimate and cannot attack | You become a vase, lose your hands | Hands |
| **Retrogression** | Debuff | Enemy's next attack deals 0 damage | No effect | Mouth |

### Permanent Consequences

- **Lost Hands**: Cannot cast Agony, Denial, or Paranoid
- **Lost Mouth**: Cannot cast Cadaver or Retrogression
- **Paranoid Effect**: The enemy cannot attack
- **Retrogression Effect**: Lasts only one enemy turn

## 📁 Project Structure

```
wizard-tower-defense/
│
├── main.py           # Entry point - starts the game
├── battle.py         # Battle system and game loop
├── player.py         # Player class with spell casting logic
├── enemy.py          # Enemy class with attack mechanics
├── spells.py         # Spell class with success rate system
└── README.md         # This file
```

## 🎯 How to Play

1. **Start the game**: Run `python main.py`
2. **Read the intro**: Learn about your mission
3. **Choose wisely**: Type the name of the spell you want to cast
   - Valid inputs: `Agony`, `Cadaver`, `Denial`, `Paranoid`, `Retrogression`
4. **Watch the outcome**: See if your spell succeeds or fails
5. **Survive**: Defeat all 5 enemies without dying
6. **Adapt**: Adjust your strategy based on success rates and available body parts

### Example Gameplay Session

```
===< Current Health >===
        100
===< Known Spells >===
Agony -- Success rate: 50%
Cadaver -- Success rate: 50%
Denial -- Success rate: 50%
Paranoid -- Success rate: 50%
Retrogression -- Success rate: 50%
Write your attack: agony

You have performed a forbidden hand movement...

The enemy has split in two, and you have seen his soul slowly leave his body.

The next enemy is approaching you...
```

## 🎲 Strategy Tips

1. **Use Paranoid early** - Permanently disables enemy attacks if successful
2. **Save Denial for emergencies** - But remember it can kill you if it fails
3. **Watch success rates** - Successful spells become more reliable
4. **Protect your body parts** - Losing hands or mouth limits your options
5. **Use Retrogression defensively** - Nullify dangerous enemy attacks

## 🛠️ Technical Details

### Classes

- **Battle**: Manages game flow, enemy waves, and win/loss conditions
- **Player**: Handles health, spell casting, and body part status
- **Enemy**: Manages enemy attacks, status effects, and damage calculation
- **Spell**: Defines spell properties and dynamic success rate system

### Key Mechanics

- **Random damage**: Enemies deal 1-100 damage per attack
- **Success calculation**: Uses `random.random()` compared against spell success rate
- **State management**: Player and enemy states persist throughout combat
- **Terminal clearing**: Cross-platform support (Windows/Unix)