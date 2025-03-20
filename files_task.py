import re


def create_if_not_exist_txt_file(filename):
    try:
        with open(f"{filename}.txt", "x", encoding="utf-8"):
            pass
    except FileExistsError:
        print(f"File '{filename}.txt' already exists.")


def write_multiple_lines_txt_file(filename, text_in_lines):
    with open(f"{filename}.txt", "w", encoding="utf-8") as file:
        file.writelines(text_in_lines)


def read_file(filename):
    try:
        with open(f"{filename}.txt", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File '{filename}.txt' not found.")
        return None


def process_line_to_get_group_and_marks(line):
    line = line.strip()
    if not line:
        return None

    match = re.match(r"^(.+), Group (\d+), Marks: (.+)$", line)
    if not match:
        print(f"Invalid line format. Line is skipped: {line}")
        return None

    _, group, marks_str = match.groups()

    try:
        marks = list(map(int, marks_str.split(",")))
    except ValueError:
        print(f"Invalid marks format. Line is skipped: {marks_str}")
        return None

    return group, marks


def calculate_group_averages(group_counts, group_av_marks):
    for group, value in group_counts.items():
        group_students, group_marks = value
        group_av_marks[group] = round(group_marks / group_students, 2)


def generate_summary(total_students, group_counts, group_av_marks):
    summary = [f"Total number of students: {total_students}\n"]
    for group, value in group_counts.items():
        group_students, _ = value
        summary.append(f"Group {group}: {group_students} students, "
                       f"average mark {group_av_marks[group]}\n")

    return summary


def read_and_process_txt_file(filename):
    lines = read_file(filename)
    if not lines:
        return None

    total_students = 0
    group_counts = {}
    group_av_marks = {}

    for line in lines:
        result = process_line_to_get_group_and_marks(line)
        if result:
            group, marks = result
            total_students += 1
            marks_st = sum(marks)
            av_marks = round(marks_st / len(marks), 2)
            if group in group_counts:
                group_counts[group][0] += 1
                group_counts[group][1] += av_marks
            else:
                group_counts[group] = [1, av_marks]

    calculate_group_averages(group_counts, group_av_marks)

    summary = generate_summary(total_students, group_counts, group_av_marks)
    print(summary)
    return summary


def add_summary_to_txt_file(filename, summary):
    with open(f"{filename}.txt", "a", encoding="utf-8") as file:
        file.writelines(summary)


create_if_not_exist_txt_file("students")
text_in_lines = ["Ivan Ivanov, Group 1, Marks: 5,4,4,5,3,5\n",
                 "Petr Petrov, Group 2, Marks: 4,5,4,3,5,5\n",
                 "Andrey Andreev, Group 1, Marks: 3,4,4,4,5,3\n",
                 "Alena Ivanova, Group 3, Marks: 5,5,4,4,3,5\n",
                 "Petra Petrova, Group 3, Marks: 4,5,3,3,5,5\n",
                 "Ada Andreeva, Group 2, Marks: 5,3,4,4,4,3\n",
                 "Adriana Chill, Group 1, Marks: 4,2,3,3,3,5\n",
                 "Linda Perk, Group 4, Marks: 5,3,5,4,4,5\n"]

write_multiple_lines_txt_file("students", text_in_lines)
summary1 = read_and_process_txt_file("students")
add_summary_to_txt_file("students", summary1)
