import pandas as pd

def calculate_demographic_data(print_data=True):
    cols = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
]

    df = pd.read_csv('C:\\Users\\rglra\\Downloads\\adult\\adult.data', header=None, names=cols)


    # 2) Normalize strings: remove leading/trailing spaces
    df.columns = [c.strip() for c in df.columns]
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()

    # 1) How many of each race represented? -> pandas Series
    race_count = df['race'].value_counts()

    # 2) Average age of men (rounded to 1 decimal)
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3) Percentage of people who have a Bachelor's degree (rounded to 1 decimal)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4 & 5) Percentage with advanced education that earn >50K; and without advanced education earn >50K
    advanced_degrees = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df['education'].isin(advanced_degrees)

    higher_education_rich = round(((df[higher_education]['salary'] == '>50K').mean()) * 100, 1)
    lower_education_rich = round(((df[~higher_education]['salary'] == '>50K').mean()) * 100, 1)

    # 6) Minimum number of hours a person works per week
    min_work_hours = int(df['hours-per-week'].min())

    # 7) Percentage of people working minimum hours who have a salary >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    if len(min_workers) > 0:
        rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)
    else:
        rich_percentage = 0.0

    # 8) Country with highest percentage of people that earn >50K and that percentage
    country_rich_pct = df.groupby('native-country').apply(lambda g: (g['salary'] == '>50K').sum() / len(g) * 100)
    highest_earning_country = country_rich_pct.idxmax()
    highest_earning_country_percentage = round(country_rich_pct.max(), 1)

    # 9) Most popular occupation for those who earn >50K in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax() if not india_rich.empty else None

    # Optional: print results while developing
    if print_data:
        print("Number of each race:\n", race_count, "\n")
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest % of >50K:", highest_earning_country)
        print("Highest % of rich people in country:", highest_earning_country_percentage)
        print("Top occupation in India for those who earn >50K:", top_IN_occupation)

    # Return values (tests will read these)
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

if __name__ == '__main__':
    calculate_demographic_data(print_data=True)
