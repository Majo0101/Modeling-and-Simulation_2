from event import DeviceManager

# Conveyor length 
TLENGTH = 10 
# CNC machine Time 
WTIME = 5   

def timestep(dev_mgr):
      dev_mgr.device(0, dev_mgr.DEV_STEP)
      dev_mgr.device(1, dev_mgr.DEV_STEP)
      dev_mgr.device(2, dev_mgr.DEV_STEP)
      dev_mgr.device(3, dev_mgr.DEV_STEP)

def printstate(dev_mgr):
      dev_mgr.device(0, dev_mgr.DEV_PRINTLINE, name="transporter1", indent=2)
      dev_mgr.device(1, dev_mgr.DEV_PRINT, name="worktool(a)", indent=25)
      dev_mgr.device(2, dev_mgr.DEV_PRINT, name="worktool(b)", indent=25)
      dev_mgr.device(3, dev_mgr.DEV_PRINTLINE, name="transporter2", indent=2)

def link_control(dev_mgr, command):
      if command == 'i':
            dev_mgr.device(0, dev_mgr.DEV_INSERT, TLENGTH)
      elif command == 't':
            dev_mgr.device(3, dev_mgr.DEV_REMOVE)
      elif command == 'a':
            dev_mgr.device(0, dev_mgr.DEV_REMOVE)
            dev_mgr.device(1, dev_mgr.DEV_INSERT, WTIME)
      elif command == 'b':
            dev_mgr.device(1, dev_mgr.DEV_REMOVE)
            dev_mgr.device(2, dev_mgr.DEV_INSERT, WTIME)
      elif command == 'c':
            dev_mgr.device(2, dev_mgr.DEV_REMOVE)
            dev_mgr.device(3, dev_mgr.DEV_INSERT, TLENGTH)

def automatic_control(dev_mgr):
      """
      - If transporter1 is empty, load it.
      - If transporter1 has finished its steps, move the item to worktool(a) if it's empty.
      - If worktool(a) has finished its steps, move the item to worktool(b) if it's empty.
      - If worktool(b) has finished its steps, move the item to transporter2.
      - If transporter2 is full and finished, unload it.
      """
      # Check transporter1
      if dev_mgr.devices[0] == 0:
            return 'i'  # Command to insert into transporter1

      # Move from transporter1 to worktool(a)
      if dev_mgr.devices[0] == 1 and dev_mgr.devices[1] == 0:
            return 'a'

      # Move from worktool(a) to worktool(b)
      if dev_mgr.devices[1] == 1 and dev_mgr.devices[2] == 0:
            return 'b'

      # Move from worktool(b) to transporter2
      if dev_mgr.devices[2] == 1 and dev_mgr.devices[3] == 0:
            return 'c'

      # Unload transporter2
      if dev_mgr.devices[3] == 1:
            return 't'

      return ''


def main():
      dev_mgr = DeviceManager(TLENGTH)
      dev_mgr.device(0, dev_mgr.DEV_INITALL)
      step = 0
      while True:
            timestep(dev_mgr)
            print(f"\n\n\n  step {step}: ", end="")
            step += 1
            command = input().strip()
            if command == 'e':
                  break
            if command == '':
                  # command = 'automatic_control'  # Manual Control
                  command = automatic_control(dev_mgr)  # Automatic control
            link_control(dev_mgr, command)
            printstate(dev_mgr)

if __name__ == "__main__":
      main()
