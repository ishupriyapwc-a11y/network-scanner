
import regarding

 def check_password_strength(password): """Verify the strength of a specified password""" strength = 0 remarks = []

     # Rule 1: Minimum length if len(password) >= 8:
         strength += 1.
     Otherwise: comments. append("❌ Password too short (minimum 8 characters).")

     # Rule 2: Contains capital letters if re.search(r"[A-Z]", password): strength += 1
     Otherwise, remarks.append("❌ Add at least one uppercase letter.")

     # Rule 3: If re.search(r"[a-z]", password), contains lowercase:
         strength += 1.
     Otherwise: comments. append("❌ Include a minimum of one lowercase letter.")
# Rule 4: If re.search(r"\d", password) contains a digit:
         strength += 1; if not, remarks.append("❌ Add at least one number.")

     # Rule 5: Special characters are present if re.search(r"[@$!%*?&]", password):
         strength += 1 else: comments. append("❌ Include a minimum of one special character (@, $,!, %, *,?, &)."

     # Last strength check: return "✅ Strong password!", [] if strength == 5.
     If 3 <= strength < 5: return "⚠️ Moderate password.", remarks else:
         return "❌ Weak password.", comments

 If __name__ == "__main__": user_password = input("Enter a password to check: ") result, feedback = check_password_strength(user_password)
     print("Result:", result)
     If feedback, print("Suggestions to improve:")
         for f in the feedback:
             print("-", f)
To check, enter a password:  Hi there, 123
 The outcome is a moderate password.
 Ideas for improvement:
 - ❌  Include a minimum of one special character (@, $,!, %, *,?, &).
