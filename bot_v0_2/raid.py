import gspread
import sqlite3
import config
import pandas as pd
import pylab

conn = sqlite3.connect('raid.db')
cursor = conn.cursor()

def raid_obr(akronim):
    gc = gspread.service_account(filename=config.data_gdoc[akronim]);
    sh = gc.open(config.name_gdoc[akronim]);
    worksheet = sh.worksheet("RaidExport");
    number_raid = int(worksheet.cell(1, 1).value);
    exl=worksheet.col_values(number_raid+1);
    exl[3] = '-'.join(reversed(exl[3].split('/')))

    cursor.execute("DELETE FROM 'Pred_{}'".format(akronim))
    conn.commit();

    max_boss = 0;
    max_attack = 0;
    boss_hp = {}
    boss_hp_miss={}
    person_damage = {}
    for i in range(8):
        boss_hp[i]=[]
        boss_hp_miss[i]=[0,0,0,0,0,0,0,0]
    for i in range(8):
        for j in range(25):
            boss_hp[i].append(0);
    sch=3
    for i in range(6,len(exl)):
        raid_mass = exl[i].split(",");
        raid_mass[0]=raid_mass[0].replace("'", "")

        cursor.execute("insert into 'Raid_{}' values ({},{},{},{},{},'{}','{}',{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(akronim,number_raid,exl[3],int(exl[0]),int(exl[1]),int(exl[2]),raid_mass[0],raid_mass[1],int(raid_mass[2]),int(raid_mass[3]),raid_mass[4],int(raid_mass[5]),int(raid_mass[6]),int(raid_mass[7]),int(raid_mass[8]),int(raid_mass[9]),int(raid_mass[10]),int(raid_mass[11]),int(raid_mass[12]),int(raid_mass[13]),int(raid_mass[14]),int(raid_mass[15]),int(raid_mass[16]),int(raid_mass[17]),int(raid_mass[18]),int(raid_mass[19]),int(raid_mass[20]),int(raid_mass[21]),int(raid_mass[22]),int(raid_mass[23]),int(raid_mass[24]),int(raid_mass[25]),int(raid_mass[26]),int(raid_mass[27]),int(raid_mass[28]),int(raid_mass[29])))
        conn.commit(); #import data in sql
        person_damage[raid_mass[1]]=[]
        person_damage[raid_mass[1]]=[raid_mass[0],int(raid_mass[2]),0,0]
        if sch==3:
            cursor.execute("insert into 'Pred_{}' values ('{}','{}',2,'2022-04-24')".format(akronim, raid_mass[0],raid_mass[1]))
            sch=0
        else:
            sch+=1
        if max_boss < int(raid_mass[3]):
            max_boss = int(raid_mass[3]);
        if max_attack < int(raid_mass[2]):
            max_attack = int(raid_mass[2]);
        for j in range(5,30):
            boss_hp[int(raid_mass[3])][j-5]+=int(raid_mass[j])

    for i in range(8):
        for j in range(8):
            if boss_hp[i][j+9]<1000000:
                boss_hp_miss[i][j]=1;

    for i in range(6,len(exl)):
        raid_mass = exl[i].split(",");
        raid_mass[0]=raid_mass[0].replace("'", "")
        person_damage[raid_mass[1]][2]+=int(raid_mass[5])
        for j in range(8):
            person_damage[raid_mass[1]][3]+=(int(raid_mass[j+6])+int(raid_mass[j+6+8]))*boss_hp_miss[int(raid_mass[3])][j]

    if (max_attack%4 == 0):
        max_attack=max_attack-4
    else:
        max_attack=max_attack-(max_attack%4)

    for key in person_damage:
        if person_damage[key][2]==0:
            person_damage[key].append(0)
        else:
            person_damage[key].append(100*person_damage[key][3]/person_damage[key][2])
        if person_damage[key][1]==0:
            person_damage[key].append(0)
        else:
            person_damage[key].append(person_damage[key][2]/person_damage[key][1]/1000000)
        if person_damage[key][1]>max_attack:
            person_damage[key].append(100)
        else:
            person_damage[key].append(100*person_damage[key][1]/max_attack)
    raid_data = pd.DataFrame.from_dict(person_damage, orient='index')

    

    cursor.execute("SELECT * FROM Pred_{}".format(akronim))
    pred = cursor.fetchall()
    mass_pred=[]
    df_pred = pd.DataFrame(pred)
    for i in pred:
        mass_pred.append(i[1])
    df_pred.index=mass_pred
    print(len(df_pred[df_pred.index == "g8wn268"]))
    print(len(df_pred[df_pred.index == "g8wn267"]))
    #print(raid_data)

    print_table(raid_data)
    return("ok")


def print_table(data):
    pylab.table(cellText=data.values, rowLabels=data.index,colLabels=data.columns, loc="upper center")
    pylab.axis("off")
    pylab.savefig('saved_figure.png', dpi = 1000)
