def copyStats(entity):
    attack = entity.attack
    magic = entity.magic
    defense = entity.defense
    resistance = entity.resistance
    speed = entity.speed
    stats = [attack,magic,defense,resistance,speed]
    return stats

def pasteStats(entity, stats: list):
    entity.attack = stats[0]
    entity.magic = stats[1]
    entity.defense = stats[2]
    entity.resistance = stats[3]
    entity.speed = stats[4]
    return entity
    
