#reads and runs text files for the cration of tickets

def file_exists(name):
    try:
        open(os.path.join("TicketOrders", name))
        return True
    except IOError:
        return False

def valid_format(lines):
    error = [True, "Missing: "]
    if "Number Tickets:" not in str(lines):
        error[0] = False
        error[1] += "Number Tickets: "
    if "Constants:" not in str(lines):
        error[0] = False
        error[1] += "Constants: "
    if "Fields:" not in str(lines):
        error[0] = False
        error[1] += "Fields: "
    if "Values:" not in str(lines):
        error[0] = False
        error[1] += "Values: "
    return error

def chunk_lines(lines):
    find_index = lambda partial, lines:lines.index([i for i in lines if partial == i.strip()][0])

    return_indexs = []        
    return_indexs.append((find_index("Number Tickets:", lines),"Tickets"))
    return_indexs.append((find_index("Constants:", lines), "Constants"))
    return_indexs.append((find_index("Fields:", lines), "Fields"))
    return_indexs.append((find_index("Values:", lines), "Values"))

    return return_indexs

def num_tickets(lines, index):
    try:
        tickets = int(lines[index+1])
        if tickets < 0:raise ValueError("Must be positive")
        return tickets
    except ValueError:
        print "Invalid Number of tickets"
        return 0

def constants(lines, begin, end):
    if begin+1 == end:return None
    return lines[begin+1:end]

def fields(lines, begin, end):
    if begin+1 == end:return None
    return lines[begin+1:end]

def values(lines, begin, end):
    if begin+1 == end:return None
    return lines[begin+1:end]

def main():
    print "Files: \n" + str(os.listdir("TicketOrders"))
    file_name = raw_input("File to excecute in TicketOrders: ")
    while not file_exists(file_name):
        print "Unable to find file"
        file_name = raw_input("File to excecute in TicketOrders: ")
    #^ vaidates the right texfile exists

    order_info = open(os.path.join("TicketOrders", file_name),"r")#file object

    print "Analyzing file"

    lines = order_info.read().split('\n')#list of each line in text file
    lines = filter(lambda x: x.split() != [], lines)

    #print lines######

    valid = valid_format(lines)
    if not valid[0]:print valid[1];return False
    #^validates the text file

    chunks = sorted(chunk_lines(lines))+[[len(lines), "length"]]#chunks appropriately
    data = {}

    #print chunks######

    chunk = 0
    while chunk < len(chunks):      
        if chunks[chunk][1] == "Tickets":
            data['Tickets'] = num_tickets(lines, chunks[chunk][0])
        elif chunks[chunk][1] == "Constants":
            data['Constants'] = constants(lines, chunks[chunk][0], chunks[chunk+1][0])
        elif chunks[chunk][1] == "Fields":
            data['Fields'] = fields(lines, chunks[chunk][0], chunks[chunk+1][0])
        elif chunks[chunk][1] == "Values":
            data['Values'] = values(lines, chunks[chunk][0], chunks[chunk+1][0])
        chunk += 1
    #^inserts appropriate data into a dict for ease of access

    #print data

    if data['Tickets'] == 0:print "0 tickets";return False

    desk = ServiceDesk(visible=True)
    desk.log_in("acomerford","Alexander4!")

    print "logged in"
    
    for ticket in range(data['Tickets']):

        desk.create_new_change()#make the ticket
        
        print "Making ticker: %d" % (ticket)
        insert_data = {}

        for const in data['Constants']:
            const_data = const.split(',')
            insert_data[const_data[0]] = const_data[1].strip().encode('string_escape')
        #inserting constants into insert data

        count = 0
        for field in data['Fields'][0].split(','):
            insert_data[field.strip()] = data['Values'][ticket].split(',')[count].strip()
            count += 1
        #^inserts the fields and values

        desk.navigate_ticket(ticket).set_all(insert_data)

    print "Finished making Tickets"

    raw_input("======Hit Enter to end======")

    desk.tear_down()

if __name__ == "__main__":
    import sys
    import os
    from AutoTicket import *
    main()
