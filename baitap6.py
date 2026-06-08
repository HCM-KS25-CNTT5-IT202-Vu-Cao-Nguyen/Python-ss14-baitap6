grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]


def find_student(book, student_id):
    for index, student in enumerate(book):
        if student["id"] == student_id:
            return index
    return -1


def display_grades(book):
    print("\n--- BẢNG ĐIỂM HỌC SINH ---")
    print(
        f"{'Mã SV':<6} | {'Tên Học Sinh':<20} | {'Điểm Toán':<10} | {'Điểm Anh':<9} | {'ĐTB':<5}"
    )
    print("-" * 70)

    for student in book:
        math_score, english_score = student["info"]
        average = (math_score + english_score) / 2

        print(
            f"{student['id']:<6} | "
            f"{student['name']:<20} | "
            f"{math_score:<10.1f} | "
            f"{english_score:<9.1f} | "
            f"{average:<5.2f}"
        )

    print("-" * 70)


def add_student(book):
    while True:
        student_id = input("Nhập mã học sinh mới: ").strip().upper()

        if find_student(book, student_id) != -1:
            print(
                f"Lỗi: Mã học sinh {student_id} đã tồn tại! Vui lòng nhập mã khác."
            )
        else:
            break

    name = input("Nhập tên học sinh: ").strip()

    try:
        math_score = float(input("Nhập điểm Toán: "))
        english_score = float(input("Nhập điểm Anh: "))

        if not (0 <= math_score <= 10 and 0 <= english_score <= 10):
            print("Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10!")
            return

        student = {
            "id": student_id,
            "name": name,
            "info": (math_score, english_score)
        }

        book.append(student)

        print(
            f"Thành công: Đã thêm học sinh {student_id} vào hệ thống!"
        )

    except ValueError:
        print("Lỗi: Điểm phải là số!")


def update_scores(book):
    student_id = input(
        "Nhập mã học sinh cần cập nhật: "
    ).strip().upper()

    index = find_student(book, student_id)

    if index == -1:
        print("Lỗi: Không tìm thấy học sinh!")
        return

    try:
        math_score = float(
            input("Nhập điểm Toán mới: ")
        )

        english_score = float(
            input("Nhập điểm Anh mới: ")
        )

        if not (0 <= math_score <= 10 and 0 <= english_score <= 10):
            print("Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10!")
            return

        book[index]["info"] = (
            math_score,
            english_score
        )

        print(
            f"Thành công: Đã cập nhật điểm cho học sinh {student_id}!"
        )

    except ValueError:
        print("Lỗi: Điểm phải là số!")


def delete_student(book):
    student_id = input(
        "Nhập mã học sinh cần xóa: "
    ).strip().upper()

    index = find_student(book, student_id)

    if index == -1:
        print("Lỗi: Không tìm thấy học sinh!")
        return

    del book[index]

    print(
        f"Thành công: Đã xóa hồ sơ học sinh {student_id} khỏi hệ thống!"
    )


def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===")
        print("1. Xem bảng điểm học sinh")
        print("2. Thêm hồ sơ học sinh mới")
        print("3. Cập nhật điểm số")
        print("4. Xóa hồ sơ học sinh")
        print("5. Thoát chương trình")
        print("================================")

        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            display_grades(grade_book)

        elif choice == "2":
            add_student(grade_book)

        elif choice == "3":
            update_scores(grade_book)

        elif choice == "4":
            delete_student(grade_book)

        elif choice == "5":
            print(
                "Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()