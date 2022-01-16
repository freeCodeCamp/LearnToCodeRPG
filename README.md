# Learn to Code RPG

**Learn to Code RPG** is a visual novel game developed by **freeCodeCamp.org**. In this game, you will teach yourself to code, make friends in the tech industry, and pursue your dream to become a developer 🎯

The game features:
- Hours of gameplay 🎮
- Original art & music 🎨
- 600+ Computer Science quiz questions 📚
- 50+ Easter Eggs you can discover 🚀
- 6 different endings 👀
- Friendly characters and an adorable cat 🐱
- Minigames! 👾


<div><a href="https://freecodecamp.itch.io/learn-to-code-rpg"><img src="https://github.com/freeCodeCamp/LearnToCodeRPG/blob/df44a3b66015021f939ef210af039d0ade1ca33a/badge-bw.png" alt="Available on itch.io" width="400"/></a></div>

<div><img src="https://github.com/freeCodeCamp/LearnToCodeRPG/blob/b2313a272536f5fd8ef653162cc97dd46e185745/game/gui/main_menu.png" alt="Learn to Code RPG Splash Image" width="600"/></div>

This game was made possible by all the kind people who donate to support freeCodeCamp.org. You can help support our nonprofit's mission [here](https://www.freecodecamp.org/news/how-to-donate-to-free-code-camp/).

This project is open source and is currently in beta. If you notice any bugs or have suggestions about accessibility, the interface, the story, or anything at all, please report them by opening **GitHub issues**.

If you are enjoying this game, please rate and review us on [itch.io](https://freecodecamp.itch.io/learn-to-code-rpg).

If you are interested in how we made this game, check out [this article (a Let's Play video included)](https://www.freecodecamp.org/news/learn-to-code-rpg/).

## Credits

| Creative Lead                 | [Lynn Zheng](https://ruolinzheng08.github.io/) |
|-------------------------------|------------|
| Coding & Writing & Misc. Art  | [Lynn Zheng](https://ruolinzheng08.github.io/) |
| Music                         | [Quincy Larson](https://twitter.com/ossia) |
| Character Art                 | [Layerto (Noa Trinh)](https://layerto.carrd.co) |
| Quiz Questions & Proofreading | [Abbey Rennemeyer](https://twitter.com/abbeyrenn) <br /> [Oliver Eyton-Williams](https://github.com/ojeytonwilliams/) <br /> [Estefania Cassingena Navone](https://twitter.com/EstefaniaCassN) <br /> [Jessica Wilkins](https://twitter.com/codergirl1991) <br /> [Dionysia Lemonaki](https://twitter.com/deniselemonaki) <br /> |
| Playtesting                   | [Ilenia Magoni](https://twitter.com/ieahleen) <br /> [Estefania Cassingena Navone](https://twitter.com/EstefaniaCassN) <br /> [Nicholas Carrigan](https://twitter.com/nhcarrigan) <br /> [Yoko Matsuda](https://twitter.com/_sidemt) <br /> [Daniel Rosa](https://twitter.com/Daniel__Rosa) <br /> [Beau Carnes](https://twitter.com/beaucarnes) <br /> |

### How to report bugs

Found a bug while playing?

Read through [this helpful article](https://forum.freecodecamp.org/t/how-to-report-a-bug-to-the-freecodecamp-open-source-community/19543) on how to report bugs.

Then, report them by opening a **GitHub Issue**.

### How to contribute

This open source project is a work in progress and ever evolving. We will publish major expansions to this game in the coming months, including new music and characters.

We welcome all contributions, suggestions and ideas for improvement from the community.

You can contribute by adding new quiz questions to [developerquiz.org](https://github.com/freeCodeCamp/Developer_Quiz_Site), catching typos, and **volunteering to localize this game into other languages**.

Make sure to first read through the [Code of Conduct](https://www.freecodecamp.org/news/code-of-conduct/).

Then, see the ways you can contribute [here](https://contribute.freecodecamp.org/#/).

#### How to help with translation

The Crowdin (our localization platform) link will be posted here shortly.

##### Instructions
- The sentences to be translated are always between `""`. These are dialogues or UI strings.
- In case of `new "..."` Do not translate `new`. 
- Prefixes like `player`, `annika`, `layla`, `marco` (or variants like `player @ happy`) should not be translated.
- Do not translate things between `[]` and `{}`. These are variable interpolations and text tags.

##### Examples

---
https://github.com/freeCodeCamp/LearnToCodeRPG/blob/351f26074b441d056ab9d6e1381e8be1e9ede8b1/game/tl/traditional_chinese/script.rpy#L61

###### Before translation

```renpy
# "[player_name]? What a coincidence! Our VIP team member {a=[vip_profile_url]}[player_name]{/a} will be honored to hear that."
"[player_name]? What a coincidence! Our VIP team member {a=[vip_profile_url]}[player_name]{/a} will be honored to hear that."  <--- this is the line that needs to be translated. see translation below
```

###### After translation

```renpy
# "[player_name]? What a coincidence! Our VIP team member {a=[vip_profile_url]}[player_name]{/a} will be honored to hear that."
"[player_name]？好巧，我们的VIP队友{a=[vip_profile_url]}[player_name]{/a}会很高兴的。"
```

Note: The `[]` and `{}` tags should be left intact.

---

https://github.com/freeCodeCamp/LearnToCodeRPG/blob/351f26074b441d056ab9d6e1381e8be1e9ede8b1/game/tl/traditional_chinese/screens.rpy#L15

###### Before translation

```renpy
old "{icon=icon-fast-forward} Skip"
new "{icon=icon-fast-forward} Skip" <-- translate this line, see below
```

###### After translation

```renpy
old "{icon=icon-fast-forward} Skip"
new "{icon=icon-fast-forward} 跳过"
```

Note: Again, the `new` prefix and the `{icon=icon-fast-forward}` tag should be left intact.

---

###### Before translation

```renpy
# layla @ neutral "Hehe, [player_name], you are a fun one. I'm sure you will enjoy your work as a developer."
layla @ neutral "Hehe, [player_name], you are a fun one. I'm sure you will enjoy your work as a developer."
```

###### After translation

```renpy
# layla @ neutral "Hehe, [player_name], you are a fun one. I'm sure you will enjoy your work as a developer."
layla @ neutral "哈哈，[player_name]，你真有趣。我相信你一定会喜欢你的开发者工作的。"
```

Note: `layla @ neutral` and `[player_name]` are left unchanged.

---

### License

Copyright © 2021 freeCodeCamp.org, All rights reserved.
