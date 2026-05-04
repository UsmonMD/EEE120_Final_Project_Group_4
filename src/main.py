"""
Traffic Light Decision Controller
EEE120 Digital Design Fundamentals - Final Project
Group 4:
Usmon Shamirzayev - b251359
Raxmanov Ibrohim - b250564
Feruz Nasrullayev - b251273
Elmurodov Dilmurod - b250615 
"""


def get_input(prompt):
    """Get yes/no input from user, returns 1 or 0"""
    while True:
        val = input(prompt).strip().lower()
        if val in ['1', 'yes', 'y']:
            return 1
        elif val in ['0', 'no', 'n']:
            return 0
        else:
            print("  >> Enter 1/yes or 0/no")


def traffic_logic(M, S, P, E):
    """
    Boolean Logic (matches CircuitVerse circuit):

    Inputs:
      M = Main road traffic present (1=yes, 0=no)
      S = Side road traffic present (1=yes, 0=no)
      P = Pedestrian button pressed  (1=yes, 0=no)
      E = Emergency vehicle detected (1=yes, 0=no)

    Boolean Expressions:
      Main_Green  = E + (NOT E · NOT P · (M + NOT S))
      Side_Green  = NOT E · NOT M · NOT P · S
      Ped_Walk    = NOT E · P

    Logic Gates Used: NOT(x3), AND(x4), OR(x4) = 11 gates total
    """
    NOT_E = 1 - E
    NOT_M = 1 - M
    NOT_S = 1 - S
    NOT_P = 1 - P

    # Gate 1: OR(M, NOT_S)
    g1 = M | NOT_S

    # Gate 2: AND(NOT_E, NOT_P, g1) -> Main without emergency
    g2 = NOT_E & NOT_P & g1

    # Gate 3: Main_Green = E OR g2
    main_green = NOT_E & NOT_P & (M | NOT_S)

    # Gate 4: Side_Green = NOT_E AND NOT_M AND NOT_P AND S
    side_green = NOT_E & NOT_M & NOT_P & S

    # Gate 5: Ped_Walk = NOT_E AND P
    ped_walk = NOT_E & P

    return main_green, side_green, ped_walk


def display_result(M, S, P, E, main_green, side_green, ped_walk):
    print("\n" + "=" * 50)
    print("  TRAFFIC SIGNAL DECISION")
    print("=" * 50)
    print(f"  Inputs:")
    print(f"    M (Main road traffic)  : {'YES' if M else 'NO'}")
    print(f"    S (Side road traffic)  : {'YES' if S else 'NO'}")
    print(f"    P (Pedestrian button)  : {'YES' if P else 'NO'}")
    print(f"    E (Emergency vehicle)  : {'YES' if E else 'NO'}")
    print("-" * 50)
    print(f"  Outputs:")

    main_status = "🟢 GREEN" if main_green else "🔴 RED"
    side_status = "🟢 GREEN" if side_green else "🔴 RED"
    ped_status = "✅ ALLOWED" if ped_walk else "🚫 NOT ALLOWED"

    print(f"    Main Road Signal       : {main_status}")
    print(f"    Side Road Signal       : {side_status}")
    print(f"    Pedestrian Crossing    : {ped_status}")
    print("=" * 50)

    # Explain reason
    if E:
        print("  ⚠️  EMERGENCY MODE: Emergency vehicle detected!")
        print("      ALL SIGNALS RED. Intersection cleared.")
    elif ped_walk:
        print("  🚶 PEDESTRIAN PHASE: Pedestrian button was pressed.")
    elif side_green:
        print("  ↗️  SIDE ROAD PHASE: No main traffic, side road gets green.")
    else:
        print("  ➡️  MAIN ROAD PHASE: Normal traffic flow.")
    print()


def run_test_cases():
    """Run all 16 possible input combinations as automated test"""
    print("\n" + "=" * 60)
    print("  TRUTH TABLE - All 16 Input Combinations")
    print("=" * 60)
    print(f"  {'M':<4}{'S':<4}{'P':<4}{'E':<6}| {'Main':<8}{'Side':<8}{'Ped'}")
    print("-" * 60)
    for E in range(2):
        for M in range(2):
            for S in range(2):
                for P in range(2):
                    mg, sg, pw = traffic_logic(M, S, P, E)
                    print(f"  {M:<4}{S:<4}{P:<4}{E:<6}| {mg:<8}{sg:<8}{pw}")
    print("=" * 60)


def main():
    print("=" * 50)
    print("  TRAFFIC LIGHT DECISION CONTROLLER")
    print("  EEE120 Final Project - Group 4")
    print("=" * 50)

    while True:
        print("\nMENU:")
        print("  1. Enter road conditions manually")
        print("  2. Run automated truth table test")
        print("  3. Exit")

        choice = input("\nChoose (1/2/3): ").strip()

        if choice == '1':
            print("\nEnter road conditions (1=Yes, 0=No):")
            M = get_input("  Main road has traffic?      : ")
            S = get_input("  Side road has traffic?      : ")
            P = get_input("  Pedestrian button pressed?  : ")
            E = get_input("  Emergency vehicle detected? : ")

            main_green, side_green, ped_walk = traffic_logic(M, S, P, E)
            display_result(M, S, P, E, main_green, side_green, ped_walk)

        elif choice == '2':
            run_test_cases()

        elif choice == '3':
            print("\n  Bye! Stay safe at intersections 🚦\n")
            break
        else:
            print("  Invalid choice, try again.")


if __name__ == "__main__":
    main()