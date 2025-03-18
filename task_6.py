def count_file_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        lines_count = len(lines)
        words_count = 0
        letters_count = 0

        for line in lines:
            words_in_line = line.split()
            words_count += len(words_in_line)

            for l in line:
                if l.isalpha():
                    letters_count += 1

    summary = f"Lines: {lines_count}, words: {words_count}, letters {letters_count}"

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(summary)

    print(summary)
