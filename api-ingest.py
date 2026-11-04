import requests

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    posts = response.json()

    print(f"Total posts fetched: {len(posts)}")

    return posts


if __name__ == "__main__":
    fetch_posts()