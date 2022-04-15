import warnings
import matplotlib.pyplot as plt
import numpy as np
from fuzzy_expert.variable import FuzzyVariable
from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.inference import DecompositionalInference
warnings.filterwarnings("ignore")
variables = {
    "win": FuzzyVariable(
        universe_range=(0, 20),
        terms={
            "High": [(12, 0), (13, 0.3), (14,0.5),(15, 0.7), (16, 0.9),(18,1.0)],
            "Low": [(4, 1), (6, 0.8), (8,0.4),(10,0.2),(12,0)],
        },
    ),
    "kda": FuzzyVariable(
        universe_range=(0, 200),
        terms={
            "High": [(70, 0), (80, 0.3), (90, 0.5), (100, 0.6),(110,0.7),(120,0.8),(130,1)],
            "Low": [(30, 1), (40, 0.8), (50, 0.6), (60, 0.4),(70,0)],
        },
    ),
    "gold_per_min": FuzzyVariable(
        universe_range=(0, 20000),
        terms={
            "High": [(11000,0), (12000,0.2), (13000,0.6), (14000,0.8),(15000,1)],
            "Low": [(5000, 1), (6000, 0.7), (7000, 0.5), (8000, 0.3),(10000,0.1),(11000,0)],
        },
    ),
    "xp_per_min": FuzzyVariable(
        universe_range=(0, 20000),
        terms={
            "High": [(13000,0), (14000,0.2), (15000,0.6), (16000,0.8),(17000,1)],
            "Low": [(7000, 1), (8000, 0.8), (9000, 0.6), (10000, 0.4),(11000,0.2),(13000,0)],
        },
    ),
    "hero_damage": FuzzyVariable(
        universe_range=(0, 1000000),
        terms={
            "High": [(600000,0),(700000,0.4), (800000,0.8), (900000,1)],
            "Low": [(200000, 1), (300000, 0.7), (400000, 0.5), (500000, 0.3),(600000,0)],
        },
    ),
    "smurf": FuzzyVariable(
        universe_range=(0, 1),
        terms={
            "High": [(0.4, 0), (0.6, 0.3), (0.8, 0.7), (1, 1)],
            "Low": [(0, 1), (0.1, 0.7), (0.3, 0.3), (0.4, 0)],
        },
    ),
}
rules = [
    FuzzyRule(
        premise=[
            ("kda", "High"),
            ("AND", "win", "High"),
        ],
        consequence=[("smurf", "High")],
    ),
    FuzzyRule(
        premise=[
            ("hero_damage", "High"),
            ("AND", "xp_per_min", "High"),
            ("AND", "gold_per_min", "High"),
        ],
        consequence=[("smurf", "High")],
    ),
    FuzzyRule(
        premise=[
            ("win", "Low"),
            ("OR", "kda", "Low"),
        ],
        consequence=[("smurf", "Low")],
    ),
    FuzzyRule(
        premise=[
            ("xp_per_min", "Low"),
            ("OR", "gold_per_min", "Low"),
        ],
        consequence=[("smurf", "Low")],
    )
]

model = DecompositionalInference(
    and_operator="min",
    or_operator="max",
    implication_operator="Rc",
    composition_operator="max-min",
    production_link="max",
    defuzzification_operator="cog",
)

plt.figure(figsize=(15, 15))
model.plot(
    variables=variables,
    rules=rules,
    win=10,
    kda=87,
    gold_per_min=6755,
    xp_per_min=10052,
    hero_damage=448411,
)
plt.savefig('normal_result.png')