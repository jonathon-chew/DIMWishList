import requests
from os import chdir, path

# Get the directory of the currently running script
script_dir = path.dirname(path.abspath(__file__))
chdir(script_dir)

# The current wish list url
url = r"https://raw.githubusercontent.com/48klocs/dim-wish-list-sources/master/voltron.txt"

# Get the wish list
file = requests.get(url)

# Record the file name to be used elsewhere
download_file = "./wish_list.txt"

# Store the text in a variable
convert_text = "title:This is a compiled collection of god/recommended rolls from top community minds.\n\ndescription:Thanks to u/Mercules904, @AyyItsChevy, @chrisfried, u/-seudonym-, u/zman2100, u/goddamtofu, Gleauxx, GodInGaming, Beenlab, CoolCheese, Critbuff, Apathettic, Ekuegan, Jarv, Ascendant Nomad, Shadow, Pijinnn, AbbyHour, GodinGaming, illPhysics, BRAVExHERO, Pattycakes, blueberries.gg, YeezyGT, @johnldixon, WarlockMaggie, 2bithacker, and whyayala for their contributions. Ping u/48klocs / @48klocs with any issues.\n\n" + file.text

# Save the current version of the wish list - in case of future development
with open("./voltron.txt", "w") as f:
    f.write(convert_text)

# Initialise the array
final_file = []

# Break the file up as per the formating - 2 back to back new lines, if the user name is present ANYWHERE in the text, remove. This will also remove if username appears anywhere in the comments for another creator
for eachWishListItem in convert_text.split("\n\n"):
    if "pandapaxxy" not in eachWishListItem:
        final_file.append(eachWishListItem)

# Write the resulting array into the file and add back in the formatting, to split up the different items as DIM expects
with open(download_file, "w") as f:
    for eachItem in final_file:
        f.write(eachItem)
        f.write("\n\n")
