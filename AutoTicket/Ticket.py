from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import WebDriverException

class Ticket:
    class Change(object):
        def __init__(self, desk, window):
            self.desk = desk
            self.window = window
            #self.number = self.get_number()
            
        def get_number(self):
            '''gets the change order number'''
            self.desk._navigate_frame("cai_main")
            element = self.desk.driver.get_element_by_xpath('//*[@id="scrollbarDiv0"]/center/div[2]/table/tbody/tr/td[1]/h2')
            text = driver.execute_script("""
                                         return jQuery(arguments[0]).contents().filter(function() {
                                            return this.nodeType == Node.TEXT_NODE;
                                         }).text();
                                         """, element)
            self.number = tect.split()[-1]
            print self.number

        def set_all(self, info_dict):
            self.desk._navigate_frame("cai_main")
            for key in info_dict.keys():
                if key == "requester":self.set_requester(info_dict[key])
                elif key == "affected_user":self.set_affected_user(info_dict[key])
                elif key == "category":self.set_category(info_dict[key])
                elif key == "status":self.set_status(info_dict[key])
                elif key == "source":self.set_source(info_dict[key])
                elif key == "location":self.set_location(info_dict[key])
                elif key == "department":self.set_department(info_dict[key])
                elif key == "email":self.set_email(info_dict[key])
                elif key == "phone":self.set_phone(info_dict[key])
                elif key == "FOC":self.set_FOC(info_dict[key])
                elif key == "assignee":self.set_assignee(info_dict[key])
                elif key == "group":self.set_group(info_dict[key])
                elif key == "impact":self.set_impact(info_dict[key])
                elif key == "priority":self.set_priority(info_dict[key])
                elif key == "start_date":self.set_start_date(info_dict[key])
                elif key == "call_back_date":self.set_call_back_date(info_dict[key])
                elif key == "root_cause":self.set_root_cause(info_dict[key])
                elif key == "external_system_ticket":set_external_system_ticket(info_dict[key])
                elif key == "clarity_project_num":self.set_clarity_project_num(info_dict[key])
                elif key == "order_summary":self.set_order_summary(info_dict[key])
                elif key == "order_description":self.set_order_description(info_dict[key])
                else:None   
            
        def set_requester(self, data):
            '''sets the requester field with data provided'''
            self.desk._set_element_value("df_0_0", data)
            #sets elements value
            
        def set_affected_user(self, data):
            '''sets the affected_user field with data provided'''
            self.desk._set_element_value("df_0_1", data)

        def set_category(self, data):
            '''sets the category field with data provided'''
            self.desk._send_key_to_id("df_0_2", data)
            
        def set_status(self, data):
            '''sets the status field with data provided'''
            self.desk._set_element_value("df_0_3", data)
            
        def set_source(self, data):
            '''sets the source field with data provided'''
            #self.desk.driver.switch_to_default_content()
            #self.desk._navigate_frame('cai_main')
            try:
                inputElement = Select(self.desk.driver.find_element_by_id("df_0_4"))
                inputElement.select_by_visible_text(data)
            except NoSuchElementException:
                pass        
            
        def set_location(self, data):
            '''sets the location field with data provided'''
            self.desk._set_element_value("df_1_0", data)

        def set_department(self, data):
            '''sets the department field with data provided'''
            self.desk._set_element_value("df_1_1", data)

        def set_email(self, data):
            '''sets the email field with data provided'''
            self.desk._set_element_value("df_1_2", data)
        
        def set_phone(self, data):
            '''sets the v field with data provided'''
            self.desk._set_element_value("df_1_3", data)
            
        def set_FOC(self, data):
            '''sets the FOC field with data provided'''
            self.desk._set_element_value("df_1_4", data)

        def set_assignee(self, data):
            '''sets the asignee field with data provided'''
            self.desk._set_element_value("df_2_1", data)
            
        def set_group(self, data):
            '''sets the group field with data provided'''
            #self.desk.driver.switch_to_default_content()
            #self.desk._navigate_frame('cai_main')
            self.desk._send_key_to_id("df_2_2", data)
            
        def set_impact(self, data):
            '''sets the impact level'''
            self.desk._set_element_value("df_2_3", data)

        def set_priority(self, data):
            '''selects the priority in a drop down menu'''
            try:
                inputElement = Select(self.desk.driver.find_element_by_id("df_2_4"))
                inputElement.select_by_visible_text(data)
            except NoSuchElementException:
                pass

        def set_start_date(self, data):
            '''sets the start date'''
            self.desk._set_element_value("df_3_0", data)

        def set_call_back_date(self, data):
            '''sets the call back date'''
            self.desk._set_element_value("df_3_1_hdn", data)

        def set_root_cause(self, data):
            '''sets the start date'''
            self.desk._set_element_value("df_3_2", data)

        def set_external_system_ticket(self, data):
            '''sets the clarity project number'''
            self.desk._set_element_value("df_3_3", data)

        def set_clarity_project_num(self, data):
            '''sets the clarity project number'''
            self.desk._set_element_value("df_3_4", data)

        def set_order_summary(self, data):
            '''sets the order summary'''
            self.desk._set_element_value("df_4_0", data)

        def set_order_description(self, data):
            '''sets the order description'''
            #self.desk.driver.switch_to_default_content()
            #self.desk._navigate_frame('cai_main')
            self.desk._send_key_to_id("df_5_0", data)
