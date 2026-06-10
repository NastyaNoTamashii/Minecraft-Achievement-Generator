"""

Copyright (C) 2026 NastyaNoTamashii.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2026 present NastyaNoTamashii
:license: MIT license, see LICENSE for more details.

"""

import re
from pathlib import Path
from colorama import Fore, init
from PIL import Image, ImageDraw, ImageFont

from banner import BANNER

init()

# MINECRAFT COLORS
colors = {
    "&0": "#000000",
    "&1": "#0000AA",
    "&2": "#00AA00",
    "&3": "#00AAAA",
    "&4": "#AA0000",
    "&5": "#AA00AA",
    "&6": "#FFAA00",
    "&7": "#AAAAAA",
    "&8": "#555555",
    "&9": "#5555FF",
    "&a": "#55FF55",
    "&b": "#55FFFF",
    "&c": "#FF5555",
    "&d": "#FF55FF",
    "&e": "#FFFF55",
    "&f": "#FFFFFF"
}

def achievememnt_maker(
        title: str,
        color: str, # &0-&f
        description: str,
        icon: str
        ):
    
    if icon is None or icon == "": icon = "Minecraft/grass_block_side"

    icon_path = Path("icons/{}.png".format(icon))

    if icon_path.is_file() == False:
        print(Fore.YELLOW+"\nIcon not found! Make sure the icon ID is correct and the corresponding PNG file exists in the 'icons' directory.\n"+Fore.RESET)
        return

    if len(title) > 18:
        print(Fore.YELLOW+"\nTitle is too long! Max 18 characters.\n"+Fore.RESET)
        return
    
    if len(description) > 25:
        print(Fore.YELLOW+"\nDescription is too long! Max 25 characters.\n"+Fore.RESET)
        return
    
    if not color or color == "":
        color = "&e"
    
    if color in colors:
        color = colors[color]
    
    img_achievement = Image.open("blank.png")
    draw = ImageDraw.Draw(img_achievement)

    draw.text((60, 12), 
            text = title, 
            font = ImageFont.truetype("Monocraft.otf", 18), 
            fill = color
        )
    
    draw.text((60, 35),
            text = description,
            font = ImageFont.truetype("Monocraft.otf", 15),
            fill = "white"
        )

    icon_img = Image.open(f"icons/{icon}.png")
    icon_img = icon_img.resize((42, 42))
    img_achievement.paste(icon_img, (11, 11), icon_img)
    
    file_name = title.replace(' ','_').lower()

    img_achievement.save(f"achievements/{file_name}.png")

    print(f"\nAchievement generated successfully! Saved as 'achievements/{file_name}.png'")
    print("Rate me!{} At https://github.com/NastyaNoTamashii/Minecraft-Achievement-Generator\n".format(Fore.YELLOW))

if __name__ == "__main__":
    print(BANNER)

    title = input("Achievement title (max 18 characters): ")
    color = input("Title Color (Minecraft colors &0-&f or Hex): ")
    description = input("Achievement description (max 25 characters): ")
    icon = input("Icon ID: ")

    achievememnt_maker(title, color, description, icon)
