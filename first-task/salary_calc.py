"""Salary Calculations"""


from pathlib import Path


def total_salary(path: Path) -> tuple[float]:
    """
    Parses a text file that contains information about the monthly salaries of developers
    in the company and returns the total and average salaries of all developers.

    Args:
        param1 (Path): The path to the text file.

    Returns:
        tuple[float]: The tuple of two numbers: the total amount of salaries and 
        the average salary.
    
    Raises:
        FileNotFoundError: If file doesn't exist.
    """
    try:

        with open(path, "r", encoding="utf-8") as file:
            salary_info = file.readlines()
            salary_list = []

            for row in salary_info:
                salary = row.split(",")[1]
                salary = float(salary.strip())
                salary_list.append(salary)

            tot_salary = sum(salary_list)
            avg_salary = round(tot_salary / len(salary_list), 2)

            return tot_salary, avg_salary

    except FileNotFoundError:
        return "There is no file"
