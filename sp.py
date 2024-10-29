a = ['''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Система отслеживания студентов для образовательных учреждений">
    <title>{% block title %}Система отслеживания студентов{% endblock %}</title>
    <style>
        /* Общие стили для всей страницы */
        body {
            margin: 0;
            font-family: 'Roboto', sans-serif;
            background-color: #f9fafb;
            color: #333;
        }

        header {
            background-color: #1e1e2f; /* Тёмный фон */
            color: #fff;
            padding: 20px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            position: relative;
            z-index: 10;
        }

        h1 {
            text-align: center;
            margin: 0;
            font-size: 2.2rem;
            font-weight: 600;
            color: #ffc107; /* Акцентный цвет */
        }

        nav {
            display: flex;
            justify-content: center;
            margin-top: 10px;
        }

        nav ul {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            gap: 20px;
        }

        nav ul li {
            font-size: 1.1rem;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            padding: 10px 20px;
            background-color: #ffc107; /* Яркие кнопки */
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        nav a:hover {
            background-color: #e0a800;
        }

        nav .active {
            background-color: #ffcd39;
            font-weight: 600;
        }

        main {
            padding: 40px 20px;
            margin: 0 auto;
            max-width: 1200px;
            background-color: #fff;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            margin-top: -40px;
            z-index: 1;
            position: relative;
        }

        footer {
            background-color: #1e1e2f;
            color: #ccc;
            text-align: center;
            padding: 20px 0;
            margin-top: 40px;
            box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.1);
        }

        footer p {
            margin: 0;
            font-size: 1rem;
        }

        /* Стили для карточек студентов */
        .students-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .student-card {
            background-color: rgba(255, 255, 255, 0.9); /* Полупрозрачный фон */
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
        }

        .student-card:hover {
            background-color: rgba(255, 255, 255, 1); /* Полная непрозрачность при наведении */
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .student-name {
            font-size: 20px;
            font-weight: bold;
            color: #1e1e2f;
            margin-bottom: 15px;
        }

        .attendance-select, .grade-input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ced4da;
            border-radius: 8px;
            background-color: #fff;
            transition: border-color 0.3s ease;
        }

        .attendance-select:focus, .grade-input:focus {
            border-color: #ffc107;
        }

        .grade-input {
            text-align: center;
        }

        /* Мобильная адаптация */
        @media (max-width: 768px) {
            header h1 {
                font-size: 1.8rem;
            }

            nav ul {
                flex-direction: column;
                gap: 15px;
            }

            main {
                padding: 20px 15px;
            }

            footer p {
                font-size: 0.9rem;
            }

            .students-list {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Система отслеживания студентов</h1>
        <nav>
            <ul>
                <li><a href="{% url 'attendance_view' %}" class="{% if request.resolver_match.url_name == 'attendance_view' %}active{% endif %}">Посещаемость</a></li>
                <li><a href="{% url 'students_list' %}" class="{% if request.resolver_match.url_name == 'students_list' %}active{% endif %}">Ученики</a></li>
            </ul>
        </nav>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>© 2024 Учебное приложение. Все права защищены.</p>
    </footer>
</body>
</html>'''
]

b = ['''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Система отслеживания студентов для образовательных учреждений">
    <title>{% block title %}Система отслеживания студентов{% endblock %}</title>
    <style>
        /* Общие стили для всей страницы */
        body {
            margin: 0;
            font-family: 'Roboto', sans-serif;
            background-color: #f9fafb;
            color: #333;
        }

        header {
            background-color: #1e1e2f; /* Тёмный фон */
            color: #fff;
            padding: 20px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            position: relative;
            z-index: 10;
        }

        h1 {
            text-align: center;
            margin: 0;
            font-size: 2.2rem;
            font-weight: 600;
            color: #ffc107; /* Акцентный цвет */
        }

        nav {
            display: flex;
            justify-content: center;
            margin-top: 10px;
        }

        nav ul {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            gap: 20px;
        }

        nav ul li {
            font-size: 1.1rem;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            padding: 10px 20px;
            background-color: #ffc107; /* Яркие кнопки */
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        nav a:hover {
            background-color: #e0a800;
        }

        nav .active {
            background-color: #ffcd39;
            font-weight: 600;
        }

        main {
            padding: 40px 20px;
            margin: 0 auto;
            max-width: 1200px;
            background-color: #fff;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            margin-top: -40px;
            z-index: 1;
            position: relative;
        }

        footer {
            background-color: #1e1e2f;
            color: #ccc;
            text-align: center;
            padding: 20px 0;
            margin-top: 40px;
            box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.1);
        }

        footer p {
            margin: 0;
            font-size: 1rem;
        }

        /* Стили для карточек студентов */
        .students-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .student-card {
            background-color: transparent; /* Прозрачный фон */
            border-radius: 10px;
            padding: 20px;
            box-shadow: none;
            transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
        }

        .student-card:hover {
            background-color: rgba(255, 255, 255, 0.6); /* Лёгкая прозрачность при наведении */
            transform: translateY(-5px);
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
        }

        .student-name {
            font-size: 20px;
            font-weight: bold;
            color: #1e1e2f;
            margin-bottom: 15px;
        }

        .attendance-select, .grade-input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ced4da;
            border-radius: 8px;
            background-color: #fff;
            transition: border-color 0.3s ease;
        }

        .attendance-select:focus, .grade-input:focus {
            border-color: #ffc107;
        }

        .grade-input {
            text-align: center;
        }

        /* Мобильная адаптация */
        @media (max-width: 768px) {
            header h1 {
                font-size: 1.8rem;
            }

            nav ul {
                flex-direction: column;
                gap: 15px;
            }

            main {
                padding: 20px 15px;
            }

            footer p {
                font-size: 0.9rem;
            }

            .students-list {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Система отслеживания студентов</h1>
        <nav>
            <ul>
                <li><a href="{% url 'attendance_view' %}" class="{% if request.resolver_match.url_name == 'attendance_view' %}active{% endif %}">Посещаемость</a></li>
                <li><a href="{% url 'students_list' %}" class="{% if request.resolver_match.url_name == 'students_list' %}active{% endif %}">Ученики</a></li>
            </ul>
        </nav>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>© 2024 Учебное приложение. Все права защищены.</p>
    </footer>
</body>
</html>'''
]

print(a in b)