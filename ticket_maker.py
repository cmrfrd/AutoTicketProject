from AutoTicket import *


info_dict = {
            'affected_user':"Vora, Vagmin",
            'requester':"Vora, Vagmin",
            'category':r"%Access SCM",
            'source':"E-Mail",
            'location':"Manhasset Main - 300",
            'phone':"555-5555",
            'FOC':"123456789",
            'group':"SCM - Helpdesk Support",
            'order_summary':"Jim Brown Report - 1234  Vora, Vagmin",
            'order_description':"Jim Brown Report - 1234  Vora, Vagmin"
        }

desk = ServiceDesk(visible=True)
desk.log_in("acomerford","Alexander4!")

print "logged in"

desk.create_new_change()

print "Change Made"

desk.navigate_ticket(0).set_all(info_dict)

print "Made Ticket"

raw_input("======Hit Enter to end======")

desk.tear_down()


