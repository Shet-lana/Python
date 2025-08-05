import pickle


class StudentManager:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
                self.students = data['students']
                self.subjects = data['subjects']
                self.next_id = max(map(lambda k: int(k.lstrip('S')), self.students.keys()), default=0) + 1
        except FileNotFoundError:
            self.students = {}
            self.subjects = set()
            self.next_id = 1

    def save_data(self):
        data = {'students': self.students, 'subjects': self.subjects}
        with open(self.filename, 'wb') as f:
            pickle.dump(data, f)

    def add_student(self, name, group):
        """Метод добавляет нового студента и выводит уведомление"""
        student_id = f'S{self.next_id:03}'
        self.students[student_id] = {'name': name, 'group': group, 'subjects': {}}
        print(f'Студент {name} добавлен с ID: {student_id}.')
        self.next_id += 1
        return student_id

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f'Студент {student_id} удалён.')
        else:
            print('Ошибка: Студента с таким ID не существует.')

    def list_students(self):
        for sid, info in self.students.items():
            print(f'{sid}: {info["name"]}, Группа: {info["group"]}')

    def add_subject(self, subject_name):
        self.subjects.add(subject_name)

    def list_subjects(self):
        print("Предметы:", ', '.join(sorted(self.subjects)))

    def add_grade(self, student_id, subject, grade):
        if not (1 <= int(grade) <= 5):
            raise ValueError('Оценка должна быть от 1 до 5')

        if student_id not in self.students:
            raise KeyError('Студент не найден')

        if subject not in self.subjects:
            raise KeyError('Предмет не найден')

        grades = self.students[student_id]['subjects'].setdefault(subject, [])
        grades.append(int(grade))

    def get_student_info(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            subjects = []
            total_avg = 0
            count = 0
            for subj, grades in student['subjects'].items():
                avg = sum(grades) / len(grades) if len(grades) > 0 else 0
                subjects.append((subj, grades, round(avg, 2)))
                total_avg += avg * len(grades)
                count += len(grades)

            overall_avg = round(total_avg / count, 2) if count > 0 else '-'
            print(f"{student_id}: {student['name']}, Группа: {student['group']} ({overall_avg})")
            for subj, grades, avg in subjects:
                print(f'- {subj}: {grades} (средний: {avg:.2f})')
        else:
            print('Ошибка: Студента с данным ID не найдено.')

    def get_group_performance(self, group):
        students_in_group = [(sid, sdata) for sid, sdata in self.students.items() if sdata['group'] == group]
        if not students_in_group:
            print('Ошибка: Нет студентов в указанной группе.')
            return

        results = []
        for sid, sdata in students_in_group:
            total_avg = 0
            count = 0
            for subj, grades in sdata['subjects'].items():
                avg = sum(grades) / len(grades) if len(grades) > 0 else 0
                total_avg += avg * len(grades)
                count += len(grades)
            overall_avg = round(total_avg / count, 2) if count > 0 else '-'
            results.append((sid, sdata['name'], overall_avg))

        # Общий средний балл группы
        group_total_avg = sum([ra[2] for ra in results]) / len(results) if len(results) > 0 else '-'
        print(f"Успеваемость группы {group}: Средний балл группы — {round(group_total_avg, 2)}")
        for sid, name, avg in sorted(results, key=lambda x: x[2], reverse=True):
            print(f"- {sid}: {name}, Средний балл: {avg}")


def main_menu(manager):
    while True:
        print("\nМеню:")
        print(
            "1. Добавить студента\n2. Добавить предмет\n3. Добавить оценку\n4. Посмотреть информацию о студенте\n5. Анализ успеваемости группы\n6. Список всех студентов\n7. Список всех предметов\n8. Удалить студента\n9. Сохранить данные\n0. Выход")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            name = input("Введите ФИО студента: ")
            group = input("Введите группу: ")
            manager.add_student(name, group)
        elif choice == '2':
            subject = input("Введите название предмета: ")
            manager.add_subject(subject)
            print(f"Предмет '{subject}' добавлен.")
        elif choice == '3':
            student_id = input("Введите ID студента: ")
            subject = input("Введите название предмета: ")
            grade = input("Введите оценку (1-5): ")
            try:
                manager.add_grade(student_id, subject, grade)
                print(f"Оценка {grade} успешно добавлена!")
            except Exception as e:
                print(e)
        elif choice == '4':
            student_id = input("Введите ID студента: ")
            manager.get_student_info(student_id)
        elif choice == '5':
            group = input("Введите номер группы: ")
            manager.get_group_performance(group)
        elif choice == '6':
            manager.list_students()
        elif choice == '7':
            manager.list_subjects()
        elif choice == '8':
            student_id = input("Введите ID студента: ")
            manager.remove_student(student_id)
        elif choice == '9':
            manager.save_data()
            print("Данные сохранены.")
        elif choice == '0':
            break
        else:
            print("Неверный выбор пункта меню.")


if __name__ == "__main__":
    manager = StudentManager('students_data.pkl')
    main_menu(manager)