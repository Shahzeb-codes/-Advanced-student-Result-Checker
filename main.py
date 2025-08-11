print("🧮 Welcome to the Student Result Checker Program!")

print("This program will take the marks of 6 subjects from you,")

print("check your pass/fail status in each subject, calculate your overall percentage,")

print("and tell you if you have passed overall.\n")

# List of subjects for which marks will be taken

subjects = [

    "English",
    "Python Language",
    "C# Language",
    "Mathematics",
    "Physics",
    "Chemistry"

]

# Updated minimum passing marks per subject and for overall percentage

passing_marks = 40

# List to store marks entered by user

marks = []

print("Please enter your marks out of 100 for each subject.\n")

# Loop to take marks input for each subject
for subject in subjects:

    while True:  # Loop until valid input is entered

        try:

            score = int(input(f"Enter the marks for {subject}: "))

            if 0 <= score <= 100:
                marks.append(score)
                break

            else:
                print("⚠️ Please enter marks between 0 and 100 only.")

        except ValueError:
            print("❌ Invalid input! Please enter a valid integer number.")


print("\n" + "="*40)

print("Here are your results in each subject:")

print("="*40 + "\n")

# Check pass/fail per subject with new passing criteria 40 marks

for i, score in enumerate(marks):

    if score >= passing_marks:
        print(f"✅ You have passed in {subjects[i]} with {score} marks.")

    else:
        print(f"❌ You have failed in {subjects[i]} with {score} marks.")
        print(f"   Don't worry! You can try again and improve.\n")


# Calculate total obtained marks
total = sum(marks)



# Calculate percentage score
percentage = (total / (len(subjects) * 100)) * 100

print("\n" + "="*40)
print("Overall Performance Summary:")
print("="*40 + "\n")


# Display total marks and percentage clearly
print(f"🎯 Total Marks Obtained: {total} out of {len(subjects)*100}")

print(f"📊 Percentage: {percentage:.2f}%")



# Overall pass/fail decision based on overall percentage >= 40%
if percentage >= 40:
    print("\n🎉 Congratulations! You have passed overall based on percentage.")
    
else:
    print("\n😢 Unfortunately, your overall percentage is below 40%. You failed overall.")

print("\n" + "="*40)

print("Thank you for using the Student Result Checker Program!")

print("We wish you the best of luck in your studies! ❤")

print("="*40)

print("the program is ended....")


