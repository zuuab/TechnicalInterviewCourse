**CI/CD Questions**

1. What is CI/CD? What are some good CI/CD practices?
    - CI stands for continuous integration. This concept ensures the regular building and testing of a program. CD stands for continuous delivery. This concept refers to the ongoing development of a program ahead of production. Good practices include the following principles:
        - Commit early, commit often
        - Keep the builds green
        - Build only once
        - Streamline your tests
        - Clean your environments
        - Make it the only way to deploy to production
        - Monitor and measure your pipeline
        - Make it a team effort

2. What are the differences between continuous integration, continuous delivery, and continuous deployment?
    - Continuous integration ensures the regular building and testing of a program. Continuous delivery ensures the ongoing development of a program ahead of production. Lastly, continuous deployment ensures your code is constantly being deployed to dev, stage, and prod environments with appropriate test checks.

3. What is blue/green deployment?
    - This is a continuous integration technique that consists of having two identical production environments. One of the environments is deployed and is in immediate use. The other environment is updated with new features and also tested. When the tests are successful the team will swithc from the first environment to the second environment.

**Cloud Questions**

1. What does high availability mean?
    - The ability of a system to be running with no failures for a given amount of time.

2. What does high durability mean?
    - The ability of a storage service to safely store data without losing data.

3. What does cloud hosting mean?
    - The use of computer system resources without direct management by a user.

**Containerization Questions**

1. What is containerization?
    - Containerization is a form of virtualization in which programs are run in contianers that utilize the underlying power of an operating system.

2. What are the benefits of Docker?
    - Docker allows you to run applications across varying operating systems without needing to constantly change code and configurations. It also allows applications to be deployed and scaled with relative ease.

**Database and SQL Questions**

1. What is a NoSQL database and what are some use cases for one?
    - Unlike a relational database, a NoSQL database does not use tables to organize its data. Data is stored in objects that can vary in size, structure, and types.
    - NoSQL databases are a good choice when:
        - You have a large volume and variety of data
        - Scalability is a top priority
        - You need continuous availability
        - Working with big data or performing real-time analytics
    - For example a NoSQL database would be good for Internet of things (IoT) and sensor data or a messaging service.

2. What is SQL injection?
    - SQL injection is the placement of malicious code in SQL statements, via web page input.
    - SQL injection is a code injection technique that might destroy your database.
    - SQL injection is one of the most common web hacking techniques.

3. What is the difference between JOIN and UNION?
    - A JOIN is used to combine data from two tables based off a related column. On the otherhand, a UNION is used to combine two result SELECT statements together.

4. If you have a limited amount of memory, how would you handle a large amount of data?
    - When processing the data one could split the data into smaller portions. However, at a certain point you might need to allocate more memory to process a large amount of data. You could also use a big data platform such as Hadoop.

5. What does normalization mean in reference to datbases?
    - Normalization is the restructuring of a relational databases based on a series of rules called forms. 
        - First Normal Form: Each table cell should contain a single value. Each record needs to be unique.
        - Second Normal Form: Be in first normal form. Single Column Primary Key that are not functionally dependant on any subset of candidate key relations.
        - Third Normal Form: Be in first two normal forms. Also, the database has no transitive functional dependencies.

7. How do you improve a database query?
    - Avoid multiple joins in a single query
    - Eliminate cursors from the query 
    - Creation and use of indexes
    - Drop unused indexes

8. What is an ORM?
    - ORM stands for Object Relational Mapping. An ORM convert incompatible data types. An ORM creates virtual objects. For example, MYSQL is transformed into an object that can be stored and altred in a programming language.

9. What is DOA?
    - DOA provides an abstract interface for a database. By mapping application calls by an additional layer, the DAO provides data operations without exposing details of the database.

10. What is the ACID property of a system?
    - ACID stands for atomicity, consistency, isolation, and durability. These principles are applied to databases and their transactions. Atomicity means that each transaction is a single unit that happens once or doesn't happen at all. Consistency means the database should be consistent before and after a transaction. Isolation means that multiple transactions can happen the same time on a database without changing the consistency of a database. Durability means the data of a database or stored and peristent after transactions.

**Data Structure Questions**

1. What is and what are the benefits of using a graph?
    - A graph is a set of nodes (vertices) and a set of connections (edges) which define relations between nodes. The graph allows one to represent spefic domains such as city layouts or networks as a data structure. A major advantage of using a graph is one can apply graph algorithms to the graph.
        - Space Complexity
            - Adjacency Matrix: O(V^2)
            - Adjacency List: O(V+E)
            - Edges List: O(E)
        - Time Complexity
            - Connection Checking
                - Adjacency Matrix: O(1)
                - Adjacency List: O(N)
                - O(E)
            - Neighbors Findiing
                - Adjacency Matrix: O(V)
                - Adjacency List: O(N)
                - Edges List: O(E)

2. What is and what are the benefits of using a binary tree?
    - A binary tree is a hierarchical tree-based data structure in which each node has at most two children. The root node is the top most node of the tree. Each node can have a left or right node. Links between nodes are called branches. A node without children nodes are called leaf nodes. The main advantage of a binary tree is simplicity. They are used to reflect relationships between data and can store an arbitrary number of data values.
        - Access: O(log(n))
        - Search: O(log(n))
        - Insertion: O(log(n))
        - Deletion O(log(n))

3. What is and what are the benefits of using a tuple?
    - A tuple is a fixed data structure that usually allows one to store two values. The data structure is often immutable and cannot be changed once they are assigned. Python has a built in tuple data structure.
        - Time Complexity
            - Find an element: O(1)

4. What is and what are the benefits of using a set?
    - A set is a data structure that can store any number of unique values. The major benefit of a set is that it does not store duplicate values. Sets reduce the amount of need to check for duplicates. 
        - Time Complexity
            - O(log(n)) or O(1)

5. What is and what are the benefits of using a dictionary?
    - 
6. What is and what are the benefits of using a linked list?
    - 
7. What is and what are the benefits of using a doubley linked list?
    - 
8. What is and what are the benefits of using an array?
    - 
9. What is the difference between a breadth-first search and a depth-first search?
    - 
10. How does a merge sort work? What is its time complexity?
    - 
11. How does a quick sort work? What is its time complexity?
    - 
12. Define “stack” and “heap.” What is a stack overflow?
    - 
13. How does an array differ from a stack?
    - 
14. What is the difference between FIFO and LIFO?
    - FIFO stands for first in first out. A queue is an example of the FIFO principle. Elements are placed in a queue and the first element place in the queue is the next to be removed. LIFO stands for last in first out. A stack is an example of the LIFO principle. Elements are placed on the stack and the most recently placed element is the element next removed from a stack.

15. What is and what are the benefits of using an queue? 
    - 

**Framework Questions**

1. What does REST stand for?
    - REST stands for Representational State Transfer. After a client requests a resource, a RESTful API will transfer a representation of the state of the requested resource to the client. 

2. What are the DRY and DIE principles? Give an example.
    - 
3. Name some best practices for RESTful API design?
    - 
4. What is an MVC framework? Pros and cons?
    - 
5. What is an MVVM framework? Pros and cons?
    - 
6. What is CAP theorem?
    - 
7. What does SOLID mean?
    - SOLID is a collection of five common software design principles. The acronym stands for Single Responsibility Property, Open-Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, and Dependency Inversion Principle.
        - Single Responsibility Property: Every class and module should only have one responsibilty.
        - Open-Closed Principle: Classes should be built in a way that one does not need to change the class, but just extend the class.
        - Liskov Substitution Principle: Every derived class should be substitutable for its parent class.
        - Interface Segregation Principle: It is better to have a lot of smaller interfaces than a few larger interfaces.
        - Dependency Inversion Principle: This principle offers a way to decouple software modules. Developers should depend on abstractions (use of intefaces), not on concretions (direct use of classes).
8. What is Agile development?
    - 

**Language Questions**

1. How is Python interpreted?
    - 
2. How is C interpreted?
    - 
3. How is Java interpreted?
    - 
5. What is strong-typing and weak-typing? Which is preferred? Why?
    - 

**Miscellaneous Questions**

1. What is regex?
    - Regex stands for regular expression. Regex is a sequence of characters that specifies a search pattern in text. The expression is used to match, locate, and adjust text. The following is a regex example that can be used to match a phone number: "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$". 

2. What is the difference between git fetch and rebase and git pull?
    - 

**Object Oriented Programming Questions**

1. What is encapcilation? Give an example.
    - 
2. What is inheritance? Give an example.
    - 
3. What is abstraction? Give an example.
    - 
4. What is polymorphism? Give an example.
    - 
5. What do you think makes object-oriented design the preferred approach?
    - 

**Opinion Questions**
1. What is difficult about writing code?
    - 
2. What programming languages do you like to work with and why?
    - 
3. What is your approach to debugging?
    - 
4. What is your most challenging project?
    - 
5. Why would you use microservice architecture?
    - 
6. What’s important when checking a team member’s code?
    - 

**Programming Questions**

1. What is a class?
    - 
2. What is a clousure?
    - 
3. What do classes and closures have in common?
    - 
4. What is an interface?
    - 
5. What is a tirnary function?
    - 
6. What is the difference between a function and a method?
    - 
7. What is an anynomous function? Why are they useful?
    - 
8. What is a callback function?
    - 
9. What is functional programming?
    - 
10. What is a generic?
    - 
11. What is an abstract class?
    - 

**Software Design Questions**

1. What is and when would you apply asynchronous communication between two systems?
    - 
2. What does the term seperation of concerns mean?
    - 
3. What is the difference between Request/Reply and Publish/Subscribe models?
    - 
4. When should one scale up vs scale out?
    - 
5. Why would you choose a microservice approach vs a monolithic app?
    - 
6. Explain the differences between a Thread and a Process?
    - 
7. What is the meaning of “high cohesion” and “loose coupling”?
    - 
8. What is a reverse proxy?
    - 
9. What is a thread?
    - 
10. What is lazy loading? Give an example of using this principle.
    - 
11. What is tight coupling?
    - 
12. When should one use memoization?
    - 
13. What is caching?
    - A cache is a data storage layer which stores a subset of data, so that future requests for that data can be accessed faster than through the data’s primary storage location.

**Software Design Pattern Questions**

1. What is a singleton? Give an example of when to use this principle
    - 
2. What is a factory? Give an example of when to use this principle
    - 
3. What is an adapter design pattern?
    - 
4. What is a builder design pattern?
    - 
5. What is an observer design pattern?
    - 
6. What is a strategy design pattern?
    - 

**Test Questions**

1. What is a unit test?
    - A unit test tests one element or module in a computer program or application.

2. What is an integration test?
    - An integration test tests a group of elements or modules in a computer program or application. The test combines modules in order to validate the interactions between varying components.

3. What does it mean to mock a test? When should or shouldn't you mock a test?
    - 

**Web Questions**

1. What is a JWT? How does it work?
    - 
2. What are advantages of Web Services?
    - 
3. What is a sticky session?
    - 
4. What are and how does SSL/TLS work?
    - 
5. What is JavaScript and why is it used?
    - 
6. Define and explain these nine server response error codes: 200, 201, 204, 301, 400, 401, 404, 409 and 500
    - 200: 'Okay' or successful.
    - 201: 'Created'. The message means a resource was created at the client's request.
    - 204: 'No Content'. The message means the server didn't send back a status.
    - 301: 'Moved Permanently'. The message means a client-triggered action changed the resource location.
    - 400: 'Bad Request'. The error refers to a client-side error. 
    - 402: 'Unathorized'. The client did provide the correct authentication.
    - 404: 'Not Found'. The error means no mapped resource was found. 
    - 409: 'Conflict'. An inconsistent or impossible state.
    - 500: 'Internal Server Error'. This error indicates a server-side issue.

7. What does statelessness mean in regards to web services?
    - 
8. What is a TCP socket?
    - TCP sockets provide an open bi-directional connection between a client and server socket. The connection is uniquely identified using the combination of the client socket and server socket. The combination contains four elements: the client IP address and port, and the server IP address and port. For example, an HTTP request can be sent from the client socket 120.1.1.1:3022 from to the server socket 189.1.1.1:80. Major advantages of a TCP socket connection is that packets dropped in the network are detected and retransmitted by the sender and data is read in the order it was written by the sender.

9. What are some ways to make websites faster?
    - 

The following websites were used to gather questions as well as answer the provided questions:
- https://procoders.tech/blog/back-end-engineer-interview-questions/
- https://www.jetbrains.com/teamcity/ci-cd-guide/ci-cd-best-practices/
- https://github.com/arialdomartini/Back-End-Developer-Interview-Questions
- https://en.wikipedia.org/wiki/Cloud_computing
- https://www.datastax.com/blog/sql-vs-nosql-whats-the-difference
- https://www.w3schools.com/sql/sql_injection.asp
- https://www.indeed.com/career-advice/interviewing/back-end-interview-questions
- https://machinelearningmastery.com/large-data-files-machine-learning/
- https://www.sqlshack.com/what-is-database-normalization-in-sql-server/
- https://www.guru99.com/database-normalization.html
- https://www.developer.com/database/10-ways-to-improve-sql-query-performance/
- https://en.wikipedia.org/wiki/Data_access_object
- https://www.redhat.com/en/topics/api/what-is-a-rest-api
- https://www.geeksforgeeks.org/acid-properties-in-dbms/
- https://www.bmc.com/blogs/solid-design-principles
- https://www.codementor.io/@zmitry/graph-data-structure-for-web-developers-10xf9a93hs
- https://www.baeldung.com/cs/graphs
- https://www.baeldung.com/cs/binary-trees-vs-linked-lists-vs-hash-tables
- https://intellipaat.com/blog/tutorial/python-tutorial/python-tuple/
- https://www.howtouselinux.com/post/tcp-socket
- https://en.wikipedia.org/wiki/Regular_expression
- https://ihateregex.io/expr/phone/
- https://aws.amazon.com/caching/


