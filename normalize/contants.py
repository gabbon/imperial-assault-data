TRUE_FALSE_CHOICES = [
    (False, 'False'),
    (True, 'True'),
]


class GAME_MODES:
    CAMPAIGN = 'Campaign'
    SKIRMISH = 'Skirmish'

    as_choices = [
        (CAMPAIGN, CAMPAIGN),
        (SKIRMISH, SKIRMISH),
    ]

    as_list = [
        CAMPAIGN,
        SKIRMISH
    ]


class SOURCES:
    SOURCE = 'sources'
    SOURCE_CONTENTS = 'source-contents'
    SKIRMISH_MAP = 'skirmish-maps'
    AGENDA = 'agenda-cards'
    AGENDA_DECKS = 'agenda-decks'
    COMMAND = 'command-cards'
    CONDITION = 'condition-cards'
    DEPLOYMENT = 'deployment-cards'
    HERO = 'heroes'
    HERO_CLASS = 'hero-class-cards'
    IMPERIAL_CLASSES = 'imperial-classes'
    IMPERIAL_CLASS_CARD = 'imperial-class-cards'
    SUPPLY = 'supply-cards'
    STORY_MISSION = 'story-mission-cards'
    SIDE_MISSION = 'side-mission-cards'
    REWARD = 'rewards-cards'
    COMPANION = 'companion-cards'
    UPGRADE = 'upgrade-cards'
    CARD = 'card-backs'
    THREAT_MISSION = 'threat-mission-cards'

    as_list = [
        SOURCE,
        SOURCE_CONTENTS,
        SKIRMISH_MAP,
        AGENDA,
        AGENDA_DECKS,
        COMMAND,
        CONDITION,
        DEPLOYMENT,
        HERO,
        HERO_CLASS,
        IMPERIAL_CLASSES,
        IMPERIAL_CLASS_CARD,
        SUPPLY,
        STORY_MISSION,
        SIDE_MISSION,
        REWARD,
        COMPANION,
        UPGRADE,
        CARD,
        THREAT_MISSION,
    ]


class AFFILIATION:
    REBEL = 'Rebel'
    IMPERIAL = 'Imperial'
    MERCENARY = 'Mercenary'
    NEUTRAL = 'Neutral'

    as_choices = [
        (REBEL, REBEL),
        (IMPERIAL, IMPERIAL),
        (MERCENARY, MERCENARY),
        (NEUTRAL, NEUTRAL),
    ]


class CARD_TRAITS:
    SPY = 'Spy'
    BRAWLER = 'Brawler'
    FORCE_USER = 'Force User'
    SKIRMISH_UPGRADE = 'Skirmish Upgrade'
    WOOKIEE = 'Wookiee'
    GUARDIAN = 'Guardian'
    TROOPER = 'Trooper'
    CREATURE = 'Creature'
    HEAVY_WEAPON = 'Heavy Weapon'
    LEADER = 'Leader'
    SMUGGLER = 'Smuggler'
    VEHICLE = 'Vehicle'
    HUNTER = 'Hunter'
    DROID = 'Droid'

    as_choices = (
        (SPY, SPY),
        (BRAWLER, BRAWLER),
        (FORCE_USER, FORCE_USER),
        (SKIRMISH_UPGRADE, SKIRMISH_UPGRADE),
        (WOOKIEE, WOOKIEE),
        (GUARDIAN, GUARDIAN),
        (TROOPER, TROOPER),
        (CREATURE, CREATURE),
        (HEAVY_WEAPON, HEAVY_WEAPON),
        (LEADER, LEADER),
        (SMUGGLER, SMUGGLER),
        (VEHICLE, VEHICLE),
        (HUNTER, HUNTER),
        (DROID, DROID),
    )


DEPLOYMENT_CARD_PREFERRED_ATTR_ORDER = [
    "id",
    "name",
    "description",
    "elite",
    "unique",
    "affiliation",
    "traits",
    "modes",
    "deployment_cost",
    "reinforce_cost",
    "deployment_group",
    "image",
    "image_file",
    "source",
]
