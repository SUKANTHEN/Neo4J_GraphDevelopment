CREATE TABLE departments (
    department_id int PRIMARY KEY,
    name varchar(255)
)

INSERT INTO departments (department_id, name)
VALUES
    (1, 'Management'),
    (2, 'Data'),
    (3, 'Engineering'),
    (4, 'Products');
