import bcrypt
from database import insert_user, get_user_by_email, log_activity

def hash_password(password: str) -> str:
    """Hash a password using bcrypt and return as UTF-8 string."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """Verify if the entered password matches the stored hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def signup_user(email: str, password: str, full_name: str = "") -> dict:
    """Register a new user with hashed password."""
    try:
        hashed_pw = hash_password(password)
        user_id = insert_user(email, hashed_pw, full_name)
        return {
            "success": True,
            "message": "User registered successfully!",
            "user_id": user_id
        }
    except Exception as e:
        return {"success": False, "message": "Signup failed: " + str(e)}

def login_user(email: str, password: str) -> dict:
    """Authenticate user by email and password."""
    user = get_user_by_email(email)  # ✅ fixed hardcoded email
    if not user:
        return {"success": False, "message": "User not found"}

    user_id, stored_hash = user
    if verify_password(password, stored_hash):
        log_activity(user_id, "Logged in")
        return {
            "success": True,
            "message": "Login successful",
            "user_id": user_id
        }
    else:
        return {"success": False, "message": "Invalid credentials"}
