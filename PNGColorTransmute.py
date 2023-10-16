import os
from PIL import Image

# Diretórios de origem e destino
src_dir = "srcdir"
dst_dir = "dstdir"

# Lista de cores
colors = [
    "IndianRed",
    "LightCoral",
    "Salmon",
    "DarkSalmon",
    "LightSalmon",
    "Crimson",
    "Red",
    "FireBrick",
    "DarkRed",
    "Pink",
    "LightPink",
    "HotPink",
    "DeepPink",
    "MediumVioletRed",
    "PaleVioletRed",
    "Coral",
    "Tomato",
    "OrangeRed",
    "DarkOrange",
    "Orange",
    "Gold",
    "Yellow",
    "LightYellow",
    "LemonChiffon",
    "LightGoldenrodYellow",
    "PapayaWhip",
    "Moccasin",
    "PeachPuff",
    "PaleGoldenrod",
    "Khaki",
    "DarkKhaki",
    "Lavender",
    "Thistle",
    "Plum",
    "Violet",
    "Orchid",
    "Fuchsia",
    "Magenta",
    "MediumOrchid",
    "MediumPurple",
    "RebeccaPurple",
    "BlueViolet",
    "DarkViolet",
    "DarkOrchid",
    "DarkMagenta",
    "Purple",
    "Indigo",
    "SlateBlue",
    "DarkSlateBlue",
    "MediumSlateBlue",
    "GreenYellow",
    "Chartreuse",
    "LawnGreen",
    "Lime",
    "LimeGreen",
    "PaleGreen",
    "LightGreen",
    "MediumSpringGreen",
    "SpringGreen",
    "MediumSeaGreen",
    "SeaGreen",
    "ForestGreen",
    "Green",
    "DarkGreen",
    "YellowGreen",
    "OliveDrab",
    "Olive",
    "DarkOliveGreen",
    "MediumAquamarine",
    "DarkSeaGreen",
    "LightSeaGreen",
    "DarkCyan",
    "Teal",
    "Aqua",
    "Cyan",
    "LightCyan",
    "PaleTurquoise",
    "Aquamarine",
    "Turquoise",
    "MediumTurquoise",
    "DarkTurquoise",
    "CadetBlue",
    "SteelBlue",
    "LightSteelBlue",
    "PowderBlue",
    "LightBlue",
    "SkyBlue",
    "LightSkyBlue",
    "DeepSkyBlue",
    "DodgerBlue",
    "CornflowerBlue",
    "MediumSlateBlue",
    "RoyalBlue",
    "Blue",
    "MediumBlue",
    "DarkBlue",
    "Navy",
    "MidnightBlue",
    "Cornsilk",
    "BlanchedAlmond",
    "Bisque",
    "NavajoWhite",
    "Wheat",
    "BurlyWood",
    "Tan",
    "RosyBrown",
    "SandyBrown",
    "Goldenrod",
    "DarkGoldenrod",
    "Peru",
    "Chocolate",
    "SaddleBrown",
    "Sienna",
    "Brown",
    "Maroon",
    "White",
    "Snow",
    "Honeydew",
    "MintCream",
    "Azure",
    "AliceBlue",
    "GhostWhite",
    "WhiteSmoke",
    "Seashell",
    "Beige",
    "OldLace",
    "FloralWhite",
    "Ivory",
    "AntiqueWhite",
    "Linen",
    "LavenderBlush",
    "MistyRose",
    "Gainsboro",
    "LightGray",
    "Silver",
    "DarkGray",
    "Gray",
    "DimGray",
    "LightSlateGray",
    "SlateGray",
    "DarkSlateGray",
    "Black"
]

# Função para alterar a cor da imagem
def change_image_color(img, color):
    data = img.getdata()
    new_data = []
    for item in data:
        # Alterar a cor se não for transparente
        if item[3] > 0:
            new_data.append((color[0], color[1], color[2], item[3]))
        else:
            new_data.append(item)
    img.putdata(new_data)
    return img

# Mapeamento de cores para RGB
def hex_to_rgb(value):
    value = value.lstrip('#')
    length = len(value)
    return tuple(int(value[i:i+length//3], 16) for i in range(0, length, length//3))

color_map = {
    "IndianRed": hex_to_rgb("#CD5C5C"),
    "LightCoral": hex_to_rgb("#F08080"),
    "Salmon": hex_to_rgb("#FA8072"),
    "DarkSalmon": hex_to_rgb("#E9967A"),
    "LightSalmon": hex_to_rgb("#FFA07A"),
    "Crimson": hex_to_rgb("#DC143C"),
    "Red": hex_to_rgb("#FF0000"),
    "FireBrick": hex_to_rgb("#B22222"),
    "DarkRed": hex_to_rgb("#8B0000"),
    "Pink": hex_to_rgb("#FFC0CB"),
    "LightPink": hex_to_rgb("#FFB6C1"),
    "HotPink": hex_to_rgb("#FF69B4"),
    "DeepPink": hex_to_rgb("#FF1493"),
    "MediumVioletRed": hex_to_rgb("#C71585"),
    "PaleVioletRed": hex_to_rgb("#DB7093"),
    "Coral": hex_to_rgb("#FF7F50"),
    "Tomato": hex_to_rgb("#FF6347"),
    "OrangeRed": hex_to_rgb("#FF4500"),
    "DarkOrange": hex_to_rgb("#FF8C00"),
    "Orange": hex_to_rgb("#FFA500"),
    "Gold": hex_to_rgb("#FFD700"),
    "Yellow": hex_to_rgb("#FFFF00"),
    "LightYellow": hex_to_rgb("#FFFFE0"),
    "LemonChiffon": hex_to_rgb("#FFFACD"),
    "LightGoldenrodYellow": hex_to_rgb("#FAFAD2"),
    "PapayaWhip": hex_to_rgb("#FFEFD5"),
    "Moccasin": hex_to_rgb("#FFE4B5"),
    "PeachPuff": hex_to_rgb("#FFDAB9"),
    "PaleGoldenrod": hex_to_rgb("#EEE8AA"),
    "Khaki": hex_to_rgb("#F0E68C"),
    "DarkKhaki": hex_to_rgb("#BDB76B"),
    "Lavender": hex_to_rgb("#E6E6FA"),
    "Thistle": hex_to_rgb("#D8BFD8"),
    "Plum": hex_to_rgb("#DDA0DD"),
    "Violet": hex_to_rgb("#EE82EE"),
    "Orchid": hex_to_rgb("#DA70D6"),
    "Fuchsia": hex_to_rgb("#FF00FF"),
    "Magenta": hex_to_rgb("#FF00FF"),
    "MediumOrchid": hex_to_rgb("#BA55D3"),
    "MediumPurple": hex_to_rgb("#9370DB"),
    "RebeccaPurple": hex_to_rgb("#663399"),
    "BlueViolet": hex_to_rgb("#8A2BE2"),
    "DarkViolet": hex_to_rgb("#9400D3"),
    "DarkOrchid": hex_to_rgb("#9932CC"),
    "DarkMagenta": hex_to_rgb("#8B008B"),
    "Purple": hex_to_rgb("#800080"),
    "Indigo": hex_to_rgb("#4B0082"),
    "SlateBlue": hex_to_rgb("#6A5ACD"),
    "DarkSlateBlue": hex_to_rgb("#483D8B"),
    "MediumSlateBlue": hex_to_rgb("#7B68EE"),
    "GreenYellow": hex_to_rgb("#ADFF2F"),
    "Chartreuse": hex_to_rgb("#7FFF00"),
    "LawnGreen": hex_to_rgb("#7CFC00"),
    "Lime": hex_to_rgb("#00FF00"),
    "LimeGreen": hex_to_rgb("#32CD32"),
    "PaleGreen": hex_to_rgb("#98FB98"),
    "LightGreen": hex_to_rgb("#90EE90"),
    "MediumSpringGreen": hex_to_rgb("#00FA9A"),
    "SpringGreen": hex_to_rgb("#00FF7F"),
    "MediumSeaGreen": hex_to_rgb("#3CB371"),
    "SeaGreen": hex_to_rgb("#2E8B57"),
    "ForestGreen": hex_to_rgb("#228B22"),
    "Green": hex_to_rgb("#008000"),
    "DarkGreen": hex_to_rgb("#006400"),
    "YellowGreen": hex_to_rgb("#9ACD32"),
    "OliveDrab": hex_to_rgb("#6B8E23"),
    "Olive": hex_to_rgb("#808000"),
    "DarkOliveGreen": hex_to_rgb("#556B2F"),
    "MediumAquamarine": hex_to_rgb("#66CDAA"),
    "DarkSeaGreen": hex_to_rgb("#8FBC8B"),
    "LightSeaGreen": hex_to_rgb("#20B2AA"),
    "DarkCyan": hex_to_rgb("#008B8B"),
    "Teal": hex_to_rgb("#008080"),
    "Aqua": hex_to_rgb("#00FFFF"),
    "Cyan": hex_to_rgb("#00FFFF"),
    "LightCyan": hex_to_rgb("#E0FFFF"),
    "PaleTurquoise": hex_to_rgb("#AFEEEE"),
    "Aquamarine": hex_to_rgb("#7FFFD4"),
    "Turquoise": hex_to_rgb("#40E0D0"),
    "MediumTurquoise": hex_to_rgb("#48D1CC"),
    "DarkTurquoise": hex_to_rgb("#00CED1"),
    "CadetBlue": hex_to_rgb("#5F9EA0"),
    "SteelBlue": hex_to_rgb("#4682B4"),
    "LightSteelBlue": hex_to_rgb("#B0C4DE"),
    "PowderBlue": hex_to_rgb("#B0E0E6"),
    "LightBlue": hex_to_rgb("#ADD8E6"),
    "SkyBlue": hex_to_rgb("#87CEEB"),
    "LightSkyBlue": hex_to_rgb("#87CEFA"),
    "DeepSkyBlue": hex_to_rgb("#00BFFF"),
    "DodgerBlue": hex_to_rgb("#1E90FF"),
    "CornflowerBlue": hex_to_rgb("#6495ED"),
    "MediumSlateBlue": hex_to_rgb("#7B68EE"),
    "RoyalBlue": hex_to_rgb("#4169E1"),
    "Blue": hex_to_rgb("#0000FF"),
    "MediumBlue": hex_to_rgb("#0000CD"),
    "DarkBlue": hex_to_rgb("#00008B"),
    "Navy": hex_to_rgb("#000080"),
    "MidnightBlue": hex_to_rgb("#191970"),
    "Cornsilk": hex_to_rgb("#FFF8DC"),
    "BlanchedAlmond": hex_to_rgb("#FFEBCD"),
    "Bisque": hex_to_rgb("#FFE4C4"),
    "NavajoWhite": hex_to_rgb("#FFDEAD"),
    "Wheat": hex_to_rgb("#F5DEB3"),
    "BurlyWood": hex_to_rgb("#DEB887"),
    "Tan": hex_to_rgb("#D2B48C"),
    "RosyBrown": hex_to_rgb("#BC8F8F"),
    "SandyBrown": hex_to_rgb("#F4A460"),
    "Goldenrod": hex_to_rgb("#DAA520"),
    "DarkGoldenrod": hex_to_rgb("#B8860B"),
    "Peru": hex_to_rgb("#CD853F"),
    "Chocolate": hex_to_rgb("#D2691E"),
    "SaddleBrown": hex_to_rgb("#8B4513"),
    "Sienna": hex_to_rgb("#A0522D"),
    "Brown": hex_to_rgb("#A52A2A"),
    "Maroon": hex_to_rgb("#800000"),
    "White": hex_to_rgb("#FFFFFF"),
    "Snow": hex_to_rgb("#FFFAFA"),
    "Honeydew": hex_to_rgb("#F0FFF0"),
    "MintCream": hex_to_rgb("#F5FFFA"),
    "Azure": hex_to_rgb("#F0FFFF"),
    "AliceBlue": hex_to_rgb("#F0F8FF"),
    "GhostWhite": hex_to_rgb("#F8F8FF"),
    "WhiteSmoke": hex_to_rgb("#F5F5F5"),
    "Seashell": hex_to_rgb("#FFF5EE"),
    "Beige": hex_to_rgb("#F5F5DC"),
    "OldLace": hex_to_rgb("#FDF5E6"),
    "FloralWhite": hex_to_rgb("#FFFAF0"),
    "Ivory": hex_to_rgb("#FFFFF0"),
    "AntiqueWhite": hex_to_rgb("#FAEBD7"),
    "Linen": hex_to_rgb("#FAF0E6"),
    "LavenderBlush": hex_to_rgb("#FFF0F5"),
    "MistyRose": hex_to_rgb("#FFE4E1"),
    "Gainsboro": hex_to_rgb("#DCDCDC"),
    "LightGray": hex_to_rgb("#D3D3D3"),
    "Silver": hex_to_rgb("#C0C0C0"),
    "DarkGray": hex_to_rgb("#A9A9A9"),
    "Gray": hex_to_rgb("#808080"),
    "DimGray": hex_to_rgb("#696969"),
    "LightSlateGray": hex_to_rgb("#778899"),
    "SlateGray": hex_to_rgb("#708090"),
    "DarkSlateGray": hex_to_rgb("#2F4F4F"),
    "Black": hex_to_rgb("#000000")
}

# Processar cada imagem no diretório de origem
for filename in os.listdir(src_dir):
    if filename.endswith(".png"):
        img_path = os.path.join(src_dir, filename)
        img = Image.open(img_path).convert("RGBA")
        
        # Criar diretórios de cores no diretório B e salvar imagens alteradas
        for color in colors:
            new_dir = os.path.join(dst_dir, color)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            new_img = change_image_color(img.copy(), color_map[color])
            new_img_path = os.path.join(new_dir, filename)
            new_img.save(new_img_path)

print("Processo concluído!")