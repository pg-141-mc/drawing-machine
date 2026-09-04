from turtle import *
def t_control(do, val):
    do = do.upper()
    if do=='F':
        forward(val)
    elif do=='B':
        backward(val)
    elif do=='R':
        right(val)
    elif do=='L':
        left(val)
    elif do=='U':
        penup()
    elif do=='D':
        pendown()
    elif do=='N':
        reset()
    else:
        print('Unrecognised command')
def string_artist(program):
    cmd_list=program.split('-')
    for cmd in cmd_list:
        cmd_len=len(cmd)
        if cmd_len==0:
            continue
        cmd_type=cmd[0]
        num=0
        if cmd_len>1:
            num_string=cmd[1:]
            num=int(num_string)
        print(cmd, ':', cmd_type, num)
        t_control(cmd_type, num)
instructions='''Enter a program for the turtle:
eg F100-R45-U-F100-L45-D-F100-R90-B50
N = New drawing
U/D = Pen Up/Down
F__ = Forward __ pixels
B__ = Backward __ pixels
R__ = Right turn __ deg
L__ = Left turn __ deg'''
screen=getscreen()
while True:
    t_prog=screen.textinput('Drawing Machine', instructions)
    print(t_prog)
    if t_prog==None or t_prog.upper()=='END':
        break
    string_artist(t_prog)
        
