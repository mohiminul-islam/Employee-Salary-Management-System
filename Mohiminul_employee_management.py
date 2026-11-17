
# ADD EMPLOYEE 

def add_employee(emp_name , emp_id , emp_salary):  # gat 3 variable for rmp info
    with open("employees.txt", "a") as file:  # use a for add 
        file.write(f"emp_name : {emp_name} | emp_id : {emp_id} | emp_Salary : {emp_salary}\n")
    return "Employee Added Successfully"

#View Employee

def view_employee():
    try:
        with open("employees.txt", "r") as file: # use r for read employee
            emp_record = file.readlines()
        if emp_record == "":
            print("No Employee record Found")
        return emp_record
    except FileNotFoundError:
        return "No Employee record Found"

def emp_operation():
    while True:
        print("Wellcome To Employee Management System")
        print("add Employee  choose 1")
        print("view Employee choose 2 ")
        print("Exit choose 3")

        choose = input("Choose option")

        if choose == "1":
            emp_name = input("Enter Employee Name : ").strip()
            emp_id= input("Enter Employee ID : ").strip()
            if not emp_name or emp_id :
                print("Name and id can not be empty")
                continue
            try:
                emp_salary = int(input("Enter Employee Salary : "))
            except ValueError:
                print("please Enter the valid number of salary")
                continue
            if emp_salary < 0:
                print("salary can not be negtive")
                continue
            emp = add_employee(emp_name , emp_id , emp_salary)
            print(emp)
        elif choose == "2":
            record = view_employee()

            if record:
                print("\nEmployee record")
                for records in record:
                    print(records.strip("\n"))
            else:
                print("No Employee record Found")
        elif choose == "3":
            print("=====Your Employee======")
            record = view_employee()
            print(record)
            print("Thanks for using our employee Management system")
            break
        else:
            print("invalid option : choose 1 , 2 , 3")
            
        

if __name__ == "__main__":
    emp_operation()