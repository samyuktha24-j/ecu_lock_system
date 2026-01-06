from django.shortcuts import render
from .models import ECU
import secrets
import hashlib
import base64

# Generate 256-bit key
def generate_256bit_password():
    return secrets.token_bytes(32)  # 32 bytes = 256 bits

# Hash the password for storage
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def home(request):
    generated_password = None
    ecu_id = None
    message = None

    if request.method == "POST":
        ecu_id = request.POST.get("ecu_id")

        # Check if ECU already exists
        if ECU.objects.filter(ecu_id=ecu_id).exists():
            message = "ECU already registered. Password cannot be viewed again."
        else:
            # Generate secure 256-bit password
            raw_password = generate_256bit_password()
            # Encode in base64 for display
            generated_password = base64.urlsafe_b64encode(raw_password).decode()

            # Hash before saving
            password_hash = hash_password(generated_password)

            # Save ECU with hashed password
            ECU.objects.create(
                ecu_id=ecu_id,
                password_hash=password_hash,
                status="LOCKED"
            )

            message = "Password generated successfully. Save it securely!"

    return render(request, "myapp/home.html", {
        "password": generated_password,
        "ecu_id": ecu_id,
        "message": message
    })
