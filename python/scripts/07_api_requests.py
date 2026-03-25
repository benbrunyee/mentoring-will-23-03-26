# =============================================================================
# API REQUESTS
# Concepts: HTTP requests, JSON, the `requests` library, dictionaries,
#           error handling, status codes, working with real-world data
# =============================================================================
#
# We use JSONPlaceholder (https://jsonplaceholder.typicode.com) — a free,
# public fake REST API that needs no account or API key.
#
# Install the dependency first:  pip install requests
# =============================================================================

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# ---------------------------------------------------------------------------
# API helper functions
# ---------------------------------------------------------------------------

def fetch_posts(limit=5):
    """
    Fetch a list of posts from the API.

    requests.get() sends an HTTP GET request to the URL — the same type
    of request your browser makes when you visit a webpage.

    The API returns data as JSON (a text format that looks like a Python
    dictionary), which requests automatically converts for us.
    """
    url = f"{BASE_URL}/posts"

    # We can pass query parameters as a dictionary.
    # This adds ?_limit=5 to the URL, asking for only 5 results.
    params = {"_limit": limit}

    response = requests.get(url, params=params)

    # HTTP status 200 means "OK". Other common ones:
    #   404 = Not Found, 403 = Forbidden, 500 = Server Error
    response.raise_for_status()  # Raises an exception if there was an error

    return response.json()  # Parse the JSON body into a Python list/dict


def fetch_post(post_id):
    """Fetch a single post by its ID."""
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_comments_for_post(post_id):
    """Fetch all comments on a specific post."""
    url = f"{BASE_URL}/posts/{post_id}/comments"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def create_post(title, body, user_id=1):
    """
    Send a POST request to create a new post.

    Note: JSONPlaceholder doesn't actually save the data permanently —
    it just pretends to and returns what the created resource would look like.
    This is great for learning!
    """
    url = f"{BASE_URL}/posts"
    payload = {
        "title": title,
        "body": body,
        "userId": user_id,
    }

    # requests.post() sends data to the server (like submitting a form)
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def print_post(post):
    print(f"  ID     : {post['id']}")
    print(f"  Title  : {post['title']}")
    print(f"  Body   : {post['body'][:80]}...")
    print()


def print_comment(comment):
    print(f"  From   : {comment['name']} <{comment['email']}>")
    print(f"  Comment: {comment['body'][:80]}...")
    print()


# ---------------------------------------------------------------------------
# Demo sections
# ---------------------------------------------------------------------------

def demo_list_posts():
    print("--- Fetching 5 posts ---\n")
    posts = fetch_posts(limit=5)
    for post in posts:
        print_post(post)


def demo_single_post():
    print("--- Fetching a single post (ID: 1) ---\n")
    post = fetch_post(1)
    print_post(post)


def demo_comments():
    print("--- Fetching comments on post #1 ---\n")
    comments = fetch_comments_for_post(1)
    for comment in comments[:3]:  # Just show the first 3
        print_comment(comment)


def demo_create_post():
    print("--- Creating a new post ---\n")
    new_post = create_post(
        title="My First Post",
        body="Hello! This is a post created with Python.",
    )
    print("Server responded with:")
    print(f"  New post ID : {new_post['id']}")
    print(f"  Title       : {new_post['title']}")
    print(f"  Body        : {new_post['body']}")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=== API Requests Demo ===")
    print("Using: https://jsonplaceholder.typicode.com\n")

    try:
        demo_list_posts()
        demo_single_post()
        demo_comments()
        demo_create_post()

        print("All requests completed successfully!")

    except requests.exceptions.ConnectionError:
        print("Could not connect to the internet. Check your connection and try again.")
    except requests.exceptions.HTTPError as error:
        print(f"The server returned an error: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Something went wrong with the request: {error}")


if __name__ == "__main__":
    main()
