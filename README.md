# 🚦 Traffic Light Decision Controller

## Project Title
**Traffic Light Decision Controller** — EEE120 Digital Design Fundamentals Final Project
### Github Repository: https://github.com/UsmonMD/EEE120_Final_Project_Group_4
---

## Group Members

| Name | Student ID | Role |
|------|-----------|------|
| [Usmon Shamirzayev] | [b251359] | Logic Designer + CircuitVerse Designer + Python Developer + Documentation Lead + Presentation Maker |
| [Elmurodov Dilmurod] | [b250615] | Presenter |
| [Raxmanov Ibrohim] | [b250564] | Presenter |
| [Feruz Nasrullayev] | [b251273] | Presenter |

---

## Course
**EEE120 — Digital Design Fundamentals**
**Instructor:** Dr. Rajan Tripathi
**Group:** Group 4

---

## Problem Statement

Modern urban traffic intersections require efficient and reliable control systems to ensure safety and reduce congestion. In many cities, especially at smaller road crossings, traffic flow is often managed using simple rule-based systems. However, without proper prioritization of different situations — such as emergency vehicles, pedestrian crossings, and varying traffic conditions — these systems can lead to unnecessary delays, traffic buildup, and even dangerous situations.

This project focuses on designing a **combinational logic-based traffic signal controller** that simulates how such intersections can be managed intelligently. The system takes four real-time inputs: presence of vehicles on the main road, presence of vehicles on the side road, pedestrian crossing requests, and detection of emergency vehicles.

Based on these inputs, the controller generates three outputs that determine which traffic signal should turn green and whether pedestrians are allowed to cross. The design ensures that emergency situations are handled with highest priority, pedestrian safety is maintained, and traffic flow is optimized under normal conditions.

This type of system reflects real-world applications used in urban environments to improve traffic efficiency, enhance road safety, and reduce waiting times at intersections.

---

## Inputs

| Input | Symbol | Description |
|-------|--------|-------------|
| Main road traffic present | M | 1 = vehicles detected, 0 = no vehicles |
| Side road traffic present | S | 1 = vehicles detected, 0 = no vehicles |
| Pedestrian button pressed | P | 1 = button pressed, 0 = not pressed |
| Emergency vehicle detected | E | 1 = emergency vehicle nearby, 0 = none |

---

## Outputs

| Output | Symbol | Description |
|--------|--------|-------------|
| Main road signal | Main_Green | 1 = Green, 0 = Red |
| Side road signal | Side_Green | 1 = Green, 0 = Red |
| Pedestrian crossing | Ped_Walk | 1 = Allowed, 0 = Not allowed |

---

## Digital Logic Explanation

The system uses **combinational logic** — outputs depend only on current inputs (no memory/clock needed).

### Boolean Expressions

```
Main_Green = NOT_E · NOT_P · (M + NOT_S)
Side_Green = NOT_E · NOT_M · NOT_P · S
Ped_Walk   = NOT_E · P
```

### Priority Rules (from high to low)
1. **Emergency (E=1)** → Always Main Green, everything else OFF
2. **Pedestrian (P=1, E=0)** → Ped Walk allowed, both roads RED
3. **Side only (S=1, M=0, P=0, E=0)** → Side Green
4. **Default** → Main Green (main road gets priority)

### Logic Gates Used
- NOT gates: 3 (for E, M, P)
- AND gates: 4
- OR gates: 4
- **Total: 11 gates** (exceeds minimum requirement of 5)


### Truth Table 

| M | S | P | E | MAIN | SIDE | PED |
| - | - | - | - | ---- | ---- | --- |
| 0 | 0 | 0 | 0 | 1    | 0    | 0   |
| 0 | 0 | 0 | 1 | 0    | 0    | 0   |
| 0 | 0 | 1 | 0 | 0    | 0    | 1   |
| 0 | 0 | 1 | 1 | 0    | 0    | 0   |
| 0 | 1 | 0 | 0 | 0    | 1    | 0   |
| 0 | 1 | 0 | 1 | 0    | 0    | 0   |
| 0 | 1 | 1 | 0 | 0    | 0    | 1   |
| 0 | 1 | 1 | 1 | 0    | 0    | 0   |
| 1 | 0 | 0 | 0 | 1    | 0    | 0   |
| 1 | 0 | 0 | 1 | 0    | 0    | 0   |
| 1 | 0 | 1 | 0 | 0    | 0    | 1   |
| 1 | 0 | 1 | 1 | 0    | 0    | 0   |
| 1 | 1 | 0 | 0 | 1    | 0    | 0   |
| 1 | 1 | 0 | 1 | 0    | 0    | 0   |
| 1 | 1 | 1 | 0 | 0    | 0    | 1   |
| 1 | 1 | 1 | 1 | 0    | 0    | 0   |


## CircuitVerse Link

🔗 [CircuitVerse Simulation Link](https://circuitverse.org/users/426843/projects/eee120_final_group4)

---

## Python Program Explanation

The Python program in `src/main.py` simulates the exact same Boolean logic as the digital circuit.

### Features
- **Interactive mode**: User enters 4 inputs manually
- **Truth table mode**: Automatically runs all 16 input combinations
- **Clear output**: Shows signal status with emoji indicators
- **Reason display**: Explains *why* a particular signal was chosen

### How to Run
```bash
python3 src/main.py
```

### Requirements
- Python 3.6+
- No external libraries needed

---

## How AI/LLM Was Used

We used **Claude (Anthropic)** as an AI assistant during this project:

| Task | What AI helped with | What we understood & verified |
|------|--------------------|-----------------------------|
| Output formatting | Helped improve readability and clarity of program output | We adjusted the output to clearly display signal states and meanings |
| Code comments & explanation | We provided our code to AI, and it generated structured comments explaining each part | We reviewed all comments and made sure they correctly describe the logic |
| Debugging & problem solving | Assisted when we faced issues with Python syntax and logic errors during development | We tested each fix ourselves and verified correctness through multiple test cases |
| Presentation preparation | Helped structure and format the presentation slides | We reviewed, edited, and ensured the presentation reflects our actual project and understanding |

**AI was not used to fully make the project**

---

## Screenshots

| File | Description |
|------|-------------|
| `screenshots/circuit_design.png` | CircuitVerse circuit screenshot |
| `screenshots/python_output.png` | Python program running in terminal |

---

## Future Improvements

1. Add a **timer-based** sequential controller (flip-flops for timed phases)
2. **LCD display output** showing countdown timer
3. Extend to **4-way intersection** with more inputs
4. Add **night mode** (flashing yellow when traffic is low)
5. Implement with **Arduino/Raspberry Pi** for physical demo

---

## Repository Structure

```
EEE120_Final_Project_Group4/
│
├── README.md
├── circuitverse_link.txt
├── screenshots/
│   ├── circuit_design.png
│   └── python_output.png
│
├── src/
│   └── main.py
│
├── presentation/
│   └── final_presentation.pdf
│
└── demo_video_link.txt
```
