import sqlite3

def createTable_Raid(nameTable):
    conn = sqlite3.connect('raid.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Raid_{}` (NumberRaid INTEGER, DataRaid DATE, TierRaid INTEGER, LvlRaid INTEGER, MoralRaid INTEGER, PlayerName TEXT, PlayerCode TEXT, TotalRaidAttacks INTEGER, TitanNumber INTEGER, TitanName TEXT, TitanDamage INTEGER, ArmorHead INTEGER, ArmorTorso INTEGER, ArmorLeftArm INTEGER, ArmorRightArm INTEGER, ArmorLeftHand INTEGER, ArmorRightHand INTEGER, ArmorLeftLeg INTEGER, ArmorRightLeg INTEGER, BodyHead INTEGER, BodyTorso INTEGER, BodyLeftArm INTEGER, BodyRightArm INTEGER, BodyLeftHand INTEGER, BodyRightHand INTEGER, BodyLeftLeg INTEGER, BodyRightLeg INTEGER, SkeletonHead INTEGER, SkeletonTorso INTEGER, SkeletonLeftArm INTEGER, SkeletonRightArm INTEGER, SkeletonLeftHand INTEGER, SkeletonRightHand INTEGER, SkeletonLeftLeg INTEGER, SkeletonRightLeg INTEGER)".format(nameTable))
    conn.commit()

def createTable_Pred(nameTable):
    conn = sqlite3.connect('raid.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Pred_{}` (PlayerName TEXT, PlayerCode TEXT, TotelPred INTEGER, DataLastPred DATE)".format(nameTable))
    conn.commit()

def createTable_Moral(nameTable):
    conn = sqlite3.connect('raid.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Moral_{}` (Date DATE, PlayerCode TEXT,PlayerName TEXT, Morale INTEGER, Role TEXT)".format(nameTable))
    conn.commit()

def create_new_clan(nameClan):
    createTable_Raid(nameClan);
    createTable_Pred(nameClan);
    createTable_Moral(nameClan);
    return("Table is OK");
