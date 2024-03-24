import sys
sys.path.append('/Users/Mefyod-EA/Documents/my_projects')
from dmz_desc import dictionary
with open('/Users/Mefyod-EA/Documents/my_projects/IN_DMZ.txt', 'r') as file:
    with open('/Users/Mefyod-EA/Documents/my_projects/OUT_DMZ.txt', 'w') as output_file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            el = line.split('.')
            module = el[2]
            uso_kc = el[3].split('_')
            if uso_kc[0] == 'USO':
                uso_str = f'УСО {uso_kc[1]}, корзина {uso_kc[2]}, канал {uso_kc[3]}'
            elif uso_kc[0] == 'KC':
                uso_str = f'КЦ {uso_kc[1]}, канал {uso_kc[2]}'
            else:
                uso_str = 'RACKSTATE'
            desc = el[4]
            desc_key = dictionary.get(desc)
            print(uso_kc)
            output_file.write(f'Модуль {module}, {uso_str}, {desc_key}  \n')
            print(line)




 #Root.Diag.DOs.USO_4_A2_05.ch_DI_28.ch_Kont