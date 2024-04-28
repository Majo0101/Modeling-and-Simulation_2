class DeviceManager:
      DEV_INIT, DEV_INITALL, DEV_INSERT, DEV_STEP, DEV_REMOVE, DEV_STATE, DEV_PRINT, DEV_PRINTLINE = range(8)
      
      def __init__(self, DEV_TRAN):
            self.devices = [0] * 4
            self.DEV_TRAN = DEV_TRAN

      def device(self, select, mode, steps=0, name="", indent=0):
            if mode == self.DEV_INITALL:
                  for i in range(4):
                        self.devices[i] = 0
                  return 1

            if mode == self.DEV_INSERT:
                  self.devices[select] = steps
                  return 1

            if mode == self.DEV_STEP:
                  if self.devices[select] > 1:
                        self.devices[select] -= 1
                  return self.devices[select]

            if mode == self.DEV_REMOVE:
                  self.devices[select] = 0
                  return 1

            if mode == self.DEV_PRINT:
                  print("\n" + " " * indent + f"{name}: ", end="")
                  if self.devices[select] == 0:
                        print("[empty]")
                  elif self.devices[select] == 1:
                        print("[loaded]")
                  else:
                        print(f"[step {self.devices[select]:2}]")
                  return 1

            if mode == self.DEV_PRINTLINE:
                  print("\n" + " " * indent + f"{name}: ", end="")
                  status = "[empty]  " if self.devices[select] == 0 else "[loaded] " if self.devices[select] == 1 else f"[step{self.devices[select]:2}] "
                  print(status + "_ " * (self.DEV_TRAN - self.devices[select]), end="")
                  if self.devices[select] == 1:
                        print("o ", end="")
                  elif self.devices[select] > 1:
                        print("> " + "_ " * (self.devices[select] - 1))
                  return 1

            return -1
