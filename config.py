INITIAL_MONEY = 5000
INITIAL_POPULATION = 100
INITIAL_ENERGY = 200
INITIAL_SECURITY = 50
TAX_RATE = 0.15
INFLATION_RATE = 0.02
BIRTH_RATE = 0.03
DEATH_RATE = 0.01
IMMIGRATION_RATE = 0.02
HAPPINESS_THRESHOLD = 30
MAX_STORAGE_BASE = 1000

BUILDING_TYPES = {
    "house": {"cost": 200, "energy": 10, "jobs": 0, "capacity": 10, "maintenance": 5},
    "farm": {"cost": 300, "energy": 15, "jobs": 5, "capacity": 0, "maintenance": 10, "produces": {"food": 30}},
    "factory": {"cost": 500, "energy": 40, "jobs": 15, "capacity": 0, "maintenance": 30, "produces": {"goods": 20}},
    "power_plant": {"cost": 600, "energy": 0, "jobs": 8, "capacity": 0, "maintenance": 40, "produces": {"energy": 100}},
    "police_station": {"cost": 400, "energy": 20, "jobs": 10, "capacity": 0, "maintenance": 25, "security_bonus": 25},
    "warehouse": {"cost": 250, "energy": 10, "jobs": 5, "capacity": 0, "maintenance": 15, "storage_bonus": 500}
}
STARTING_RESOURCES = {"food": 150, "goods": 50}
