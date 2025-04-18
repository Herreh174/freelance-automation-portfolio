from scripts.parse_vacancies import (
    parse_vacancies_api,
    calculate_percentiles,
    group_similar_salaries,
    save_to_excel,
    plot_scatter
)

def main():
    job_title = input("Введите должность: ")
    vacancies = parse_vacancies_api(job_title, pages=5)  # Увеличено количество страниц
    
    if vacancies:
        # Группировка вакансий по зарплатам
        grouped_salaries = group_similar_salaries(vacancies)
        
        # Построение графика
        plot_scatter(vacancies, grouped_salaries)
        
        # Сохранение данных в файл Excel
        save_to_excel(vacancies)

    else:
        print(f"Не удалось найти вакансии для должности '{job_title}', исключая Москву.")

if __name__ == "__main__":
    main()
