# Interview Questions 

### 1. What makes a password strong?
*   **Length:** The single most important factor (e.g., 12+ characters, ideally 16+).
*   **Complexity:** Mix uppercase, lowercase, numbers, and symbols.
*   **Unpredictability:** Avoid dictionary words, common phrases, personal info, sequences, or keyboard patterns.
*   **Uniqueness:** Not reused across any other accounts.
*   **Randomness:** Appears random, not based on easily guessable patterns.

### 2. What are common password attacks?
*   **Brute Force:** Trying every possible combination.
*   **Dictionary Attack:** Trying common words, phrases, and their variations (e.g., "P@ssw0rd").
*   **Credential Stuffing:** Using breached username/password pairs on other sites.
*   **Phishing:** Tricking users into revealing passwords.
*   **Keylogging:** Malware recording keystrokes.
*   **Rainbow Table Attacks:** Using precomputed tables to crack hashed passwords (mitigated by salting).
*   **Social Engineering:** Manipulating people into giving up passwords.
*   **Shoulder Surfing:** Physically observing someone enter their password.

### 3. Why is password length important?
*   **Exponential Difficulty:** Each added character *exponentially* increases the number of possible combinations.
*   **Resistance to Brute Force:** Makes it computationally infeasible to try all combinations within a reasonable time.
*   **Resistance to Dictionary Attacks:** Longer strings are less likely to be in wordlists or easily mutated from them.
*   **Modern Priority:** Length is now prioritized over complex character requirements by experts (like NIST).

### 4. What is a dictionary attack?
*   An attack where hackers systematically try a vast list of:
    *   Common words (from multiple languages).
    *   Common passwords (e.g., "password123", "qwerty").
    *   Known breached passwords.
    *   Variations of the above (e.g., adding numbers/symbols at start/end, using "leet speak" like `@` for `a`).
*   It exploits the human tendency to use easily remembered (and easily guessed) words and patterns.

### 5. What is multi-factor authentication (MFA)?
*   A security method requiring **two or more distinct verification factors** to grant access:
    1.  **Something You Know:** Password, PIN, security question.
    2.  **Something You Have:** Smartphone (app notification/code), security key (YubiKey), hardware token, smart card.
    3.  **Something You Are:** Biometrics (fingerprint, facial recognition, iris scan).
*   **Purpose:** Significantly increases security by adding layers. Even if a password is compromised, the attacker likely lacks the second factor.

### 6. How do password managers help?
*   **Generate Strong Passwords:** Create long, random, unique passwords for each site.
*   **Store Passwords Securely:** Keep passwords encrypted in a vault, accessible by one strong master password.
*   **Auto-fill Credentials:** Securely fill usernames/passwords into websites and apps.
*   **Prevent Reuse:** Eliminate the temptation to reuse passwords across sites.
*   **Simplify Management:** Users only need to remember one strong master password.
*   **Security Alerts:** Often alert users about compromised passwords or weak/reused credentials.

### 7. What are passphrases?
*   A password created by stringing together **multiple random words** (e.g., "correct horse battery staple" or "tuna pencil gateway jolly").
*   **Advantages:**
    *   **Length:** Easily achieve recommended lengths (20+ characters).
    *   **Memorability:** Easier to remember than complex, random strings of characters.
    *   **Strength:** Can be very strong *if* the words are truly random and not a common phrase/song lyric/quote.
*   **Key:** Must use **random words** (ideally 4-6), not predictable phrases ("iloveyou" or "sunshinebeach").

### 8. What are common mistakes in password creation?
*   **Using Short Passwords:** Easily cracked.
*   **Reusing Passwords:** One breach compromises many accounts.
*   **Using Personal Information:** Names, birthdays, pet names, addresses (easily found).
*   **Relying on Common Words/Patterns:** "Password123", "qwerty", "abc123", sequences.
*   **Simple Character Substitutions:** "P@ssw0rd" is still weak and in every attacker's dictionary.
*   **Not Updating Default Passwords:** Leaving default router/admin passwords.
*   **Writing Down Passwords Insecurely:** Sticky notes, unencrypted files.
*   **Sharing Passwords:** Especially via insecure methods like email/chat.
*   **Ignoring MFA:** Not enabling it where available.
