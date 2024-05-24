from Entities.web_manipulation import Manipulation
from datetime import datetime
from time import sleep



if __name__ == "__main__":
    url = "https://app.powerbi.com/groups/79373af8-3c95-480c-9832-1323fe2c9501/lineage?experience=power-bi"
    
    initial_config = False
    
    if not initial_config:
        bot = Manipulation(url=url, visible=False)
        
        print()
        while True:
            try:
                bot.navegador.current_url
            except:
                break
            try:
                bot._identifyUpdateButtonBox("Liquidação de Obras").click()
                print(f"{datetime.now().isoformat()} -> clicou <-----------------------------------------------")
                sleep(2*60)
            except:
                print(f"{datetime.now().isoformat()} -> não clicou <-----------------------------------------------")
                sleep(10)
            #sleep(60)
    else:
        bot = Manipulation(url=url)
        input("digite para fechar: ")