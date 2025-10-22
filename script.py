import requests

url = r"https://raw.githubusercontent.com/48klocs/dim-wish-list-sources/master/voltron.txt"

file = requests.get(url)

download_file = "./wish_list.txt"

convert_text = file.text

final_file = []

for eachWishListItem in convert_text.split("\n\n"):
    if "pandapaxxy" not in eachWishListItem:
        final_file.append(eachWishListItem)

with open(download_file, "w") as f:
    for eachItem in final_file:
        f.write(eachItem)
        f.write("\n\n")
