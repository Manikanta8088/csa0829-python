def calculate_users_details(total_users, staff_users):
    # Calculate student users
    student_users = total_users - staff_users

    # Calculate non-teaching staff users
    non_teaching_staff_users = staff_users // 3

    return student_users, staff_users, non_teaching_staff_users

if __name__ == "__main__":
    total_users = int(input("Enter the total number of users in the college: "))
    staff_users = int(input("Enter the number of staff users in the college: "))

    student_users, staff_users, non_teaching_staff_users = calculate_users_details(total_users, staff_users)

    print("\nTotal Users:", total_users)
    print("Student Users:", student_users)
    print("Staff Users:", staff_users)
    print("Non-teaching Staff Users:", non_teaching_staff_users)
