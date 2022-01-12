from db_config import cursor
from excel_config import sheet

# Makin a for loop to iterate through the rows
rows = sheet.max_row;
id = 5678;

for row in range(1, rows):
    nomcidade = sheet['E'+str(row)].value;
    txtuf = sheet['D'+str(row)].value;
    codpais = "32";
    
    # Checking if the city already exists in the database
    cursor.execute("SELECT codcidade FROM Teste_Cidade WHERE nomcidade = ? AND txtuf = ?", nomcidade, txtuf);
    result = cursor.fetchone();

    if (result == None):
        # Inserting data into the database
        cursor.execute("INSERT INTO Teste_Cidade (codcidade, nomcidade, txtuf, codpais)" +
                        "VALUES (?, ?, ?, ?)", id, nomcidade, txtuf, codpais);
        cursor.commit();
        id += 1;