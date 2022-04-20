CREATE TABLE client (
        id SERIAL PRIMARY KEY,
        email CHAR(100) UNIQUE,
        pass VARCHAR NOT NULL,
        salt VARCHAR NOT NULL
    );
    
CREATE TABLE project (
        id  SERIAL PRIMARY KEY,
        client_id INT NOT NULL,
        name VARCHAR NOT NULL,
        canvas_state VARCHAR,
        type VARCHAR,
        FOREIGN KEY (client_id) REFERENCES client(id)
    );
    