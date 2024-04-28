# Industrial Conveyor Control System

This Python script simulates an industrial environment with conveyor belts and CNC machines. The script defines various devices and controls their operations based on user input or automatic control logic.

## Features

- **Conveyor Control**: Manage two conveyor belts and two work tools (CNC machines) to simulate the movement and processing of items.
- **Automatic and Manual Controls**: The system can operate in automatic mode based on predefined logic or accept manual input from the user to control device operations.
- **Dynamic State Printouts**: Outputs the current state of each device in a formatted console output, reflecting the system's current operational status.

## How to Run

Ensure you have Python 3 installed on your machine, and the script depends on a custom module named `event`, which should define the `DeviceManager` class.

1. Clone the repository or download the script.
2. Navigate to the script's directory.
3. Run the script using Python

## Example Output
```
step 0: i
  transporter1: [step 10] __________________________ o 
  worktool(a): [empty]
  worktool(b): [empty]
  transporter2: [empty] __________________________
```

## Development
This script was developed to demonstrate control logic in an industrial setting. It can be modified to include more devices, enhance logic, or integrate with actual hardware controls.
