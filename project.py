import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Загружаем скачанный с Kaggle каталог фильмов
movies_df = pd.read_csv('tmdb_5000_credits.csv')

# Получаем список всех ID фильмов из каталога
available_ids = movies_df['movie_id'].dropna().unique().tolist()

# 2. Генерируем историю только для ОДНОГО пользователя (для вас)
user_data = []

num_movies = 500
watched_movies = random.sample(available_ids, num_movies)

# Варианты оценок и их веса (вероятности выпадания)
ratings_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ratings_weights = [1, 2, 3, 4, 10, 15, 15, 20, 20, 10]  # Чем больше число, тем чаще выпадает оценка


for movie_id in watched_movies:
    # Выбираем одну оценку с учетом весов
    user_rating = random.choices(ratings_pool, weights=ratings_weights, k=1)[0]

    # Случайная дата просмотра за последние полгода
    random_days = random.randint(0, 180)
    watch_date = (datetime.now() - timedelta(days=random_days)).strftime('%Y-%m-%d')

    user_data.append({
        'movie_id': movie_id,
        'user_rating': user_rating,
        'watch_date': watch_date
    })

# 3. Сохраняем в CSV
user_history_df = pd.DataFrame(user_data)
user_history_df.to_csv('user_history.csv', index=False)
print("Файл user_history.csv для одного пользователя успешно создан!")
