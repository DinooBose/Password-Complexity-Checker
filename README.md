# Password Complexity Checker

This tool assesses the strength of a password based on the following criteria:

* *Length:* The number of characters in the password.
* *Uppercase Letters:* Presence of at least one uppercase letter (A-Z).
* *Lowercase Letters:* Presence of at least one lowercase letter (a-z).
* *Numbers:* Presence of at least one digit (0-9).
* *Special Characters:* Presence of at least one special character (e.g., !, @, #, $, %, ^, &, \*).

It provides feedback to the user on the password's strength and suggests ways to improve it.

## Requirements

* Python 3.x

## Usage

1.  clone the repository
```bash
git clone https://github.com/DinooBose/Password-Complexity-Checker.git
cd Password-Compexity-Checker

```
(e.g., password_checker.py).
2.  Run the script using the command: 
```bash
python3 password_checker.py
```
3.  The tool will prompt you to enter a password. Type your password and press Enter.
4.  The tool will display the password strength and provide feedback.
5.  You can enter more passwords to check or type exit to quit.

## How it Works

The script defines a function assess_password_strength that takes a password as input and checks for the presence of different character types and the length of the password. It assigns a score based on these criteria and then categorizes the password strength as "Weak," "Moderate," or "Strong." It also generates feedback to inform the user about what makes their password strong or what they can do to improve it.

