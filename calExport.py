from ics import Calendar, Event

c = Calendar()
e = Event()
e.name = "Greg"
e.begin = '2020-01-30 21:30:00'
e.end = '2020-01-30 22:00:00'
c.events.add(e)
c.events
# [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
with open('testCalendar.ics', 'w') as my_file:
     my_file.writelines(c)
