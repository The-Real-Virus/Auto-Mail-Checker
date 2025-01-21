# 💀Auto Mail Checker💀

## 📜Description
The Email Enumeration Script allows penetration testers and developers to automate the process of validating  
email addresses against a web application's backend. Using a list of emails and customizable request parameters,  
the script verifies which emails are valid and outputs the results. It is designed to streamline  
email enumeration tasks in an interactive and user-friendly manner.  

## 🔑Features
- Customizable Requests: Define target URLs, headers, and error messages to fit your testing environment.  
- Concurrency Support: Utilizes multithreading for faster email validation.  
- Interactive Prompts: Walks users through the required input, making it beginner-friendly.  
- Progress Bar: Displays a real-time progress bar with tqdm for better feedback.  
- Error Handling: Gracefully handles request errors, file issues, and unexpected input.  
- Results Saving: Automatically saves valid emails to a file specified by the user.  

## 🚀Step-by-Step Guide in Linux Terminal !

Step 1: Update & upgrade your system  
>sudo apt update  
>sudo apt upgrade  

Step 2: Clone the repository  
>git clone https://github.com/The-Real-Virus/Auto-Mail-Checker.git  

Step 3: Go to the Tool Directory where u clone it and read requirements.txt file !  
>cd Auto-Mail-Checker  
(read requirements.txt file using cat or gedit)  

Step 4: Email File ! (Important !)  
>u can use this repository for gmails ( https://github.com/nyxgeek/username-lists )  
>or make ur own list using crunch or any other tool for target mails to check against any web form  

Step 5: Move Email File To The Directory  
>after creating ur own list or downloaded from that repository  
>move it to the Auto-Mail-Checker Directory  
>after running script then u need just to enter the name of file not a full path  

Step 5: After Completing the process now u can run script  
>python3 Checker.py  

## ⚙️Troubleshooting

1) `Script Doesn't Run:`  
- Install required dependencies (see requirements.txt file)  

2) `Progress Bar Freezes:`  
- Check your internet connection.  
- Reduce the number of threads (default is 10) in the script if your machine is under heavy load.  

3) `FileNotFoundError:`  
- Ensure the path to the email list file is correct.  
- Use absolute paths if the file isn't in the same directory as the script.  

4) `Unexpected Response Structure:`  
- Verify the target URL, headers, and error messages are configured correctly.  

## 💡Tips !
- Test in a Safe Environment: Always run this script on a test server or with explicit permission from the target owner.  
- Verify Inputs: Double-check the URL, headers, and error messages to match the web application's behavior.  
- Optimize Email Lists: Remove duplicates and invalid formats from the email list to reduce unnecessary requests.  
- Adjust Thread Count: Use a higher thread count for faster performance, but ensure your system can handle the load.  
- Use Output Files: Save the results to a file for easier analysis and reporting.  

## 🤝Follow the Prompts !
1) Displays an ASCII art banner.  
2) Asks for the target URL, headers, and error messages.  
3) Prompts you to input the email list file path.  
4) Runs email enumeration with a visible progress bar.  
5) Outputs valid emails and saves them to a file.  

## 🛠️MODIFICATION  

- U CAN MODIFY THE SCRIPT ACCORDING TO UR NEEDs !!!  

## 📂Example OutPut
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

	Press 'y' to continue or 'n' to exit: y

	Enter the details for the target:
	Target URL (e.g., http://example.com/functions.php): http://example.com/api/login
	Error message for invalid emails (e.g., 'Email does not exist'): Email does not exist
	Host header (e.g., example.com): example.com
	Origin header (e.g., http://example.com): http://example.com
	Referer header (e.g., http://example.com/login): http://example.com/login

	Enter the path to the email list file: email_list.txt

	Starting email enumeration...

	Checking emails: 100%|#####################################| 100/100 [00:05<00:00, 19.88it/s]

	=== Enumeration Complete ===
	Valid emails found:
	valid1@example.com
	valid2@example.com
	valid3@example.com

	Enter the output file name to save valid emails (e.g., valid_emails.txt): valid_emails.txt

	[INFO] Valid emails saved to valid_emails.txt

# ⚠️Disclaimer !
This tool is intended for ethical and educational use only.  
Do not use it for illegal activities. The author is not responsible for any misuse.  
This script is intended for educational purposes and authorized testing only.  
Unauthorized use of this script is illegal and unethical.  
Ensure you have explicit permission before testing any system.  
- Obtain explicit permission before testing any system.  
- Adhere to all applicable laws and regulations.  
- Respect user privacy and data.  
- By using this script, you agree to take full responsibility for your actions.  
