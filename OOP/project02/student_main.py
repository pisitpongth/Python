from student import Student


def show_info(st):
    print(
        "Name : ",
        st.get_name(),
        "\nYear : ",
        st.get_study_year(),
        "\nScore: ",
        st.get_score(),
        "\nGrade: ",
        st.get_grade(),
    )


def main():
    student = Student()

    name = input("Enter student name: ").strip()
    student.set_name(name)

    year = int(input("Enter student year: ").strip())
    student.set_study_year(year)

    midterm_score = int(input("Enter mid-term score: ").strip())
    student.add_point(midterm_score)

    fianl_score = int(input("Enter final score: ").strip())
    student.add_point(fianl_score)

    print("------------------------------")
    show_info(student)


if __name__ == "__main__":
    main()
