import os
import bcrypt
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

try:
    supabase = create_client(url, key)
    print("Connecting to Supabase...")

    # 1. Add some Courses
    courses = [
        {"course_name": "Web Development", "total_fee": 50000, "duration": "6 Months"},
        {"course_name": "Data Science", "total_fee": 75000, "duration": "8 Months"},
        {"course_name": "Digital Marketing", "total_fee": 30000, "duration": "3 Months"}
    ]
    
    # Simple way to insert (might fail if they exist, but that's okay)
    for c in courses:
        # Check if exists
        existing = supabase.table("courses").select("id").eq("course_name", c["course_name"]).execute()
        if not existing.data:
            supabase.table("courses").insert(c).execute()
            print(f"Added course: {c['course_name']}")
    
    # Get course IDs
    course_list = supabase.table("courses").select("id, course_name, total_fee").execute().data
    if not course_list:
        print("No courses found!")
        exit()

    # 2. Add some Students
    password_hash = bcrypt.hashpw("password123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    students = [
        {
            "student_unique_id": "STU001",
            "name": "Arjun Sharma",
            "email": "arjun@example.com",
            "phone": "9876543210",
            "password_hash": password_hash,
            "course_id": course_list[0]["id"]
        },
        {
            "student_unique_id": "STU002",
            "name": "Priya Patel",
            "email": "priya@example.com",
            "phone": "9876543211",
            "password_hash": password_hash,
            "course_id": course_list[1]["id"]
        }
    ]

    for s in students:
        existing = supabase.table("students").select("id").eq("student_unique_id", s["student_unique_id"]).execute()
        if not existing.data:
            res = supabase.table("students").insert(s).execute()
            student_id = res.data[0]["id"]
            
            # Create fee record (mimicking the routes/students.py logic)
            course = next(c for c in course_list if c["id"] == s["course_id"])
            supabase.table("fees").insert({
                "student_id": student_id,
                "total_fee": course["total_fee"],
                "amount_paid": 0,
                "balance_fee": course["total_fee"]
            }).execute()
            print(f"Added student: {s['name']}")

    # 3. Add a sample payment for Arjun
    arjun = supabase.table("students").select("id").eq("student_unique_id", "STU001").execute().data[0]
    # Check if he has payments
    payments = supabase.table("payments").select("id").eq("student_id", arjun["id"]).execute()
    if not payments.data:
        amount = 10000
        supabase.table("payments").insert({
            "student_id": arjun["id"],
            "amount_paid": amount,
            "payment_method": "UPI",
            "remarks": "Admission Fee"
        }).execute()
        
        # Update fee record
        fee = supabase.table("fees").select("*").eq("student_id", arjun["id"]).execute().data[0]
        new_paid = fee["amount_paid"] + amount
        new_balance = fee["total_fee"] - new_paid
        supabase.table("fees").update({
            "amount_paid": new_paid,
            "balance_fee": new_balance,
            "last_payment_date": "now()"
        }).eq("student_id", arjun["id"]).execute()
        print("Added sample payment for Arjun")

    print("\nDummy data setup complete!")

except Exception as e:
    print(f"Error: {e}")
