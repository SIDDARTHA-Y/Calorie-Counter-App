import json

def load_database():
    with open('database.json', 'r') as f:
        return json.load(f)

def track_calories(food, amount):
    database = load_database()
    if food in database:
        calories = database[food] * amount
        return f'{amount}g of {food} contains {calories} kcal'
    return 'Food item not found in database'

if __name__ == "__main__":
    print(track_calories('Apple', 100))
