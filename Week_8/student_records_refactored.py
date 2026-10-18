# student class that has student_id, student_name, major, gpa (float), total_credits(int)
class student:
    def __init__(self, student_id, student_name, major, gpa, total_credits):
        self.student_id = student_id
        self.student_name = student_name
        self.major = major
        self.gpa = round(float(gpa), 2)
        self.total_credits = int(total_credits)

# __str__ function that prints a student
    def __str__(self):
            return f"{self.student_id:<12} {self.student_name:<22} {self.major:<24} {self.gpa:<6} {self.total_credits}"

# StudentRoster class that has a list of students
class StudentRoster:
    def __init__(self):
        self.students = []
        self.csv_loaded = False

# loads a csv file and appends each row to a student_record list. 
    def load_csv(self, filename):
        import csv      
# clears the student list each time a csv is loaded
        self.students.clear()
# Try open the csv file and return False if the csv is not loaded
        try:
            with open(filename, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
# iiterate through the csv and addend each valid row the list
                for row in csv_reader:
                    try:
                        student_record = student(
                            row["StudentID"],
                            row["StudentName"],
                            row["Major"],
                            row["GPA"],
                            row["TotalCredits"]
                        )

                        self.students.append(student_record)

                    except (ValueError, KeyError, TypeError) as e:
                        print("Record ", row, "skipped due to ", e)
                        continue

            csv_file.close()
            self.csv_loaded = True
            return True
            
        except FileNotFoundError:
            print("\nFile not found or exists. Please try again")
            return False

# display the list of records 
    def list_students(self):
        print(f"{'#':<5} {'Student ID':<12} {'Student Name':<22} {'Major':<24} {'GPA':<6} {'Credits'}")
        print("-" * 82)

        row_number = 1

        for current_student in self.students:
            print(
                f"{row_number:<5}"
                f"{current_student.student_id:<12}"
                f"{current_student.student_name:<22}"
                f"{current_student.major:<24}"
                f"{current_student.gpa:<6}"
                f"{current_student.total_credits}"
            )
            row_number += 1

        print("-" * 82)
        print(f"Total records: {len(self.students)}")
        return
# uses sirted () to sort the roster in order. prerequisite before implementing binary search
    def sorted_roster(self):
        sorted_roster = sorted(self.students, key=lambda student: student.student_id.upper())
        return sorted_roster
    
# binary search 
    def search_by_id(self, sorted_roster, search_id):
        search_id = search_id.strip().upper()
        found_student = None
        lower = 0
        higher = len(sorted_roster) - 1

        while lower <= higher:
            middle = (lower + higher) // 2
            current_student = sorted_roster[middle]
            current_student_id = current_student.student_id.upper()

            if current_student_id == search_id:
                found_student = current_student
                break

            elif current_student_id > search_id:
                higher = middle - 1

            else:
                lower = middle + 1

        if found_student is None:
            print(f"No student found with ID '{search_id}'.")
        else:
            print("\nStudent found!")
            print("-" * 40)
            print(f"  Student ID    : {found_student.student_id}")
            print(f"  Student Name  : {found_student.student_name}")
            print(f"  Major         : {found_student.major}")
            print(f"  GPA           : {found_student.gpa}")
            print(f"  Total Credits : {found_student.total_credits}")
            print("-" * 40)
        return

# main loop with the menu. Calls the methods from both classes
    def run(self):

        print("\n","=" * 60, " Student Record Management System ","=" * 60)

        while True:
            # -------------------------------------------------------------------------
            # Display Menu
            # -------------------------------------------------------------------------
            print("\nPlease select an option:")
            print("  1. Read CSV")
            print("  2. List CSV Contents")
            print("  3. Search for Student by ID")
            print("  4. Exit\n")

            menu_choice = input("Enter your choice (1-4): ").strip()

            # =========================================================================
            # Option 1: Read CSV
            # =========================================================================
            if menu_choice == "1":

                csv_filename = input("Enter the CSV filename (e.g., students.csv): ").strip()
                self.load_csv(csv_filename)

                if not self.csv_loaded:
                    print("\nNo data loaded. Please use Option 1 to read a CSV file first.")
                else:
                    print(f"\nSuccess! {len(self.students)} student record(s) loaded from '{csv_filename}'.")
                             
            # =========================================================================
            # Option 2: List CSV Contents
            # =========================================================================
            elif menu_choice == "2":

                if not self.csv_loaded:
                    print("\nNo data loaded. Please use Option 1 to read a CSV file first.")

                else:  
                    self.list_students()  

            # =========================================================================
            # Option 3: Search for Student by ID
            # =========================================================================
            elif menu_choice == "3":

                if not self.csv_loaded:
                    print("\nNo data loaded. Please use Option 1 to read a CSV file first.")

                else:
                    search_id = input("Enter the Student ID to search for: ").strip().upper()
                    sorted_roster = self.sorted_roster()
                    self.search_by_id(sorted_roster, search_id)

            # =========================================================================
            # Option 4: Exit
            # =========================================================================
            elif menu_choice == "4":
                print("\nThank you for using the Student Record Management System. Goodbye!")
                break

            # =========================================================================
            # Invalid Input
            # =========================================================================
            else:
                print()
                print(f"\n'{menu_choice}' is not a valid option. Please enter 1, 2, 3, or 4.")

    
if __name__ == '__main__':
    roster = StudentRoster()
    roster.run()