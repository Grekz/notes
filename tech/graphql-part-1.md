# GraphQL + Kotlin & Spring Boot - Part 1

## Summary

Welcome back to your humble dev.to blog! In this post I will try to give you the tools to set up a simple graphql with spring boot project. As a small disclaimer the folder structure and design patterns are not to be followed in a real application.

## Prerequisites

You need to set up your local environment.
To do this we have already created a [step by step guide in here.](https://dev.to/grekz/setup-your-macos-for-java-development-with-multiple-java-versions-5djj)
You can check that you have installed Kotlin and JDK by typing this in your terminal:

```bash
$ kotlin -version
## output: Kotlin version 1.3.61-release-180 (JRE 13.0.2+8)
$ javac -version
## output: javac 13.0.2
$ gradle -version
```

## Spring Boot Initializr

You can go to [Spring Boot Initializr page](https://start.spring.io/) and select the next.

- Project: Gradle Project
- Language: Kotlin
- Spring Boot: 2.2.5
- Group: com.grekz
- Artifact: graphqlDemo
- Dependencies: Spring Web, Spring Boot DevTools

And click in the **Generate** button.

## Add dependencies

We need to add some dependencies necessary to have our GraphQL up and running.

```kotlin
// file build.gradle.kts
dependencies {
	implementation ("com.graphql-java:graphql-spring-boot-starter:5.0.2")
	implementation ("com.graphql-java:graphiql-spring-boot-starter:5.0.2")
	implementation ("com.graphql-java:voyager-spring-boot-starter:5.0.2")
	implementation ("com.graphql-java:graphql-java-tools:5.2.4")
    // ... rest of dependencies
}
```

Here we just added graphql, [GraphQL (A graphical interactive in-browser GraphQL IDE)](https://github.com/graphql/graphiql#graphiql), [Voyager (Represents your GraphQL API as an interactive graph)](https://github.com/APIs-guru/graphql-voyager) and utilities classes to help you with your GraphQL integrations.

## Update application configuration

After updating the dependencies, we need to have a file that contains the configurations to tell our application how to behave.
You need to create a file named `application.yml` in your folder `./src/main/resources`

```yml
# file application.yml
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

## Create a data class

Now we are going to create a data class named Book, that will contain two attributes.

```kotlin
package com.grekz.graphqlDemo

data class Book( val id: String, val name: String )
// file: ./src/main/kotlin/com/grekz/graphqlDemo/Book.kt
```

## Create a GraphQL query resolver

```kotlin
package com.grekz.graphqlDemo

import org.springframework.stereotype.Component
import com.coxautodev.graphql.tools.GraphQLQueryResolver

@Component
class BookResolver() : GraphQLQueryResolver {
    // this method name needs to be same and in the schema
    fun books(): List<Book> {
        val book1 = Book("1", "name1")
        val book2 = Book("2", "name2")
        return listOf(book1, book2)
    }
}
// file: ./src/main/kotlin/com/grekz/graphqlDemo/BookResolver.kt
```

## Defining your schema

In GraphQL you need to specify the types and how data can be queried or mutated.
You can put the next in the file: `./src/main/resources/models.graphqls`

```graphql
type Query {
  books: [Book]
}

type Book {
  id: String!
  name: String!
}
```

## Run the project!

This is all you need to have your graphql application running.
To do this you need to type the command:

```bash
$ gradle bootRun
```

After starting your server you can go to:
http://localhost:8080/graphiql?query=query%7B%0A%20%20books%7B%0A%20%20%20%20id%0A%20%20%7D%0A%7D

And hit the play button on the top to see the results.
Another cool thing you just did is to install Voyager. To see it running you can check: http://localhost:8080/voyager

Now that you have graphql up and running the sky is the limit!

## Follow up

If you want another example on another thing you can do with GraphQL you can check [this Auth0 post.](https://auth0.com/blog/building-graphql-apis-with-kotlin-spring-boot-and-mongodb/)
