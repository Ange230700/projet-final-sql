//link js and sqlite3
var sqlite3 = require('sqlite3').verbose();

//connect the database
var database = new sqlite3.Database('C:\\xampp\\htdocs\\projet-final-sql-DevFlavio\\projet-final-sql\\SQLEmploye.db');

database.get("SELECT * FROM departement WHERE id = 1", (err, row) => {
    if (err){
        return console.error(err.message);
    }
    return console.log(row);
});

database.close();