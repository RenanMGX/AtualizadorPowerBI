from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getpass import getuser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from typing import List
from time import sleep

def _find_element(*, browser:WebDriver|WebElement, by:str, target:str, timeout:int=15, ignore:bool=False, speak:bool=False) -> WebElement:
    for _ in range(timeout*2):
        try:
            element:WebElement= browser.find_element(by, target)
            print(f"find: {target=}") if speak else None
            return element
        except:
            sleep(0.5)
        
    if ignore:
        print(f"ignore: {target=}") if speak else None
        return browser.find_element(By.TAG_NAME, 'html')
        
    raise Exception(f"Not Found: {target=}")

def _find_elements(*, browser:WebDriver|WebElement, by:str, target:str, timeout:int=15, ignore:bool=False, speak:bool=False) -> List[WebElement]:
    for _ in range(timeout*2):
        try:
            elements:List[WebElement] = browser.find_elements(by, target)
            print(f"find: {target=}") if speak else None
            if len(elements) >= 1:
                return elements
            else:
                raise Exception()
        except:
            sleep(0.5)
        
    if ignore:
        print(f"ignore: {target=}") if speak else None
        return [browser.find_element(By.TAG_NAME, 'html')]
        
    raise Exception(f"Not Found: {target=}")

class Manipulation:
    @property
    def options(self) -> Options:
        return self.__options
    @property
    def navegador(self) -> WebDriver:
        return self.__navegador
    
    def __init__(self, *, url:str="", visible:bool=True) -> None:
        self.__options = webdriver.ChromeOptions()
        self.options.add_argument(f"--user-data-dir=C:\\Users\\{getuser()}\\AppData\\Local\\Google\\Chrome")
        
        if not visible:
            print("invisible")
            self.options.add_argument("--headless")  # Configura o Chrome em modo headless
            self.options.add_argument("--disable-gpu")  # Desativa a GPU (necessário para algumas versões do Windows)
            self.options.add_argument("--window-size=1920x1080")  # Define o tamanho da janela
            self.options.add_argument("--window-position=-2400,-2400")
        else:
            self.options.add_argument("--window-size=1920x1080")
            
        self.__navegador:WebDriver = webdriver.Chrome(options=self.options)
        if url:
            self.navegador.get(url)
        self._verificarLogin()
    
    def restart_browser(self):
        self.navegador.close()
        self.__navegador:WebDriver = webdriver.Chrome(options=self.options)
        return self
    
    def _verificarLogin(self, email:str="renan.oliveira@patrimar.com.br"):
        sleep(5)
        divs:List[WebElement] = _find_elements(browser=self.navegador, by=By.TAG_NAME, target='div')
        for div in divs:
            try:
                attibuteDiv = div.get_attribute("data-test-id")
            except:
                continue
            if attibuteDiv == email:
                div.click()
                return self

    def _identifyUpdateButtonBox(self, name_box:str) -> WebElement:
        
        self._changePreview()
        num_attempts:int = 15
        for num in range(num_attempts):
            try:
                
                
                def search_box_group() -> List[WebElement]:
                    box_group_temp:List[WebElement] = []
                    tags_g:List[WebElement] = _find_elements(browser=self.navegador, by=By.TAG_NAME, target='g')
                    for tag_g in tags_g:
                        #print(g)
                        if tag_g.get_attribute("class") == "node ng-star-inserted":
                            box_group_temp.append(tag_g)
                    return box_group_temp
                
                box_group:List[WebElement] = search_box_group()  
                
                
                box_selected:WebElement
                for box in box_group:
                    if (("Modelo semântico" in box.text) or ("Semantic model" in box.text)) and (name_box in box.text):
                        #pass
                        #print(box.text, end="\n\n")
                        box_selected = box
                
                buttons:List[WebElement] = _find_elements(browser=box_selected, by=By.TAG_NAME, target='button')
                for button in buttons:
                    button:WebElement
                    if button.get_attribute('data-testid') == "refresh-now-btn":
                        #print("\nachou botão")
                        return button
            except Exception as error:
                print(error)
                import traceback
                print(traceback.format_exc())
                print(error) if num >= num_attempts else None
                sleep(5)
        
        raise ValueError(f"Botão não encontrado!")
       
    
    def _changePreview(self) -> None:
        for span in _find_elements(browser=self.navegador, by=By.TAG_NAME, target='span'):
            try:
                attibuteSpan:str|None = span.get_attribute("innerHTML")
            except:
                continue
            if attibuteSpan:
                if "O botão de exibição da lista foi selecionado" in attibuteSpan:
                    for button in _find_elements(browser=self.navegador, by=By.TAG_NAME, target='button'):
                        attibuteButton:str|None = button.get_attribute("data-testid")
                        if attibuteButton:
                            if "LineageView_Switcher" in attibuteButton:
                                button.click()
                                break
                    
    def atualizar(self):
        try:
            andamento = self.navegador.find_element(By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/error-dialog/mat-dialog-actions/section/button')
            andamento.click()
            raise Exception("Atualização em Andamento")
        except NoSuchElementException:
            try:
                _find_element(browser=self.navegador, by=By.XPATH, target='//*[@id="content"]/tri-shell/tri-item-renderer/tri-extension-page-outlet/div[2]/dataset-details-container/dataset-action-bar/action-bar/action-button[2]/button').click()
                _find_element(browser=self.navegador, by=By.XPATH, target='//*[@id="mat-menu-panel-1"]/div/span[1]/button').click()
            except:
                self.navegador.refresh()
                raise Exception("Atualização em Andamento")
        except Exception as err:
            raise err
                    
if __name__ == "__main__":
    pass
