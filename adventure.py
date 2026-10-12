def choose(prompt, options):
    """Return a valid numbered choice from the player."""
    while True:
        print(prompt)
        for number, option in enumerate(options, start=1):
            print(f"  {number}. {option}")

        answer = input("> ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer)

        print(f"Please enter a number from 1 to {len(options)}.\n")


def main():
    print("THE MOONLIT TRAIL")
    print("A silver map leads you to the edge of a dark forest.\n")

    path = choose("Which way will you go?", ["Follow the forest path", "Enter the cave"])

    if path == 1:
        forest_choice = choose(
            "A fox with a tiny brass key blocks the trail. What do you do?",
            ["Offer it your lunch", "Walk past and climb the hill"],
        )
        if forest_choice == 1:
            print("\nThe fox takes your lunch, then unlocks a hidden gate. You find a warm cottage and a new friend. THE END.")
        else:
            print("\nAt the hilltop, you watch the moon rise over a sea of clouds. You have found the quietest place in the world. THE END.")
    else:
        cave_choice = choose(
            "The cave splits in two. A blue glow shines from one tunnel; a breeze comes from the other.",
            ["Follow the blue glow", "Follow the breeze"],
        )
        if cave_choice == 1:
            print("\nThe glow leads to a crystal lake. Beneath its surface, you discover a sunken library. THE END.")
        else:
            print("\nThe breeze carries you through the mountain and out beside the map's marked treasure chest. THE END.")


if __name__ == "__main__":
    main()