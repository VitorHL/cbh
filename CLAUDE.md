# CLAUDE.md — Coppernell Hill

## Project Overview

Coppernell Hill is a visual novel / interactive fiction game built with **Ren'Py 8.3.7**. It features a skill-based dice system (2d6), character interactions, inventory management, calendar progression, and a hub-based navigation system. Resolution is 1920x1080 with a retro VHS aesthetic (VCR font, grain/scanline effects).

## Directory Structure

```
game/
  core/              # Core game systems (characters, skills, events, inventory, etc.)
  definitions/       # Data definitions for game objects
    characters/      # Character definitions (Claire, Gia, Daniel, Val, Boss, Karol)
  scenes/
    locations/       # Scene scripts per location (9 locations)
    test_scenes/     # Test scenarios
  screens/           # UI/screen definitions (12 files)
  GFX/               # Graphics (sprites, backgrounds, fonts, UI elements)
    characters/      # Character sprite animations (webp)
    background/      # Background images (webp)
    fonts/           # VCR_OSD_MONO font
    interface/       # UI graphics (buttons, bars, sliders)
  gui/               # GUI theme assets (button states, scrollbars, overlays, dice)
  audio/             # Sound effects and music (ogg/wav)
  localization/      # Translation keys
  tl/                # Translation files
  options.rpy        # Game config (version, audio, layers, build settings)
  script.rpy         # Main entry point (~225 lines)
  gui.rpy            # GUI styling (~474 lines)
  screens.rpy        # Main screen definitions (~1,395 lines)
```

## Core Systems (`game/core/`)

| File | System | Key Elements |
|------|--------|-------------|
| `0_core.rpy` | Utilities | `get_var_name()`, `callback_builder()` for character animations |
| `characters.rpy` | Characters | `game_character` class — talks, items, flags tracking |
| `skills.rpy` | Skills/Dice | `game_skill` class, `game_skill_roll()`, 2d6 probability tables |
| `calendar.rpy` | Time | `game_calendar` class — day/month/year/weekday progression |
| `events.rpy` | Events | `game_event` class — priority-based with calendar triggers |
| `interactions.rpy` | NPC dialogue | `game_interaction` class — tracks dialogue state |
| `iventory.rpy` | Items | `game_item` class — owned items and character reactions |
| `navigation.rpy` | Rooms | `game_room` class — hub-based travel system |
| `leveling.rpy` | Progression | `add_xp()`, `player_levelup()` — XP and level cap at 16 |
| `gui_functions.rpy` | GUI helpers | Skill point allocation/reset |

## Naming Conventions

- **Classes:** `game_<type>` (e.g., `game_skill`, `game_character`, `game_room`)
- **Functions:** `snake_case` (e.g., `add_xp`, `player_levelup`, `set_room`)
- **Variables:** `snake_case` with type suffixes (e.g., `skill_inquiry`, `skill_inquiry_loc`)
- **Labels:** `<type>_<name>_label` or `<character>_<action>` (e.g., `daniel_apartment_label`, `char_gia_hello`)
- **Localization:** `_loc` suffix for localized names (e.g., `LOC_room_edgar_counter`)
- **Colors:** Hex assigned per character (Claire `#3962af`, Gia `#b32137`, etc.)

## Game Mechanics

- **Dice rolls:** 2d6 + skill level. Natural 2 always fails, 12 always succeeds. Buffs supported.
- **Skills (6):** Inquiry, Insight, Acuity, Sentiment, Resolve, Communion
- **Progression:** 7 attribute points at start, 1 per level. XP from rolls (15), dialogues (10), items (5).
- **Difficulty scale:** TRIVIAL through HEROIC with color coding
- **Events:** Priority-based (lower = higher), calendar-triggered, room-specific or global
- **Navigation:** Hub-based rooms with travel lists, thumbnails, and custom travel sounds

## Screen/UI Patterns

- Modal screens prevent ESC menu during critical sections
- Menu selections support `skill_roll=` or `skill_check=` attributes on choices
- Custom styles: `select_button`, `hover_button`, `desc_text`
- VHS overlay effects via webp grain and scanline animations
- Custom Ren'Py layers: `master`, `transient`, `underlay`, `vignette`, `screens`, `overlay`, `vhs_screens`, `effect_overlay`

## Build & Development

- **Engine:** Ren'Py 8.3.7.25031702
- **Build name:** `dicetest`
- **Compilation:** Ren'Py auto-compiles `.rpy` to `.rpyc` bytecode
- **File exclusions:** `.rpyc`, `.rpa`, `.rpymc`, and `cache/` are excluded from builds and hidden in VS Code
- **No external test framework** — testing is done via in-game test scenes (`game/scenes/test_scenes/`)

## Known Issues

1. **`tag menu` in `inventory_screen`** (`game/screens/choice_menu.rpy:408`): `tag` is not a valid keyword for screen statements in Ren'Py 8.3.7. Prevents compilation.
2. **`Hide(self)` in `choice_menu.rpy:520`**: `self` is not defined in screen context. Use `Return()` or the explicit screen name instead.
3. **Typo `iventory`**: The inventory system file and some references use `iventory` instead of `inventory`. This is consistent throughout the codebase — do not "fix" one occurrence without renaming all of them.

## Important Notes for AI Assistants

- This is a **Ren'Py** project, not a standard Python project. Files use `.rpy` extension with Ren'Py-specific syntax (labels, screens, ATL, init blocks).
- There is no `pip`, `npm`, or standard build tooling. The game is built and run through the Ren'Py SDK/launcher.
- There are no automated tests or linters. Validate changes by checking Ren'Py syntax rules.
- When editing screens, be aware of Ren'Py's screen language — it is indentation-sensitive and has its own keywords (`screen`, `use`, `action`, `hbox`, `vbox`, `frame`, etc.).
- Character sprites use animated webp files with callback-based transitions defined in `0_core.rpy`.
- The `localization/` directory handles i18n — text in game scripts should use `_()` for translatable strings.
