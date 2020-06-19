from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

# Parameters
WP_LINK = 'https://web.whatsapp.com'

## XPATHS
# _1U1xa

CONTACTS = '//*[@id="main"]/header/div[2]/div[2]/span'
SEND = '//*[@id="main"]/footer/div[1]/div[3]/button'
MESSAGE_BOX = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
NEW_CHAT = '//*[@id="side"]/header/div[2]/div/span/div[2]/div'
FIRST_CONTACT = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div'
SEARCH_CONTACT ='//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]'
CAMPO_BUSCAR = '//*[@id="side"]/div[1]/div/label/div/div[2]'
UNREAD_CHAT = "//span[@class='_31gEB']/ancestor::div[4]"


class WhatsApp:
    def __init__(self):
        self.driver = self._setup_driver()
        self.driver.get(WP_LINK)
        print("Please scan the QR Code")
    
    
    @staticmethod
    def _setup_driver():
        print('Loading...')
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars") #NAO TA FUNCIONANDO ISSO AQUI
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver

    def _get_element(self, xpath, attempts=5, _count=0):
        '''Safe get_element method with multiple attempts'''
        try:
            element = self.driver.find_element_by_xpath(xpath)
            #print('Found element!')
            return element
        except Exception as e:
            if _count<attempts:
                sleep(1)
                #print(f'Attempt {_count}')
                self._get_element(xpath, attempts=attempts, _count=_count+1)
            else:
                print("Element not found")

    def _click(self, xpath):
        el = self._get_element(xpath)
        el.click()

    def _send_keys(self, xpath, message):
        el = self._get_element(xpath)
        el.send_keys(message)

    def write_message(self, message):
        '''Write message in the text box but not send it'''
        self._click(MESSAGE_BOX)
        self._send_keys(MESSAGE_BOX, message)

    def _paste(self):
        el = self._get_element(MESSAGE_BOX)
        el.send_keys(Keys.SHIFT, Keys.INSERT)

    def teste(self):
        
        self.driver.get(WP_LINK + "/send?phone=+555180403522&text=olapessoa")

    def send_message(self, message):
        '''Write and send message'''
        message = message.rstrip('\n')
        
        if len(message) > 1:
            self.write_message(message)
            print("escreveu")
            self._click(SEND)
            print("clicou em Send")
        # sleep(1)
        # print("esperou")
           
            

    def get_group_numbers(self):
        '''Get phone numbers from a whatsapp group'''
        try:
            el = self.driver.find_element_by_xpath(CONTACTS)
            return el.text.split(',')
        except Exception as e:
            print("Group header not found")

    def espera_abrir_whatsapp(self):
        
        a = 1
        
        while a == 1: 
            try:
                self._click(CAMPO_BUSCAR)
                a = 2
                break
            except Exception: 
                print("Aguardando Abrir")
                sleep(2)

    def search_contact(self, keyword):
        '''Write and send message'''
        self._click(NEW_CHAT)
        self._send_keys(SEARCH_CONTACT, keyword)
        sleep(1)
        self._click(FIRST_CONTACT)
        
        
    def get_all_messages(self):
        all_messages_element = self.driver.find_elements_by_class_name('_12pGw')
        all_messages_text = [e.text for e in all_messages_element]
        return all_messages_text
        
    def get_last_message(self):
        all_messages = self.get_all_messages()
        return all_messages[-1]
    
    def enter_unread_chat(self):
        while True: 
            try:
                el = self.driver.find_element_by_xpath(UNREAD_CHAT)
                # Entra na conversa
                el.click()
                break
            except Exception:
                sleep(5)
                print("Elemento Não Encontrado")
        
        
        