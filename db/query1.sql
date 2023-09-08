-- Create the "employees" table and insert the data into the created table
CREATE TABLE employees (
    employee_id serial PRIMARY KEY,
    full_name varchar,
    job_title varchar,
    manager_id int,
    department_id int,
    collaborator_id int
)

INSERT INTO employees (employee_id, full_name, job_title, manager_id, department_id, collaborator_id)
VALUES
    (1, 'John Doe', 'CEO', 1, 1, NULL),
    (2, 'Jane Smith', 'CTO', 1, 1, NULL),
    (3, 'Jim Brown', 'Data Analyst', 2, 2, 4),
    (4, 'Judy White', 'Data Scientist', 2, 2, 3),
    (5, 'Joe Black', 'Sr. Software Eng.', 2, 3, 6),
    (6, 'Jennifer Green', 'Software Eng.', 5, 3, 5),
    (7, 'Jason Blue', 'Product Manager', 1, 4, 8),
    (8, 'Jane Orange', 'Product Designer', 7, 4, 7);
