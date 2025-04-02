import os
from scrapfly import Scrapfly, ScrapeConfig
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
SCRAPFLY_API_KEY = os.getenv("SCRAPFLY_API_KEY")

# Initialisation Scrapfly
scrapfly = Scrapfly(key=SCRAPFLY_API_KEY)

def scrape_tiktok_profile(username):
    url = f"https://www.tiktok.com/@{username}"
    
    # Configuration de la requête avec rendu JavaScript (TikTok est dynamique)
    config = ScrapeConfig(url=url, render_js=True)
    
    # Envoi de la requête
    response = scrapfly.scrape(config)
    
    # Affichage du contenu brut (à parser ensuite)
    print(response.content)

    return response.content

if __name__ == "__main__":
    profile = scrape_tiktok_profile("tiktok")
