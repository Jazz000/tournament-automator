import random

def run_bracket_generator():
    """
    A professional-grade tournament bracket generator.
    Handles any number of teams and automatically manages 'Byes'.
    """
    print("========================================")
    print("   UNIVERSAL TOURNAMENT AUTOMATOR")
    print("========================================\n")
    
    teams = []
    
    # Step 1: Collect team names dynamically
    while True:
        entry = input("Enter team/player name (or type 'done' to finish): ").strip()
        
        if entry.lower() == 'done':
            break
        
        if entry != "":
            teams.append(entry)
        else:
            print("Name cannot be empty!")

    # Step 2: Validation
    num_teams = len(teams)
    if num_teams < 2:
        print("\nError: You need at least 2 participants for a bracket.")
        return

    # Step 3: Randomize for fairness (Seeding)
    print(f"\nRandomizing seeds for {num_teams} entries...")
    random.shuffle(teams)

    # Step 4: Logic for Odd Numbers (The "Bye" System)
    # If the number of teams is odd, the last team gets a 'Bye' (auto-advance)
    has_bye = False
    if num_teams % 2 != 0:
        has_bye = True
        bye_team = teams.pop() # Remove the last team to give them the Bye

    # Step 5: Generate and Display Matchups
    print("\n" + "—" * 40)
    print("           GENERATED MATCHUPS")
    print("—" * 40)

    # Loop through the list two teams at a time
    match_count = 1
    for i in range(0, len(teams), 2):
        print(f"Match {match_count}: {teams[i]} vs. {teams[i+1]}")
        match_count += 1

    if has_bye:
        print(f"Match {match_count}: {bye_team} [BYE - Advances to next round]")

    print("—" * 40)
    print("\nTournament successfully initialized. Good luck!")

if __name__ == "__main__":
    run_bracket_generator()
