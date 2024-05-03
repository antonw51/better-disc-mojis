# better-disc-mojis

The emoji theme for discord's alternative emoji style, as seen on the message bar emoji button on desktop.

> [!NOTE]
> Sadly, at the time of this README file, _**better-disc-mojis**_ does **not** support all the standard emojis, not even a full category, only select emojis.

On desktop, the message bar in Discord has an emoji button, which on hover displays a random emoji; this is a different set from the discord original emojis and features a flat, simple, quad-color design meant to simplify and unify the emojis we see everyday.

These few emojis aren't available for use within Discord however, so this theme/repository means to bridge that gap.

_Better-disc-mojis_ provides a couple ways to use emojis, either the two available theme files: `FlatMojis.theme.css` (for the best experience) and `FlatMojisVariant.theme.css` (Experiments with some custom made additional emojis. W.I.P. _might not ever release!_). These theme files can be used with a Discord client to replace the default emojis and give a overall better experience. Alternatively the source SVG and PNG files are also available for those that want to either create custom emojis, build on the emojis, or do something completely different.

## Installation

> [!NOTE]
> This is an installation guide for the better-disc-moji theme files, thus you must have a modified discord client like BetterDiscord, Vencord or Powercord to allow you to load a custom CSS file and override the default emojis if you wish to use these theme files.

1. Prepare a discord client with support for CSS themes.
2. Find your themes configuration (Typically: Settings -> "Client": Themes)
3. Download the either the `FlatMojis.theme.css` or the `FlatMojisVariant.theme.css` from this repository (Or, for Vencord grab a link to the raw contents of those files)
4. Add your selected file to your client's theme directory (or on Vencord alternatively link one of the file under "Online Themes")
5. **Done!** Supported emojis should be shown in the Emoji Picker, Reactions, and messages.

## Building

When adding new emojis to the set, you may want to add them to the theme, this can be done rather easily with two python scripts.

### Prerequisites
1. An emoji, both in a 24x24pt SVG and a 80x80 transparent PNG file.
2. A default emoji you wish to replace.
3. Python3 and Python3-toml (`pip install toml` or on Ubuntu/deb `sudo apt install pyton3-toml`)

### Adding an emoji

> [!NOTE]
> Your emoji PNG and SVG files must be named the same as the discord emojis they replace.

To add an emoji to the existing set, make sure you have selected a default discord emoji to replace and add an entry to the `emojis.toml` file

Your emoji should have these three fields, albeit optional if left blank. Your emoji must however be titled after an existing emoji in discord:
    - **position**: (For your emoji to show up in the emoji picker) Look at the `source-atlas.png` file and find the emoji you wish to replace, count the grid spots (starting from 1, 1 in the top-left corner) and add that position to this entry (e.g. "13,2")
    - **emoji**: (For your emoji to show up in reactions) Send the emoji you plan to replace and _from the chat_ copy the emoji and paste it into this entry. This value must be a unicode emoji and not a discord emoji (e.g. ":dizzy_face:") or a null unicode character (e.g. "�").
    - **discord_id**: (For your emoji to show up in the suggestions bar) Again send the emoji you plan to replace in a discord chat, but this time _from the chat_ right click it and select _"Copy Link"_ paste this link somewhere and extract the part after "assets/" but trim off the suffixing ".svg", leaving you with a id for this field (e.g. "578a868786e07850a386", not "https://discord.com/assets/578a868786e07850a386.svg" nor "578a868786e07850a386.svg").

Additionally, to allow for your emoji to render, you'll need to fork the directory and publicize your own, then replace the [setup.repository] field with a link to your forked github repository:
```toml
[setup]
repository="https://github.com/your-user/your-fork-repo"
```

Once you've added your emoji and linked your repositoy, you're ready to re-build the theme.

### Building

Building the theme can be done with a simple command: 

```bash
$ python3 atlas_builder.py source_atlas.png res emojis.toml && python3 css_builder.py
```

This 

## Contributions

_Better-disc-mojis_ is open to contribution for as long as it remains available.

You can help/contribute by either creating more SVG files for existing discord emojis, opening issues to report bugs with the theme files, or by forking this repository and finishing what Discord/I have started.

PR's with emojis may be modified, _better-disc-mojis_ interprets the flat style of emoji as having a simple set of rules:

1. All emojis use at most four unique colors, one for the color or _"skin tone"_ of the emoji, a black for detail, and two free colors depending on emoji. (On occasion this convention can be broken, see `partying_face`)
2. The default emoji skin color is `#FCC145`, the standard used black is `#020202`, and the standard white used is `#F6FAFE`. These colors are universal but can differ on circumstance.
3. Emojis use common elements, the most common which being a 3pt*3pt dot or filled circle for eyes, a 2pt rounded, straight or curved line, a universal tongue, a universal heart, and a universal drop of water. These common elements apply to faces only.
4. Emojis are, for the most part, simple. Don't use unnecessary detail, and if appropriate (for a face), stick to a format of two eyes and a mouth, no eyebrows or teeth in most emojis.
5. Emojis are fitted within a 24pt*24pt bounding box

For the _better-disc-mojis_ repository, submitted emojis will be subject to modification to suit these conventions if they don't already. If you don't like a rule, then feel free to fork and try your own with these emojis.

You can also open issues to suggest emojis to be added, will I add them? Likely not, and if yes, then the simpler the better. _But someone else might!_

**Avoid creating duplicate issues.**

## License

I felt best not to use a license, as I am under belief that this project might infringe on Discord property. This repository will be taken down if a report on Discord's behalf is made.

But for now (and hopefully forever) feel free to fork, copy, modify, and use these emojis to your own accord. You _could_ try to sell or redistribute them, but I can't advise for or against that.
