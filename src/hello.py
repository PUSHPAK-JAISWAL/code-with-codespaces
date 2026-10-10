def build_greeting(name: str, activity: str) -> str:
    safe_name = (name or "friend").strip() or "friend"
    safe_activity = (activity or "coding").strip() or "coding"
    return (
        f"Hello, {safe_name}! Ready for some {safe_activity} today? "
        "This repo just got a little more interactive."
    )


def main() -> None:
    print("Welcome to this mini interactive repo demo!")
    name = input("What should I call you? ").strip()
    activity = input("What are you in the mood to do today? ").strip()

    print(build_greeting(name, activity))


if __name__ == "__main__":
    main()