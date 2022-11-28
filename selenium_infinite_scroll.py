#infinite scrolling
last_height=driver.execute_script('return document.body.scrollheight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.ScrollHeight)')
    time.sleep(3)
    new_height=driver.execute_script('return document.body.scrollheight')
    if new_height==last_height:
        break
    last_height=new_height
