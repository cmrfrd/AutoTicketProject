#AutoTicket

##As of July 2015 NSLIJ has changed their ticketing service.
###As a result this program will not work

Hello! This is the README.md document for AutoTicket.

By: Alexander Comerford
Email: acomerford@sunypoly.edu

#Description:
-These pieces of software are meant to automate the ticketing process of CA Service Desk Manager via
 a simple api for users to create Change Orders and Incidents.

#What AutoTicket can do (and how it should be used):

1. Create Incidents and Change Orders via script or text file
2. Create multiple tickets at once
3. Create "scheduled" tickets that need to be made weekly or daily

#What AutoTicket cannot do (and how it shouldn't be used):

1. Replace CA Service Desk Manager website
2. Make all tickets via AutoTicket


Main Purpose: Auto Create repetative tickets

Usage:
-Create new programs to automate new repetative tasks
-Load commands into a text file to be read and excecuted

Technical Information about AutoTicket:

Programs are written in the Python programming language version 2.7.10 see ==> https://www.python.org/downloads/
Multiple libraries are required. 

Requirements: selenium, pywin32, psutil, pywinauto,


Fields that can be filled on ticket:

-Requester
-affected_user
-category
-status
-source
-location
-department
-email
-phone
-FOC
-assignee
-group
-impact
-priority
-start_date
-call_back_date
-root_cause
-extenal_system_ticket
-clarity_project_num
-order_summary
-order_description

##Text file orders:

#Format for text file input
```
Number Tickets: <number>       <== number of tickets

Constants:                     <== constant values for each ticket
<field1>,<value1>
<field2>,<value2>
...

Fields:			 <== Fields for each ticket to be filled
<field1>,<field2>,<field3>,...

Values:			 <== Value associated for each field
<value1>,<value2>,<value3>,...
<value1>,<value1>,<value1>,...
```

