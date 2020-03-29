package com.grekz.demo

fun main(args: Array<String>) {

    val me = Person("Juan", "Mendoza")
    val you = Person("Ruth", "Prado", "Jackelyne")
    
    val location = object {
        var xPos = 100
        var yPos = 200
    }

    println("Location: ${location.xPos} + ${location.yPos}")

    println("------")
    // val test = 123_321_123
    val aInt: Int = 1
    val aLong: Long = aInt.toLong()
    println(aLong)
    val lowest = 8
    when(lowest){
        0 -> println("some value $lowest")
        else -> println("else value")
    }

    when {
        lowest >= 8 -> println("lol integer")
        else -> println("More value")
    }
    for( (i, item) in 10.rangeTo(20).step(2).withIndex() ){
        print("${i+1}) $item, ")
    }
    println()
    val arr = arrayOf(10,20,30,40,50)
    for(item in arr.indices) {
        print("ind= $item, value: ${arr[item]}")
    }
    println()
    println("10 + 20 = ${testFn(10, 20)}")

}
fun testFn(a: Int, b: Int) = a + b

class Person internal constructor (firstName: String, lastName: String){
    init{
        println("Create a person named: $firstName, $lastName")
    }
    constructor(firstName: String, lastName: String, middleName: String):
        this(firstName, lastName) {

        }
}