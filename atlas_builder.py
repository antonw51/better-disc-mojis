# Atlas builder
# Add emoji's to the atlas.toml and compile an emoji atlas with this utility.
# Credits goes to https://github.com/tototomate123 for writing this script for me.

import sys
import toml
from PIL import Image

def replace_emoji_in_atlas(atlas_path, emoji_dir, config_path, emoji_size=(80, 80)):
    atlas = Image.open(atlas_path).convert("RGBA")

    config = toml.load(config_path)
    
    print("Loaded config file.")
    print("Starting to replace emojis in atlas...")
    
    buffer_space = 30
    
    for i in range(0, len(config['emojis'])):
        emoji_name = list(config['emojis'].keys())[i]
        position = str(config['emojis'][emoji_name]['position'])

        x, y = map(int, position.split(','))
        x -= 1
        y -= 1
        
        emoji_path = f"{emoji_dir}/{emoji_name}.png"
        
        emoji = Image.open(emoji_path).convert("RGBA")

        x_pos = x * emoji_size[0]
        y_pos = y * emoji_size[1]

        transparent_area = Image.new('RGBA', emoji_size, (0, 0, 0, 0))
        
        atlas.paste(transparent_area, (x_pos, y_pos))

        atlas.paste(emoji, (x_pos, y_pos), emoji)
        print("Replaced:", emoji_name, " " * int(buffer_space - len(emoji_name)), "at (", str(x_pos) + ",", y_pos, ") - (", str(x_pos + emoji_size[0]) + ",", y_pos + emoji_size[1], ")")

    atlas.save('updated_atlas.png')
    print("Updated atlas saved as 'updated_atlas.png'.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py atlas.png emoji_directory config.toml")
        sys.exit(1)
    
    atlas_path = sys.argv[1]
    emoji_dir = sys.argv[2]
    config_path = sys.argv[3]

    replace_emoji_in_atlas(atlas_path, emoji_dir, config_path)
