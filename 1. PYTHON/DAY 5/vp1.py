def check_password(password):
    if len(password) >= 8:
        return "Valid"
    else:
        return "Invalid"


print(check_password("python123"))