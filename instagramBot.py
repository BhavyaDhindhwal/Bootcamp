import os

# Title for console
os.system("title Instagram followers, likes and views botter.")


def validate_url(url: str) -> bool:
    return bool(url) and (url.startswith("http://") or url.startswith("https://"))


def main():
    account_name = input("Account name ? ").strip()
    if account_name == "":
        print("Please input a real name")
        return

    print("Please choose a botter category:")
    print("[1] - Likes")
    print("[2] - Views")
    print("[3] - Followers")

    choose = input("> ").strip()

    if choose == "1":
        url = input("Paste your Instagram post URL (your account needs to be public): ").strip()
        if not validate_url(url):
            print("Cannot find the post (URL must start with http:// or https://)")
            return
        print("Post URL accepted. Bot action removed due to missing dependencies.")

    elif choose == "2":
        url = input("Please input your story URL (must be public and accessible on Instagram web): ").strip()
        if not validate_url(url):
            print("Cannot find the story/account (URL must start with http:// or https://)")
            return
        print("Story URL accepted. Bot action removed due to missing dependencies.")

    elif choose == "3":
        print("Welcome to the followers botter for Instagram")
        print("Please donate $5 to this PayPal to access the follower gen")
        print("https://paypal.me/InstaGenNtrx")
        print("Follower generation logic removed due to missing dependencies.")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()

