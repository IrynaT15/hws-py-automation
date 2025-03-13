import re


def create_if_not_exist_txt_file(filename):
    try:
        with open(f"{filename}.txt", "x") as file:
            pass
    except FileExistsError:
        print(f"File '{filename}.txt' already exists.")
    except Exception as e:
        print(f"Error for file creation: {e}")


def write_multiple_lines_txt_file(filename, text_in_lines):
    try:
        with open(f"{filename}.txt", "w") as file:
            file.writelines(text_in_lines)
    except Exception as e:
        print(f"Error for file writing: {e}")


def read_and_process_txt_file(filename):
    try:
        with open(f"{filename}.txt") as file:
            text = file.readlines()
    except FileNotFoundError:
        print(f"File '{filename}.txt' not found.")
    except Exception as e:
        print(f"Error for file reading: {e}")

    total_students = 0
    group_counts = {}
    group_av_marks = {}

    for line in text:
        line = line.strip()
        if not line:
            continue

        match = re.match(r"^(.+), Group (\d+), Marks: (.+)$", line)
        if not match:
            print(f"Invalid line format. Line is skipped: {line}")
            continue

        line = line.split(", ")

        if len(line) != 3:
            print(f"Invalid line format: {line}")
            continue

        marks =line[2].replace('Marks: ', '')

        try:
            marks = list(map(int, marks.split(",")))
        except ValueError:
            print(f"Invalid marks format. Line is skipped: {marks}")
            continue

        total_students += 1

        marks_st = sum(marks)
        av_marks_st = round(marks_st / len(marks), 2)

        for char in line[1]:
            if char.isnumeric():
                group_number = "".join(char)

                if group_number in group_counts:
                    group_counts[group_number][0] += 1
                    group_counts[group_number][1] += av_marks_st
                else:
                    group_counts[group_number] = [1, av_marks_st]

    for group, value in group_counts.items():
        group_students, group_marks = value
        group_av_marks[group] = round(group_marks / group_students, 2)

    summary = [f"Total number of students: {total_students}\n"]
    for group, value in group_counts.items():
        group_students, group_marks = value
        summary.append(f"Group {group}: {group_students} students,"
                       f"average mark {group_av_marks[group]}\n")

    print(summary)
    return summary


def add_summary_to_txt_file(filename, summary):
    try:
        with open(f"{filename}.txt", "a") as file:
            file.writelines(summary)
    except Exception as e:
        print(f"Error writing to file: {e}")


# create_if_not_exist_txt_file("students")
# text_in_lines = ["Ivan Ivanov, Group 1, Marks: 5,4,4,5,3,5\n",
#                  "Petr Petrov, Group 2, Marks: 4,5,4,3,5,5\n",
#                  "Andrey Andreev, Group 1, Marks: 3,4,4,4,5,3\n",
#                  "Alena Ivanova, Group 3, Marks: 5,5,4,4,3,5\n",
#                  "Petra Petrova, Group 3, Marks: 4,5,3,3,5,5\n",
#                  "Ada Andreeva, Group 2, Marks: 5,3,4,4,4,3\n",
#                  "Adriana Chill, Group 1, Marks: 4,2,3,3,3,5\n",
#                  "Linda Perk, Group 4, Marks: 5,3,5,4,4,5\n"]
#
# write_multiple_lines_txt_file("students", text_in_lines)
# summary1 = read_and_process_txt_file("students")
#
# add_summary_to_txt_file("students", summary1)
