# Tutorial: Creating a REST api with Kotlin + SpringBoot + JPA + Flyway

## Summary

It has been some time since I have used a Spring Boot repository and I thought today would be a good day to refresh this knowledge while I get to play around with **Flyway**.
In this tutorial we will learn how to create a small **Spring Boot** application using a **JPA Repository** and having Flyway to help us with the migrations.
All of this using this fun (see the reserved words for functions) language called **Kotlin**.

## Prerequisites

To follow this tutorial is necessary that you have installed Java, Kotlin and Gradle.
You can learn how to do it in [this post.](https://dev.to/grekz/setup-your-macos-for-java-development-with-multiple-java-versions-5djj)
Excellent! Now that you have what is needed, let's continue.

## Getting SpringBoot

You can get it with your vscode extension or from the [Spring Initializr page](https://start.spring.io/).
Make sure to select the next dependencies:

- Spring Web
- Spring Data JPA
- Spring DevTools
- Flyway Migration
- MySQL Driver
  After you download the generated zip file, unpack it and you can continue with the tutorial.
  _if you have some doubts on how to get your project going you can check out [this post.](https://dev.to/grekz/how-to-create-your-own-hello-world-rest-service-with-spring-boot-gradle-kotlin-409l)_

## Setting up your database

In order to persist our information we are going to use **Docker**. In case that you don't have this great tool already installed, you can check their website and [follow the steps to install.](https://docs.docker.com/docker-for-mac/install/)

Now that you have docker installed, you can input this command in your terminal:

```shell
docker run --rm --name test-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=kotlin_crud_db -d mysql:latest
```

After the previous step is completed we need to go to our folder, the one that we unzipped, that contains the Spring Boot application we just downloaded. And identify the `application.properties` file.

We will rename this file to `application.yml` and its content should be:

```yaml
## content of /src/main/resources/application.yml
spring:
  datasource:
    url: &dbURL jdbc:mysql://localhost:3306/kotlin_crud_db
    username: &dbUser root
    password: &dbPassword 123456
  jpa:
    properties:
      hibernate:
        dialect: org.hibernate.dialect.MySQL5InnoDBDialect
    hibernate:
      ddl-auto: update
```

Now we have configured our data source. To make sure we have everything running, let us go back to our terminal and type the next command:

```shell
gradle bootRun
```

Now you should see that in your terminal there was no error, and the spring boot app should be **EXECUTING**

## Create Flyway migrations

Now we need to create some migration scripts so they get run by Flyway.
In the folder `/src/main/resources/db/migration/` we'll create a file called `V1__CreateTableTasks.sql` with content:

```sql
CREATE TABLE IF NOT EXISTS tasks(
    id BIGINT(19) AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    start_date DATE,
    due_date DATE,
    status TINYINT NOT NULL,
    priority TINYINT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)  ENGINE=INNODB;
```

And we are going to create another script, in the same folder, called `V2__TestData.sql`:

```sql
insert into tasks(title, status, priority, description) values ('First Task', 1, 1, 'My first task description');
insert into tasks(title, status, priority, description) values ('Another Task', 2, 2, 'Another task description');
```

Now let's run the command:

```shell
gradle bootRun
```

If you want to check what happened in the Database, you can run the following commands:

```shell
docker exec -it test-mysql mysql -u root -p
```

You'll get prompted `Enter password:` and you need to input `123456` if you are following the tutorial exactly.
When you are inside the container you should see `mysql>`. Now you can type the next command:

```sql
mysql> use kotlin_crud_db;
mysql> select * from tasks;
mysql> select * flyway_schema_history;
```

## Create the model

Now let's create a folder in `/src/main/kotlin/com/example/demo` which is gonna be called `model`.
And we are going to create a new Kotlin data class called `Task`:

```kotlin
package com.example.demo.model

import java.time.LocalDateTime
import java.util.*
import javax.persistence.*

@Entity
@Table(name = "tasks")
data class Task(
        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        val id: Long? = null,
        val title: String,
        val description: String? = null,
        val startDate: Date? = null,
        val dueDate: Date? = null,
        val status: Int,
        val priority: Int,
        val createdAt: LocalDateTime? = LocalDateTime.now(),
        val updatedAt: LocalDateTime? = LocalDateTime.now()
)
```

## Create the JPA Repository

Now we need to create a [JPA Repository](https://docs.spring.io/spring-data/jpa/docs/2.2.5.RELEASE/reference/html/#jpa.repositories) where we are going to declare the `TaskRepository` Interface, this is going to exist in `/src/main/kotlin/com/example/demo/repository/TaskRepository.kt`:

```kotlin
package com.example.demo.repository

import com.example.demo.model.Task
import org.springframework.data.jpa.repository.JpaRepository
import org.springframework.stereotype.Repository
import javax.transaction.Transactional

@Repository
@Transactional(Transactional.TxType.MANDATORY)
interface TaskRepository : JpaRepository<Task, Long>
```

This will help us to handle all the interactions with the database for this tutorial. We are not going to write a single line of code to configure or to read anything from the database, besides the things we've already done.

## Create the service

After the Repository is created, now we need to create our Service that will be the layer where we are going to communicate our Resource with our Repository.
We will create a file in `/src/main/kotlin/com/example/demo/service/TaskService.kt`:

```kotlin
package com.example.demo.service

import com.example.demo.model.Task
import com.example.demo.repository.TaskRepository
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.stereotype.Service

@Service
class TaskService(private val taskRepository: TaskRepository) {

  fun getTasks(): List<Task> =
    taskRepository.findAll()

  fun addTask(task: Task): ResponseEntity<Task> =
    ResponseEntity.ok(taskRepository.save(task))

  fun getTaskById(taskId: Long): ResponseEntity<Task> =
    taskRepository.findById(taskId).map { task ->
      ResponseEntity.ok(task)
    }.orElse(ResponseEntity.notFound().build())

  fun putTask(taskId: Long, newTask: Task): ResponseEntity<Task> =
    taskRepository.findById(taskId).map { currentTask ->
      val updatedTask: Task =
        currentTask
          .copy(
            title = newTask.title,
            description = newTask.description,
            status = newTask.status,
            startDate = newTask.startDate,
            priority = newTask.priority,
            dueDate = newTask.dueDate
          )
      ResponseEntity.ok().body(taskRepository.save(updatedTask))
    }.orElse(ResponseEntity.notFound().build())

  fun deleteTask(taskId: Long): ResponseEntity<Void> =
    taskRepository.findById(taskId).map { task ->
      taskRepository.delete(task)
      ResponseEntity<Void>(HttpStatus.ACCEPTED)
    }.orElse(ResponseEntity.notFound().build())
}
```

## Create the resource (controller)

After creating the service we are going to tell the applcation how to map the different HTTP methods (GET, POST, PUT, DELETE).
In the file `/src/main/kotlin/com/example/demo/resource/TaskResource.kt`:

```kotlin
package com.grekz.crudKotlin.resource

import com.grekz.crudKotlin.model.Task
import com.grekz.crudKotlin.repository.TaskRepository
import com.grekz.crudKotlin.service.TaskService
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*
import javax.validation.Valid

@RestController
@RequestMapping("/v1/api/tasks")
class TaskResource(private val taskService: TaskService) {

  @GetMapping
  fun getTasks(): List<Task> =
    taskService.getTasks()

  @PostMapping
  fun addTask(@Valid @RequestBody task: Task): ResponseEntity<Task> =
    taskService.addTask(task)

  @GetMapping("/{id}")
  fun getTaskById(@PathVariable(value="id") taskId: Long): ResponseEntity<Task> =
    taskService.getTaskById(taskId)

  @PutMapping("/{id}")
  fun updateTaskById(
    @PathVariable(value = "id") taskId: Long,
    @Valid @RequestBody newTask: Task): ResponseEntity<Task> =
    taskService.putTask(taskId, newTask)

  @DeleteMapping("/{id}")
  fun deleteTask(@PathVariable(value = "id") taskId: Long): ResponseEntity<Void> =
    taskService.deleteTask(taskId)
}
```

## Ok, great. Now... how do I test this?

I will probably follow up this tutorial with how to implement tests in a project.
But in the meantime you can test it with some good ol' curls:

Here we can test the get where we return all the tasks:

```shell
$ curl --location --request GET 'localhost:8080/v1/api/tasks'
```

With this other curl we can test retrieve one single task:

```shell
$ curl --location --request GET 'localhost:8080/v1/api/tasks/1'
```

Now we can test creating a new task with the following command:

```shell
$ curl --location --request POST 'localhost:8080/v1/api/tasks/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title": "new 2nd task",
	"status": 1,
	"priority": 1,
	"description":"2244 blah blah task"
}'
```

In case you want to update the task:

```shell
$ curl --location --request PUT 'localhost:8080/v1/api/tasks/2' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title": "blah blah new 2nd task",
	"status": 1,
	"priority": 1,
	"description":"2244 blah blah task"
}'
```

And to delete the task that has the id=2 :

```shell
$ curl --location --request DELETE 'localhost:8080/v1/api/tasks/2'
```

## Final source code

[Just take me to the code already!](https://github.com/Grekz/example-kotlin-crud)
Alright my people, I hope you are staying safe in this COVID19 times.
We will get through this, hang in there.
