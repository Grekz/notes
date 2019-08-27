# Atomic design

## What is atomic design methodology?
This is a methodology that allows you to have a better way to organize your components. You can use atomic design methodology to have a better organization on your Design System or Component Pattern Library.

## What is it all about?
The atomic design methodology consist of splitting the design into five different stages or types:
1. Atoms
2. Molecules
3. Organisms
4. Templates
5. Pages 

Having this categorization helps you organize in a better way how you compose your User Interfaces.

### Atoms
The category of atoms is the most basic of them all. Those that fall under this category are the building blocks of the rest of the components, the fundation.
One quick way of identify if an element is in this category is: if the component contains one to three html tag. The rules to categorize components is up to you to define it.

### Molecules
This type of components are the next in term of complexity. You could thing of this components as something more elaborated than just a simple html element. An example would be: a whole input with button and label with some behaviour.

### Organisms
The organisms category is a somewhat complex UI component composed of severals molecules and/ or atoms.
An example of this would be a galery full of products with pricing (Molecules). Another example could be a header of a page with links, search input and page logo.

### Templates
All components that are on this category should have the skeleton of the page. How your page will look, with dummy data. Placeholder images, 'lorem ipsum' everywhere and mock information all over the place to see how the placement and distribution will look like.

### Pages
We have made it to the final part. The good old pages are the last level in our quest. Components here will have the information that is going to be presented to the final user.


## Why use it?
I know you are looking for a great way to organize your next component pattern library or your future design system. I can tell you based on our current experience, that having this way of organizing our component pattern library has been working great for us and we plan to continue following this methodology.
 
### Reference
You can hear it from the good Brad Frost himself in this next link: http://atomicdesign.bradfrost.com/chapter-2/