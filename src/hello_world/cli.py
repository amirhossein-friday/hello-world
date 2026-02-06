"""CLI for hello-world."""

import argparse
import random


GREETINGS = [
    "Hello, {name}!",
    "Hey there, {name}!",
    "What's up, {name}?",
    "Greetings, {name}.",
    "Yo {name}!",
]

FANCY_GREETINGS = [
    "✨ Greetings and salutations, {name}! ✨",
    "🌟 Hello, magnificent {name}! 🌟",
    "⚡ {name}! Great to see you! ⚡",
    "🎉 Well well well, if it isn't {name}! 🎉",
    "💫 The legendary {name} has arrived! 💫",
]


def main():
    parser = argparse.ArgumentParser(description="Greet someone with style.")
    parser.add_argument("--name", default="World", help="Who to greet")
    parser.add_argument("--fancy", action="store_true", help="Enable fancy mode")
    args = parser.parse_args()

    greetings = FANCY_GREETINGS if args.fancy else GREETINGS
    greeting = random.choice(greetings)
    print(greeting.format(name=args.name))


if __name__ == "__main__":
    main()
