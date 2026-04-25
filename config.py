INITIAL_MONEY = 5000
INITIAL_POPULATION = 100
INITIAL_ENERGY = 200
INITIAL_SECURITY = 50
TAX_RATE = 0.1
INFLATION_RATE = 0.02
BIRTH_RATE = 0.03
DEATH_RATE = 0.01
IMMIGRATION_RATE = 0.02
HAPPINESS_THRESHOLD = 30
MAX_STORAGE_BASE = 500

BUILDING_TYPES = {
    "house": {"cost": 100, "energy": 10, "jobs": 0, "capacity": 5, "maintenance": 5},
    "farm": {"cost": 150, "energy": 15, "jobs": 3, "capacity": 0, "maintenance": 10, "produces": {"food": 20}},
    "factory": {"cost": 300, "energy": 30, "jobs": 10, "capacity": 0, "maintenance": 20, "produces": {"goods": 10}},
    "power_plant": {"cost": 400, "energy": 0, "jobs": 5, "capacity": 0, "maintenance": 25, "produces": {"energy": 50}},
    "police_station": {"cost": 200, "energy": 20, "jobs": 8, "capacity": 0, "maintenance": 15, "security_bonus": 20},
    "warehouse": {"cost": 150, "energy": 5, "jobs": 2, "capacity": 0, "maintenance": 8, "storage_bonus": 200}
}
RESOURCES_LIST = ["food", "goods", "energy", "money"]
STARTING_RESOURCES = {"food": 100, "goods": 50}
