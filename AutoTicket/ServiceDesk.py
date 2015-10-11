import pip

try:
    import psutil
except ImportError:
    print "psutil not found, Importing from PYPI now"
    pip.main(["install", "psutil"])
    import psutil
    
try:
    import pywinauto
except ImportError:
    print "pywinauto not found Import from pypi now"
    pip.main(['install', 'http://sourceforge.net/projects/pywinauto/files/latest/download'])
    import pywinauto

try:
    import selenium
except ImportError:
    print "pywinauto not found Import from pypi now"
    pip.main(['install', 'selenium'])
    import selenium

try:
    import win32gui
except:
    print "config is messed up"
    import shutil
    import os
    def find(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
    dest = "C:\\python27\\Lib\\site-packages\\win32"
    shutil.move(find("pywintypes27.dll", "C:\\python27"), dest)
    shutil.move(find("pywincom27.dll", "C:\\python27"), dest)
    try:
        import win32gui
    except ImportError:
        print "well idk whats wrong.... call alex and have him debug"
print "All requirements satisfied"


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import WebDriverException

from time import sleep
from pywinauto import findwindows
import win32gui
import psutil
import os

from .Ticket import Ticket

class ServiceDesk(object):
    '''
    This class is designed for automating ticket submission
    in Unicenter Service Desk web application

    ***NOTE***
    With no feasible way to get access to an API or back end server
    I must resort to navigating the site manually.

    This class is not going to be a full API for Unicenter Service Desk
    but a simple tool designed to accomplish a small set of tasks

    I assume this is a node.js application based upon it's structure or
    some back end custom framework. Idk all I know is no one knows anything...
    '''
    def __init__(self, visible = True):

        self.visible = visible
        self.is_log_in = False
        #^by default make visible
        
        #for key, value in styles.iteritems():
        #    setattr(self, key, value)
        #^set attributes

        if self.visible:
            self._launch_visible()
        else:
            self._launch_invisible()
        #^launches visible or invisible based on user preference
        
        self.main_window = self.driver.current_window_handle
        self.driver.get("http://sykpcasd12sb1v/CAisd/pdmweb.exe")
        #^goes to CA website

        self.tickets = []
        #^ticket creation

    def log_in(self, username, password):
        '''logs into CA with defined username and password'''

        if self.is_log_in == True:
            print "Already logged in"
            return False
        #^prevents user from loggin on twice

        if type(username) != str or type(password) != str:
            print "Username or password must be string"
            return False
        #^makes sure input is valid
        
        try:
            username_element = self.driver.find_element_by_id("USERNAME")
            password_element = self.driver.find_element_by_id("PIN")
            #^get's log_in necessary elements

            username_element.send_keys(username)
            password_element.send_keys(password)
            #^sends keystrokes to those elements

            self.driver.find_element_by_id("imgBtn0").click()
            #clicks log in 

            self.log_in = True
            return True            
        except NoSuchElementException:
            print "Unable to find 'User Name' or 'password' or 'log in'"
            return False    

    def navigate_ticket(self, ticket_num=0):
        '''navigates to the first window that's not the main window and returns ticket object'''
        try:
            self.driver.switch_to_window(self.tickets[ticket_num].window)
            #^switches to window by ticket index id
            return self.tickets[ticket_num]
        except NoSuchWindowException:
            print "Invalid window handle"
            return False
        except IndexError:
            print "invalid ticket index"
            return False

    def create_new_change(self):
        '''navigates to service desk -> new change to make a new change order'''
        try:
            self.driver.switch_to_window(self.driver.window_handles[0])
            self.driver.switch_to_default_content()
            
            self._navigate_frame('toolbar')
            self.driver.find_element_by_id('tabhref0').click()

            self.driver.switch_to_default_content()

            self._navigate_frame('product')
            self._navigate_frame('tab_1003')
            self._navigate_frame('role_main')
            self._navigate_frame('scoreboard')

            handles = len(self.driver.window_handles)#get the number of windows before creatuing a new one

            self.driver.find_element_by_id("imgBtn2").click()

            sleep(1)            
            while len(self.driver.window_handles) == handles:sleep(0.5);print "checking windows"
            sleep(1)
            
            self.tickets.append(Ticket.Change(self, self.driver.window_handles[-1]))
            
            return True
        except:
            print "unable to make change"
            return False
    def create_new_incident(self):
        '''navigates to service desk -> new change to make a new change order'''
        try:
            self.driver.switch_to_default_content()
            
            self._navigate_frame('toolbar')
            self.driver.find_element_by_id('tabhref0').click()

            self.driver.switch_to_default_content()

            self._navigate_frame('product')
            self._navigate_frame('tab_1003')
            self._navigate_frame('role_main')
            self._navigate_frame('scoreboard')

            handles = len(self.driver.window_handles)#get the number of windows before creatuing a new one

            self.driver.find_element_by_id("imgBtn1").click()

            while len(self.driver.window_handles) <= handles:sleep(0.5)
                
            self.tickets.append(Ticket.Change(self, self.driver.window_handles[-1]))
            
            return True
        except:
            print "unable to make incident"
            return False
    def _navigate_frame(self, name):
        '''navigates to a desired frame based on name'''
        if type(name) != str:return False
        #^authenticates input
        
        try:
            frame = self.driver.find_element_by_name(name)
            self.driver.switch_to_frame(frame)
            #^gets the default content of page, switches to frame
            return True
        except NoSuchElementException:
            print "No frame with that name: " + str(name)
            return False

    def _send_key_to_id(self, id, data):
        '''sends keystrokes to an element with specific id'''

        if type(id) != str or type(data) != str:
            print "both inputs must be strings"
            return False
        #^makes sure input is valid
        
        try:
            element = self.driver.find_element_by_id(id)
            element.send_keys(data)
            return True
        except NoSuchElementException:
            print "Element with id cannot be found"
            print id
            return False

    def _set_element_value(self, id, data):
        
        if type(id) != str or type(data) != str:
            print "both inputs must be strings"
            return False
        
        try:
            self.driver.execute_script("document.getElementById(\'"+id+"\') \
                                     .setAttribute('value', \'"+data+"\')");
            return True
        except WebDriverException:
            print "invalid data or id"
            print id
            return False

    def _click_element(self, id):
        self.driver.find_element_by_id(id).click()
        return True
    
    def _launch_visible(self):
        '''launches chrome visible to user SHOULD ONLY BE USED ONCE'''
        try:
            #this_dir, this_filename = os.path.split(__file__)
            #DATA_PATH = os.path.join(this_dir, "drivers", "chromedriver.exe")
            DATA_PATH = r"drivers\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = DATA_PATH
            self.driver = webdriver.Chrome(DATA_PATH)
            #^launch selenium with chrome and adds driver to class
            return True
        except:
            return False
        
    def _launch_invisible(self):
        '''launches phantom js invisible SHOULD ONLY BE USED ONCE'''
        try:
            DATA_PATH = r"drivers\phantomjs.exe"
            #os.environ["webdriver.chrome.driver"] = DATA_PATH
            #self.driver = webdriver.PhantomJS(DATA_PATH)

            user_agent = (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
            )
            
            dcap = dict(DesiredCapabilities.PHANTOMJS)
            dcap["phantomjs.page.settings.userAgent"] = user_agent

            self.driver = webdriver.PhantomJS(DATA_PATH, desired_capabilities=dcap)
            
            window_h = findwindows.find_windows(title_re = r"*[^^]phantomjs\.exe")
            while len(window_h) == 0:
                window_h = findwindows.find_windows(title_re = r'*[^^]phantomjs\.exe')

            win32gui.ShowWindow(window_h[0], False)
            #launches PhantomJS then makes window invisible
            return True
        except:
            return False
            
    def tear_down(self):
        '''kills CA and ends session'''        
        try:
            for handle in self.driver.window_handles:
               self.driver.switch_to_window(handle)
               sleep(0.5)
               self.driver.close()
            #^kills driver
        except WebDriverException:
            pass

        for proc in psutil.process_iter():#loop through all processes
            try:
                if proc.name() == "phantomjs.exe":proc.kill()#if this process kill it and start a new
                if proc.name() == "chromedriver.exe":proc.kill()
            except:
                None
        #^ends phantom js task

        self.log_in = False
        return True
