# How to create your own 'Hello World' REST Service with Spring Boot, Gradle & Kotlin ?

### Some questions you might have:

#### What is Spring Boot?
Spring Boot is one of the most popular Java based frameworks. It is open source. It is developed by Pivotal Team. And it is pretty damn popular in the micro services world. [See it for yourself.](https://spring.io/projects/spring-boot)

#### What is Kotlin?
Kotlin is an Open Source statically typed programming language that targets the JVM, Android, JavaScript and Native. [See the reference.](https://kotlinlang.org)

#### What is a REST Service?
REST stands for Representational State Transfer. And you can find more info about it [here.](https://en.wikipedia.org/wiki/Representational_state_transfer)

### What is Gradle?
Gradle is an Open Source build automation tool. Similar to Maven, but cooler. [See the gradle homepage](https://gradle.org/)

### Ok, now we can jump into the good stuff...

### Get the bootstrap application from Spring Initializr
The guys making Spring Boot are pretty cool, and created a page where you can go and get your new spring boot application already condigured and with the dependencies you want. 
For this example we are going to use just two:
- __Spring Web__
    - Uses Apache Tomcat.
    - Used for building RESTful services.
- __Spring Boot DevTools__
    - Allows you to do live reloading and fast application restars.

1. You need to go to the [Spring Initializr page](https://start.spring.io/) 
1. Select _Project:_ __Gradle Project__
1. Select _Language:_ __Kotlin__
1. Leave the _Spring Boot_ and _Project Metadata_ as is.
1. When you arrive to the _Dependencies_ section search for __'Spring Web'__ and __'Spring Boot DevTools'__
1. Click __Generate__(the green button)

After you generate your spring boot application and unzip it.
Your project should look something like this: ![Example configuration][springboot_helloworld_project_structure]

### Create a new package.
You can name the new package: ``` com.example.demo.api ```

### Create a new Kotlin Class
Inside this new package, you need to create a new Kotlin class. Which we are going to name: ``` HelloWorldController ```

Example: ![Create Kotlin Class][springboot_helloworld_create_class]

### Map your class to the requests
We need to add two annotations, one to let the framework know that this class is a REST controller and the another one to tell Spring where to send the request with a particular path. Example: 
```java    
    @RestController 
    @RequestMapping("api/v1/hello")
```

### Create a new function
Now that the request mapping has been added to the class, we need to tell spring boot where are we going to handle the 'world' part of our hello world example.
For that we need to create a new function 
```kotlin 
    fun getHelloWorld(): String {
        return "Hello world!!!"
    } 
```

### Map the newly created function
Now that we have created a function that will handle the request we need to map it!
To do that, we need to add a new annotation to the method:
```kotlin
    @GetMapping("/world")
```

### Run the application!
Now that we have everything ready, you can run the application!!!
In order to do this, we have many options. Two of them are:
1. In the command line run: ```$ gradle bootRun ```
1. Or in your IDE hit the 'run' button. 

### See your Service
To check your new shinny Kotlin RESTful 'Hello World' Service, you can go to [http://localhost:8080/api/v1/hello/world](http://localhost:8080/api/v1/hello/world)

### Your Controller should look like this:
```kotlin
package com.example.demo.api

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RequestMapping("api/v1/hello")
@RestController
class HelloWorldController {

    @GetMapping("/world")
    fun getHelloWorld(): String {
        return "Hello world!!!"
    }

}
```
The rest of the folder structure and files, should remain as they were when you downloaded the bootstrap project.

#### Stay tuned for more
Some upcoming articles will be: Dockerize it, using JPA, configure Swagger, failure tolerance, service discovery.

## The END



<!-- Asset definitions -->
[springboot_helloworld_initializr]: ../assets/img/springboot_helloworld_initializr.png "Initializr Configuration Page"
[springboot_helloworld_project_structure]: ../assets/img/springboot_helloworld_project_structure.png "Project Folder Structure"
[springboot_helloworld_create_class]: ../assets/img/springboot_helloworld_create_class.png "Create Kotlin Class"