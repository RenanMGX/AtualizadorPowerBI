from Entities.web_manipulation import Manipulation
from datetime import datetime
from time import sleep
import os
import traceback



if __name__ == "__main__":
    try:
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
                sleep(5)
                bot.navegador.refresh()
        else:
            bot = Manipulation(url=url)
            input("digite para fechar: ")
    
    except Exception as error:
        path:str = "logs/"
        if not os.path.exists(path):
            os.makedirs(path)
        file_name = path + f"LogError_{datetime.now().strftime('%d%m%Y%H%M%Y')}.txt"
        with open(file_name, 'w', encoding='utf-8')as _file:
            _file.write(traceback.format_exc())
        raise error
        