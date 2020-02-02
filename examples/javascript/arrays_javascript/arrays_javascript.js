const myTacos = [ 
  { name: "Cheese", price: 4, spicy: true },
  { name: "Pastor", price: 5, spicy: true }, 
  { name: "Beef", price: 7, spicy: false },
  { name: "Fish", price: 9, spicy: false } 
]

// forEach
// 1. Print all taco objects.
// myTacos.forEach(taco => console.log(taco))

// 2. Print all taco names.
// myTacos.forEach(taco => console.log(`Taco name: ${taco.name}`))

// filter
// 1. Get all tacos cheaper than 6.
const cheapTacos = myTacos.filter(taco => taco.price < 6)

// 2. Get all tacos that are spicy.
const spicyTacos = myTacos.filter(taco => taco.spicy)

// map
// 1. Adjust inflation to all the tacos prices.
const adjustedTacos = myTacos.map(taco => ({...taco, price: taco.price + 4}))

// 2. Translate all taco names to spanish-o.
const spanishoTacos = myTacos.map(taco => ({...taco, name: taco.name + 'o'}))

// 3. Map from taco objects to name strings
const tacoNames = myTacos.map(({name}) => name)

// reduce
// 1. Get the sum of all the amounts.
const amounts = [12, 9, 4, 0, 11]
const sumAmmounts = amounts.reduce((sum, current) => sum + current, 0)

// 2. Get the sum of prices if you eat 1 taco of each.
const tacoPricesSum = myTacos.reduce((sum, taco) => sum + taco.price, 0)
console.log(tacoPricesSum)