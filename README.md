
# Neo4J Graph Creation

### 1. Setting Up PostgreSQL Docker

*  Download Docker images from official DockerHub repo.

       docker pull postgres

* Run the docker in port 5432 and setup credentials.

      docker run --name postgres-container -e  POSTGRES_PASSWORD=<password> -d -p 5432:5432 postgres

* Once the docker is built and running, create a user `Sukan` with SuperUser access. 

* Access the PostgreSQL container and start a psql (PostgreSQL interactive terminal) using user as postgres

      docker exec -it postgres-container psql -U postgres -d postgres

* Run the below script inside psql terminal. This will create a new user sukan for PostgreSQL DB.

      CREATE USER sukan WITH SUPERUSER PASSWORD "[your_pwd]";



### 2. DB data Upload and CSV Export

* Now, once created, do a test connection and if connection established successfully, run the `db/upload_data.py`, which takes a SQL query as input and created a table inside the specified DB.

* The DB is running with the required `employees` and `department` tables. Hence, we will export the data as separate csv files using the `db/export_csv.py`


### 3. Setting Up Neo4J Docker

* Download Neo4J images from official DockerHub repo.
             
      docker pull neo4j


* Run the pulled docker image using the following command

          
        docker run -p 7474:7474 -p 7687:7687 \ 
        --volume=/Users/sukan/Downloads/graph_data/data:/data \  
        --volume=/Users/sukan/Downloads/graph_data/assignment-2/data:/var/lib/neo4j/import \  --env NEO4JLABS_PLUGINS='["apoc", "graph-data-science"]' \  
        --env apoc.import.file.enabled=true \
        --env NEO4J_AUTH=neo4j/sukan@1234 \ 
        neo4j:latest


### 4. Create Graph using Cypher Query

* Run the Cypher query present in `cypher_query/query.cql` file. This query will create the necessary graph as shown in `results/` folder. 

