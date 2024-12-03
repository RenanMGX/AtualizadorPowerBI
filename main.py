from Entities.web_manipulation import Manipulation
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from time import sleep
import os
import traceback



if __name__ == "__main__":
    try:
        #url = "https://app.powerbi.com/groups/79373af8-3c95-480c-9832-1323fe2c9501/lineage?experience=power-bi"
        #url = "https://app.powerbi.com/groups/01fb58bd-12a1-4105-b916-0ea0fb6874da/list?experience=power-bi"
        url = "https://app.powerbi.com/groups/01fb58bd-12a1-4105-b916-0ea0fb6874da/datasets/94bbba1c-f4a7-494e-b42a-755ac44a7886/details?experience=power-bi"
        
        initial_config = False
        
        if not initial_config:
            
            bot = Manipulation(url=url, visible=False)
            
            #bot.navegador.minimize_window()
            print()
            while True:
                try:
                    bot.navegador.current_url
                    
                except:
                    break
                try:
                    #bot._identifyUpdateButtonBox("Liquidação de Obras").send_keys(Keys.RETURN)
                    bot.atualizar()
                    print(f"{datetime.now().isoformat()} -> clicou <-----------------------------------------------")
                    sleep(2*60)
                except Exception as err:
                    print(f"{datetime.now().isoformat()} -> não clicou <-----------------------------------------------")
                    print(str(err))
                    sleep(10)
                sleep(5)
                #bot.navegador.refresh()
        else:
            
            bot = Manipulation(url=url)
            input("digite para fechar: ")
    
    except Exception as error:
        #import pdb; pdb.set_trace()
        path:str = "logs/"
        if not os.path.exists(path):
            os.makedirs(path)
        file_name = path + f"LogError_{datetime.now().strftime('%d%m%Y%H%M%Y')}.txt"
        with open(file_name, 'w', encoding='utf-8')as _file:
            _file.write(traceback.format_exc())
        raise error
        
        