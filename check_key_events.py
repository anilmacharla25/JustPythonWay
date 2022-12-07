import keyboard
mystring=''
while True:
    # Wait for the next event.
    
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        print(event.name)
        mystring=mystring+event.name
        if event.name=='z':
            print(mystring)
        
####        print(type(event.name))
##        if event.name=='z':
##            break
##        else:
##            letter=event.name
##            key_events_list+=letter
##            print(key_events_list )
##print('-------------------------------------------')
##print(key_events_list )
