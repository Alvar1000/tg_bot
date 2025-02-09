from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    name = State()
    age = State()
    height = State()
    weight = State()
    city = State()

class FoodState(StatesGroup):
    waiting_for_food = State()

class WaterState(StatesGroup):
    waiting_for_water = State()

class WorkoutState(StatesGroup):
    waiting_for_workout = State()