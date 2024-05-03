header_formats = ["ExMx", "MAPxx"]

header = ""
map_num = 1
episode = 1

def process_header_format():
    if iwad in iwad_doom or iwad in iwad_heretic:
        header = f"MAP E{episode}M{map_num}"
    elif (iwad in iwad_doom2 or iwad in iwad_hexen) and map_num < 10:
        header = f"MAP MAP0{map_num}"
    elif (iwad in iwad_doom2 or iwad in iwad_hexen) and map_num >= 10:
        header = f"MAP MAP{map_num}"
    else:
        print(f"ERROR: {iwad} is not a recognized IWAD")

def process_header_map_num():
    if map_num not in range(1,100):
        print(f"ERROR: map_num is out of bounds")

def process_header_episode():
    if episode not in range(1,10):
        print(f"ERROR: episode is out of bounds")
