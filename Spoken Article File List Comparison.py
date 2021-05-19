def check_for_missing_files(version_1_filename = "existence check 1.txt", version_2_filename = "existence check 2.txt"):
    """Runs through two versions of the "Spoken Articles" file, and sees if anything is missing from one or the other. (Unfinished.)"""
    with open(version_1_filename) as file1:
        lines1 = [line.split(']]')[0] for line in file1 if line[0] == '*']
    with open(version_2_filename) as file2:
        lines2 = [line.split(']]')[0] for line in file2 if line[0] == '*']

    return [lines1, lines2]
#    return (len(lines1), len(lines2))

