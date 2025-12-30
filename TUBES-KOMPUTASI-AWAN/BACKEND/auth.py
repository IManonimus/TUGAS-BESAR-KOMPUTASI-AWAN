from flask_jwt_extended import create_access_token

def generate_token(user):
    return create_access_token({
        "id": user.id,
        "role": user.role
    })
