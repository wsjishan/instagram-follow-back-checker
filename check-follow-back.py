import json
import os


def load_json_file(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                print(f"Error: {filename} is not valid JSON.")
    else:
        print(f"Error: {filename} not found.")
    return []


followers_data = load_json_file("followers.json")
following_data = load_json_file("following.json")

if followers_data and following_data:
    followers = {item["string_list_data"][0]["value"] for item in followers_data}

    following = {
        item["string_list_data"][0]["value"]: item["string_list_data"][0]["href"]
        for item in following_data["relationships_following"]
    }

    not_following_back = {
        user: following[user] for user in following if user not in followers
    }

    with open("not-following-back.txt", "w", encoding="utf-8") as f:
        if not_following_back:
            f.write(
                f"Count of people who are not following you back: {len(not_following_back)}\n"
            )
            f.write("People who are not following you back:\n")
            for user, url in not_following_back.items():
                f.write(f"{user}: {url}\n")
        else:
            f.write("No users found who are not following you back.\n")

    print(f"Count of people who are not following you back: {len(not_following_back)}")
    print("Check 'not-following-back.txt' for detailed list.")
else:
    with open("not-following-back.txt", "w", encoding="utf-8") as f:
        f.write(
            "Please ensure you have pasted your 'followers.json' and 'following.json' files in the current directory."
        )
    print(
        "Please ensure you have pasted your 'followers.json' and 'following.json' files in the current directory."
    )
