import argparse
import sys
from typing import Optional

from .extraction import extract_info, get_llm
from .schemas import PersonInfo, MeetingNotes

PERSON_EXAMPLE = (
    "John Doe is a 35-year-old software engineer. "
    "He works at Acme Corp and can be reached at john.doe@example.com. "
    "His phone number is +15551234567 and he lives at 123 Main St, Springfield."
)

MEETING_EXAMPLE = (
    "Team Sync Meeting\n"
    "Date: 2023-09-15\n"
    "Participants: Alice, Bob, Charlie\n"
    "Agenda: Project updates, Budget review, Next sprint planning\n"
    "Decisions: Approved budget increase, Assigned tasks to Bob and Charlie."
)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract structured data from text using LangChain and Pydantic."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-t",
        "--text",
        type=str,
        help="Free‑text input to extract information from.",
    )
    group.add_argument(
        "-e",
        "--example",
        choices=["person", "meeting"],
        help="Use a built‑in example (person or meeting).",
    )
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        default="gpt-3.5-turbo",
        help="OpenAI model name (default: gpt-3.5-turbo).",
    )
    parser.add_argument(
        "-T",
        "--temperature",
        type=float,
        default=0.0,
        help="LLM temperature (default: 0.0).",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()

    if args.example:
        if args.example == "person":
            text = PERSON_EXAMPLE
        else:
            text = MEETING_EXAMPLE
    else:
        text = args.text

    llm = get_llm(model_name=args.model, temperature=args.temperature)

    try:
        result = extract_info(text, llm)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Print the full model dump
    print("\n=== Structured Output ===")
    print(result.model_dump(indent=2))

    # Print a concise summary
    if isinstance(result, PersonInfo):
        summary = f"{result.name}, {result.age} years old, email: {result.email}"
    else:
        summary = f"Meeting '{result.title}' on {result.date} with {len(result.participants)} participants."
    print("\n=== Summary ===")
    print(summary)

if __name__ == "__main__":
    main()
