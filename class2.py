import easygui
#answer = easygui.choicebox(msg='What is your favourite animal?',title='animal',choices=['rabbit','cat','dog'])
a = easygui.passwordbox(msg="your password is",title="Password",default="123456")
easygui.msgbox("your new password is " + a)

#message = "what a pig?"
#title = 'Hello!! Nice to meet you!'
#easygui.textbox(msg = message, title = title, text = 'PIG!!!!')
#easygui.integerbox(msg = message, title = title, default= 50)