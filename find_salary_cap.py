"""
ABC corporation needs to cut payroll expenses to a specified target. 
The chief executive officer wants to do this by putting a cap on last year's 
salaries. Every employee who earned more than the cap last year will be paid the cap this year; 
employees who earned no more than the cap will see no change in their salary.

For example, if there were five employees with salaries last year were $90, $30, $100, $40, and $20, 
and the target payroll this year is $210, then $60 is suitable salary cap, since 60+30+60+40+20=210.

Design an algorithm for computing the salary cap, given the existing salaries and the targeted payroll
"""
def find_salary_cap_brute(target_payroll, current_salaries):
    current_salaries.sort()
    if sum(current_salaries) == target_payroll:
        return current_salaries[-1]
    if sum(current_salaries) < target_payroll:
        return -1
    print("Current: " + str(target_payroll) + ", Sum: " + str(sum(current_salaries)) + ", Target: " + str(target_payroll))
    current_cap = 1
    while(current_cap <= target_payroll):
        temp_salaries = []
        for val in current_salaries:
            if val > current_cap:
                temp_salaries.append(current_cap)
            else:
                temp_salaries.append(val)
        # print(sum(temp_salaries))
        if sum(temp_salaries) >= target_payroll:
            return current_cap
        else:
            current_cap += 1
            #print("Bumping up current cap to: " + str(current_cap))
    return current_cap

# driver code
target = 210
current = [90, 30, 100, 40, 20]
print(find_salary_cap_brute(target, current))    