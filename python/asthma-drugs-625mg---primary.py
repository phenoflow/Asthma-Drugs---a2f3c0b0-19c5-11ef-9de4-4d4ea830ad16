# Evangelos Kontopantelis, David Springate, David Reeves, Darren M Ashcroft, Jose M Valderas, Tim Doran, 2024.

import sys, csv, re

codes = [{"code":"4640","system":"gprdproduct"},{"code":"7972","system":"gprdproduct"},{"code":"674","system":"gprdproduct"},{"code":"23269","system":"gprdproduct"},{"code":"4634","system":"gprdproduct"},{"code":"1957","system":"gprdproduct"},{"code":"4100","system":"gprdproduct"},{"code":"2158","system":"gprdproduct"},{"code":"4647","system":"gprdproduct"},{"code":"964","system":"gprdproduct"},{"code":"15765","system":"gprdproduct"},{"code":"1422","system":"gprdproduct"},{"code":"5898","system":"gprdproduct"},{"code":"1414","system":"gprdproduct"},{"code":"14603","system":"gprdproduct"},{"code":"12822","system":"gprdproduct"},{"code":"37612","system":"gprdproduct"},{"code":"34018","system":"gprdproduct"},{"code":"35557","system":"gprdproduct"},{"code":"31082","system":"gprdproduct"},{"code":"18988","system":"gprdproduct"},{"code":"510","system":"gprdproduct"},{"code":"1728","system":"gprdproduct"},{"code":"25339","system":"gprdproduct"},{"code":"5308","system":"gprdproduct"},{"code":"11046","system":"gprdproduct"},{"code":"34162","system":"gprdproduct"},{"code":"10958","system":"gprdproduct"},{"code":"1630","system":"gprdproduct"},{"code":"7965","system":"gprdproduct"},{"code":"45863","system":"gprdproduct"},{"code":"35744","system":"gprdproduct"},{"code":"40709","system":"gprdproduct"},{"code":"13365","system":"gprdproduct"},{"code":"5837","system":"gprdproduct"},{"code":"1711","system":"gprdproduct"},{"code":"3187","system":"gprdproduct"},{"code":"19350","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["asthma-drugs-625mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["asthma-drugs-625mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["asthma-drugs-625mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
