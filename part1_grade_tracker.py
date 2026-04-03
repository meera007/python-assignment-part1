class PythonBasicsControlFlow():
    """ Masai Assignment 3 Part 1 """


    def task1():
        raw_students = [
            {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
            {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
            {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
            {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
            {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
            ]
        cleaned_students = []
        for student in raw_students:
            # Clean name
            name = student["name"].strip().title()

            # Convert roll to int
            roll = int(student["roll"])

            marks=[]
            # Convert marks string to list of ints
            for m in  student["marks_str"].split(", "):
                marks.append(int(m))

            # Validate name (only alphabetic characters in each word)
            name_words = name.split()
            for word in name_words:
                if not word.isalpha():
                    validation_msg = "✗ Invalid name"
                    break
                validation_msg = "✓ Valid name"
            

            print(f"{validation_msg} → {name}")

            # Print formatted profile card
            print("=" * 32)
            print(f"Student : {name}")
            print(f"Roll No : {roll}")
            print(f"Marks   : {marks}")
            print("=" * 32)

            cleaned_students.append({
            "name": name,
            "roll": roll,
            "marks": marks
            })

            # Find student with roll number 103
            for student in cleaned_students:
                if student["roll"] == 103:
                    print("\nName in ALL CAPS :", student["name"].upper())
                    print("Name in lowercase:", student["name"].lower())

    def task2():
        student_name = "Ayesha Sharma"
        subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
        marks        = [88, 72, 95, 60, 78]
        print(f"Student Name: {student_name}\n")
        # Subject-wise Report
        print("Subject-wise Report:")
        for subject, mark in zip(subjects, marks):
            grade = PythonBasicsControlFlow.get_grade(mark)
            print(f"{subject:<10} : {mark} → Grade {grade}")
        total_marks = sum(marks)
        average_marks = round(total_marks / len(marks), 2)
        highest_mark = max(marks)
        lowest_mark = min(marks)
        highest_subject = subjects[marks.index(highest_mark)]
        lowest_subject = subjects[marks.index(lowest_mark)]
        # Printing the Summary
        print("\nSummary:")
        print(f"Total Marks          : {total_marks}")
        print(f"Average Marks        : {average_marks}")
        print(f"Highest Scoring      : {highest_subject} ({highest_mark})")
        print(f"Lowest Scoring       : {lowest_subject} ({lowest_mark})")

        #Adding Additional Subjects
        new_subjects_added = 0
        print("\n--- Enter New Subjects (type 'done' to stop) ---")
        while True:
            subject = input("Enter subject name: ").strip()
            if subject.lower() == "done":
                break
            try:
                mark = int(input("Enter marks (0–100): "))
                if mark < 0 or mark > 100:
                    print("⚠ Marks must be between 0 and 100. Entry skipped.")
                    continue
            except ValueError:
                print("⚠ Invalid input. Marks must be a number. Entry skipped.")
                continue

            subjects.append(subject)
            marks.append(mark)
            new_subjects_added += 1
            print("Subject added successfully.\n")
        updated_total = sum(marks)
        updated_average = round(updated_total / len(marks), 2)
        print("\n--- Final Report ---")
        print(f"New subjects added : {new_subjects_added}")
        print(f"Updated average   : {updated_average}")


    def get_grade(mark):
        #Deciding the Subject grade bases on marks
        if 90 <= mark <= 100:
            return "A+"
        elif 80 <= mark <= 89:
            return "A"
        elif 70 <= mark <= 79:
            return "B"
        elif 60 <= mark <= 69:
            return "C"
        else:
            return "F"
    
    def task3():
        class_data = [
            ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
            ("Rohit Verma",    [55, 68, 49, 72, 61]),
            ("Priya Nair",     [91, 85, 88, 94, 79]),
            ("Karan Mehta",    [40, 55, 38, 62, 50]),
            ("Sneha Pillai",   [75, 80, 70, 68, 85]),
            ]
        passed = 0 
        failed = 0
        averages = []
        topper_name = ""
        topper_avg = 0
        print("Name              | Average | Status")
        print("----------------------------------------")
        for name, marks in class_data:
            total = sum(marks)
            sujectcount = len(marks)
            avg = round(total / sujectcount, 2)
            averages.append(avg)
            if avg >= 60:
                status = "Pass"
                passed += 1
            else:
                status = "Fail"
                failed += 1                

            if avg > topper_avg:
                topper_avg = avg
                topper_name = name

            print(f"{name:<17} | {avg:6.2f}  | {status}")

        class_average = round(sum(averages) / len(averages), 2)

        print("\nSummary:")
        print(f"Students Passed : {passed}")
        print(f"Students Failed : {failed}")
        print(f"Class Topper    : {topper_name} ({topper_avg})")
        print(f"Class Average   : {class_average}")

    def task4():
        essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

        # Step 1: Strip leading and trailing whitespace
        clean_essay = essay.strip()
        print("1. Clean Essay:")
        print(clean_essay)
        print()

        # Step 2: Convert to Title Case
        title_case_essay = clean_essay.title()
        print("2. Title Case:")
        print(title_case_essay)
        print()

        # Step 3: Count occurrences of "python" (case-insensitive)
        python_count = clean_essay.count("python")
        print("3. Count of 'python':")
        print(python_count)
        print()

        # Step 4: Replace "python" with "Python 🐍"
        replaced_essay = clean_essay.replace("python", "Python 🐍")
        print("4. Replaced 'python' with 'Python 🐍':")
        print(replaced_essay)
        print()

        # Step 5: Split into sentences
        sentences = clean_essay.split(". ")
        print("5. Sentences List:")
        print(sentences)
        print()

        # Step 6: Print numbered sentences
        print("6. Numbered Sentences:")
        for i, sentence in enumerate(sentences, start=1):
            sentence = sentence.strip()
            if not sentence.endswith("."):
                sentence += "."
            print(f"{i}. {sentence}")

    def main():
        print("\n===========Task1===================\n")
        PythonBasicsControlFlow.task1()
        print("\n===========Task2===================\n")
        PythonBasicsControlFlow.task2()
        print("\n===========Task3===================\n")
        PythonBasicsControlFlow.task3()
        print("\n===========Task4===================\n")
        PythonBasicsControlFlow.task4()
        


if __name__ == "__main__":
    PythonBasicsControlFlow.main()