import os

WORLD_SIZE = 20

STARTING_BIOMASS_COD = 0
STARTING_BIOMASS_ANCHOVY = 500
STARTING_BIOMASS_PLANKTON = 14800
MIN_PERCENT_ALIVE = 0.2
MAX_STEPS = 2000

EAT_AMOUNT = 0.25
EAT_AMOUNT_ANCHOVY = 1
EAT_AMOUNT_COD = 0.25
BASE_BIOMASS_LOSS = 0.05
BIOMASS_GROWTH_RATE = 0.1
PLANKTON_GROWTH_RATE = 0
MAX_PLANKTON_IN_CELL = (STARTING_BIOMASS_PLANKTON / (WORLD_SIZE * WORLD_SIZE)) * 1.5
ENERGY_FROM_BIOMASS = 0.5
MAX_ENERGY = 100.0

NUM_AGENTS = 24
ELITISM_SELECTION = 8
TOURNAMENT_SELECTION = 4
BASE_ENERGY_COST = 1
GENERATIONS_PER_RUN = 25

OFFSETS_TERRAIN_LAND = 0
OFFSETS_TERRAIN_WATER = 1
OFFSETS_TERRAIN_OUT_OF_BOUNDS = 2

OFFSETS_BIOMASS = OFFSETS_TERRAIN_OUT_OF_BOUNDS + 1

OFFSETS_BIOMASS_PLANKTON = OFFSETS_BIOMASS
OFFSETS_BIOMASS_ANCHOVY = OFFSETS_BIOMASS + 1
OFFSETS_BIOMASS_COD = OFFSETS_BIOMASS + 2

OFFSETS_ENERGY = OFFSETS_BIOMASS_COD + 1

OFFSETS_ENERGY_PLANKTON = OFFSETS_ENERGY
OFFSETS_ENERGY_ANCHOVY = OFFSETS_ENERGY + 1
OFFSETS_ENERGY_COD = OFFSETS_ENERGY + 2

CURRENT_FOLDER = "results/run"

def override_from_file(file_path):
    global WORLD_SIZE
    global STARTING_BIOMASS_COD
    global STARTING_BIOMASS_ANCHOVY
    global STARTING_BIOMASS_PLANKTON
    global MIN_PERCENT_ALIVE
    global MAX_STEPS
    global EAT_AMOUNT
    global EAT_AMOUNT_ANCHOVY
    global EAT_AMOUNT_COD
    global BASE_BIOMASS_LOSS
    global BIOMASS_GROWTH_RATE
    global PLANKTON_GROWTH_RATE
    global MAX_PLANKTON_IN_CELL
    global ENERGY_FROM_BIOMASS
    global MAX_ENERGY
    global NUM_AGENTS
    global ELITISM_SELECTION
    global TOURNAMENT_SELECTION
    global BASE_ENERGY_COST
    global GENERATIONS_PER_RUN
    
    global CURRENT_FOLDER
    file_name = os.path.basename(file_path).split(".")[0]

    CURRENT_FOLDER = f"results/{file_name}"
    if not os.path.exists(CURRENT_FOLDER):
        os.makedirs(CURRENT_FOLDER)
        if not os.path.exists(f"{CURRENT_FOLDER}/agents"):
            os.makedirs(f"{CURRENT_FOLDER}/agents")

    with open(file_path, "r") as f:
        for line in f:
            key, value = line.strip().split("=")
            if key in globals():
                globals()[key] = type(globals()[key])(value)
    
    print(f"Overridden constants from file {file_path}")
    print(f"NUM_AGENTS: {NUM_AGENTS}")



