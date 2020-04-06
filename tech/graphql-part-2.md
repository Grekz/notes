# GraphQL + Kotlin & Spring Boot - Part 2

## Summary

Hey people! Today we are going to continue our Kotlin with GraphQL tutorials.
We are going to take as a code base https://github.com/Grekz/example-kotlin-crud that we did in our previous post [here.](https://dev.to/grekz/tutorial-creating-a-rest-api-with-kotlin-springboot-jpa-flyway-15j5)

## Test that the base code works

First let us make sure that you have everything ready. Input these command:

```bash
$ docker run --rm --name test-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=kotlin_crud_db -d mysql:latest
$ gradle bootRun
```

If you have trouble running it, make sure to follow the previous [post.](https://dev.to/grekz/tutorial-creating-a-rest-api-with-kotlin-springboot-jpa-flyway-15j5)

## Update the TaskService.kt file

First of all we need to do some changes in our TaskService, to reuse most of the code in our GraphQL Resolvers.

```kotlin
// .../kotlin/com/grekz/crudKotlin/service/TaskService.kt
package com.grekz.crudKotlin.service

import com.grekz.crudKotlin.model.Task
import com.grekz.crudKotlin.repository.TaskRepository
import org.springframework.stereotype.Service
import java.util.*

@Service
class TaskService(private val taskRepository: TaskRepository) {

  fun getTasks(): List<Task> =
    taskRepository.findAll()

  fun addTask(task: Task): Task = taskRepository.save(task)

  fun getTaskById(taskId: Long): Optional<Task> =
    taskRepository.findById(taskId)

  fun putTask(taskId: Long, newTask: Task): Optional<Task> =
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
      taskRepository.save(updatedTask)
    }

  fun deleteTask(taskId: Long): Boolean =
    taskRepository.findById(taskId).map { task ->
      taskRepository.delete(task)
      true
    }.orElse(false)
}
```

## Extra points... Update your TaskResource.kt

If you want to continue providing a RESTful API, we need to update the tasks resources:

```kotlin
package com.grekz.crudKotlin.resource

import com.grekz.crudKotlin.model.Task
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
    ResponseEntity.ok(taskService.addTask(task))

  @GetMapping("/{id}")
  fun getTaskById(@PathVariable(value = "id") taskId: Long): ResponseEntity<Task> =
    taskService.getTaskById(taskId).map { task ->
      ResponseEntity.ok(task)
    }.orElse(ResponseEntity.notFound().build())

  @PutMapping("/{id}")
  fun updateTaskById(
    @PathVariable(value = "id") taskId: Long,
    @Valid @RequestBody newTask: Task): ResponseEntity<Task> =
    taskService.putTask(taskId, newTask)
      .map { task -> ResponseEntity.ok().body(task) }
      .orElse(ResponseEntity.notFound().build())

  @DeleteMapping("/{id}")
  fun deleteTask(@PathVariable(value = "id") taskId: Long): ResponseEntity<Void> =
    if (taskService.deleteTask(taskId))
      ResponseEntity<Void>(HttpStatus.ACCEPTED)
    else
      ResponseEntity.notFound().build()
}
```

## Update the application yaml file

```yaml
## ../resources/application.yml
## ... Previous config ...
graphql:
  servlet:
    mapping: /graphql
    enabled: true
    corsEnabled: true
graphiql:
  mapping: /graphiql
  endpoint: /graphql
  enabled: true
  pageTitle: GraphiQL
  cdn:
    enabled: false
    version: 0.11.11
```

## Update your build.gradle.kts

```kotlin
// ... Previous config ...

dependencies {
	implementation("com.graphql-java:graphql-java-extended-scalars:1.0.1")
	implementation("com.graphql-java:graphql-spring-boot-starter:5.0.2")
	implementation("com.graphql-java:graphiql-spring-boot-starter:5.0.2")
	implementation("com.graphql-java:voyager-spring-boot-starter:5.0.2")
	implementation("com.graphql-java:graphql-java-tools:5.2.4")
    // ... Rest of the dependencied ...
}
```

## Add the resolvers

We need to tell the application how to handle the graphql requests. For queries and mutations.
Query Resolver:

```kotlin
// .../kotlin/com/grekz/crudKotlin/resolver/QueryResolver.kt
package com.grekz.crudKotlin.resolver

import com.coxautodev.graphql.tools.GraphQLQueryResolver
import com.grekz.crudKotlin.model.Task
import com.grekz.crudKotlin.service.TaskService
import org.springframework.stereotype.Component

@Component
class QueryResolver (private val taskService: TaskService) : GraphQLQueryResolver {
  fun getTasks(): List<Task> = taskService.getTasks()
  fun getTaskById(taskId: Long): Task = taskService.getTaskById(taskId).orElse(null)
}
```

Mutation Resolver:

```kotlin
// ../kotlin/com/grekz/crudKotlin/resolver/MutationResolver.kt
package com.grekz.crudKotlin.resolver

import com.coxautodev.graphql.tools.GraphQLMutationResolver
import com.grekz.crudKotlin.model.Task
import com.grekz.crudKotlin.service.TaskService
import org.springframework.stereotype.Component

@Component
class MutationResolver (private val taskService: TaskService) : GraphQLMutationResolver {
  fun createTask(title: String, description: String, status: Int, priority: Int): Task =
    taskService.addTask(
      Task(
        title = title,
        description = description,
        status = status,
        priority = priority
      )
    )

  fun updateTask(taskId: Long, title: String, description: String, status: Int, priority: Int): Task =
    taskService.putTask(
      taskId,
      Task(
        id = taskId,
        title = title,
        description = description,
        status = status,
        priority = priority
      )
    ).orElse(null)

  fun deleteTask(taskId: Long): Boolean = taskService.deleteTask(taskId)
}
```

## Add your GraphQL Schema

File: `../resources/schema.graphqls`

```graphql
type Query {
  getTasks: [Task]
  getTaskById(taskId: ID!): Task
}

type Mutation {
  createTask(
    title: String
    description: String
    status: Int
    priority: Int
  ): Task
  updateTask(
    taskId: Long!
    title: String
    description: String
    status: Int
    priority: Int
  ): Task
  deleteTask(taskId: Long!): Boolean
}

type Task {
  id: Long
  title: String
  description: String
  status: Int
  priority: Int
}
```

## It's all good and dandy... but just take me to the code!

Alright, if you just want to run the project you can get it in this repo: https://github.com/Grekz/example-kotlin-crud-graphql

## How to test it?

CRUD tests:
Now you can test your changes on your API and go to the **Graph_i_QL** http://localhost:8080/graphiql

Create:

```graphql
mutation {
  createTask(
    title: "He is cool Update"
    description: "asdas"
    status: 1
    priority: 2
  ) {
    id
    title
    description
    status
  }
}
```

Read:
All tasks

```graphql
query {
  getTasks {
    id
    title
    description
    status
    priority
  }
}
```

Or task by ID

```graphql
query {
  getTaskById(taskId: 1) {
    id
    title
    description
    status
    priority
  }
}
```

Update:

```graphql
mutation {
  updateTask(
    taskId: 4
    title: "He is cool Update"
    description: "asdas"
    status: 1
    priority: 2
  ) {
    id
    title
    description
    status
  }
}
```

Delete:

```graphql
mutation {
  deleteTask(taskId: 4)
}
```

Cheers!
I hope this helps you get your CRUD graphQL API up and running.
Let me know if you have some feedback!
