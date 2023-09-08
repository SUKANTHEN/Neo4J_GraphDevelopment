// Create Employee nodes
LOAD CSV WITH HEADERS FROM 'file:///employee.csv' AS row
MERGE (e:Employee {employee_id: row.employee_id})
SET e.full_name = row.full_name,
    e.job_title = row.job_title;

// Create Department nodes
LOAD CSV WITH HEADERS FROM 'file:///department.csv' AS row
MERGE (d:Department {department_id: row.department_id})
SET d.name = row.name;

// Create relationships
LOAD CSV WITH HEADERS FROM 'file:///employee.csv' AS row
MATCH (e:Employee {employee_id: row.employee_id})
MATCH (d:Department {department_id: row.department_id})
MERGE (e)-[:BELONGS_TO]->(d);

// Create relationships
LOAD CSV WITH HEADERS FROM 'file:///employee.csv' AS row
WITH row WHERE row.manager_id IS NOT NULL
MATCH (e:Employee {employee_id: row.employee_id})
MATCH (m:Employee {employee_id: row.manager_id})
MERGE (e)-[:REPORTS_TO]->(m);
