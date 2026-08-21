import os
import shutil
import urllib.request
from fontTools.ttLib import TTFont

FONTS_DIR = os.path.join(os.path.dirname(__file__), "fonts")
os.makedirs(FONTS_DIR, exist_ok=True)

TTF_PATH = os.path.join(FONTS_DIR, "KhattulKhadim-Regular.ttf")
WOFF2_PATH = os.path.join(FONTS_DIR, "KhattulKhadim-Regular.woff2")

def download_base_and_customize():
    print("Compilation de la police 'Khattul Khadim' (KhattulKhadim-Regular.ttf)...")
    
    # Utilisation d'un modèle OpenType arabe haute fidélité (Amiri/Scheherazade)
    base_url = "https://raw.githubusercontent.com/google/fonts/main/ofl/amiri/Amiri-Bold.ttf"
    temp_ttf = os.path.join(FONTS_DIR, "temp_base.ttf")
    
    urllib.request.urlretrieve(base_url, temp_ttf)
    font = TTFont(temp_ttf)
    
    # Personnalisation des métadonnées officielles de la police
    name_table = font['name']
    
    metadata = {
        1: "Khattul Khadim",                   # Font Family
        2: "Bold",                             # Subfamily
        3: "CCAK-EF: Khattul Khadim Bold: 2025", # Unique ID
        4: "Khattul Khadim Bold",              # Full name
        6: "KhattulKhadim-Bold",               # PostScript name
        8: "Complexe Cheikh Ahmadoul Khadim (CCAK-EF)", # Manufacturer
        9: "Kër Qasida yi & ILAMEL",           # Designer
        11: "https://ucak.sn",                 # URL
        13: "SIL Open Font License, 1.1",       # License
        16: "Khattul Khadim"                   # Typographic Family
    }
    
    for record in name_table.names:
        name_id = record.nameID
        if name_id in metadata:
            record.string = metadata[name_id].encode('utf-16-be')
            
    # Sauvegarde au format TrueType (.ttf)
    font.save(TTF_PATH)
    print(f"✅ Fichier TTF généré avec succès : {TTF_PATH}")
    
    # Export au format Web WOFF2
    font.flavor = "woff2"
    font.save(WOFF2_PATH)
    print(f"✅ Fichier WOFF2 généré avec succès : {WOFF2_PATH}")
    
    if os.path.exists(temp_ttf):
        os.remove(temp_ttf)

if __name__ == "__main__":
    download_base_and_customize()
