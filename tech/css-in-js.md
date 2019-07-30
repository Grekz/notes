# Why in hell should I use CSS-in-JS <sub><sup>_with EmotionJS_</sup></sub> ?

## Table of Content
1. [What is the problem with CSS?](WhatistheproblemwithusingonlynormalCSS?)
2. [What is CSS-in-JS?](WhatisCSS-in-JS?)
3. [What libraries can you use?](Whatlibrariescanyouuse?)
4. [How can you start using this wonderful thing called CSS-in-JS?](HowcanyoustartusingthiswonderfulthingcalledCSS-in-JS?)

## What is the problem with using only normal CSS?

Bottomline: Using normal css in a javascript application is hard to maintain. 

__Some of the problems you will encounter are:__
- Having global css rules that can affect your components without intention.
- More often than not, you will have two files open at all times; one for css and one for your javascript component.
- As time progresses you or your team will began to add more and more rules to the css files and making a change in certain class or rule can affect your component in an undesired way.
- In addition to the previous point, when you have the need to update a css rule, you sometimes are not 100% sure that you will not affect other components.
- To include css in your components you will need to add extra configuration to load the css files.

## What is CSS-in-JS?

__Css-in-JS__ is simple put: to have your CSS that style your component inside your Javascript code. It allows you to easily encapsulate all the CSS related to a particular component inside that same Javascript component.

## What libraries can you use?

There are several libraries that will help you in your css-in-js journey. You have the OG called [Styled-components.](https://github.com/styled-components/styled-components). Some other options are: [JSS](https://github.com/cssinjs/jss) & [Radium](https://github.com/FormidableLabs/radium). My favorite and the more loveable of them all is [EmotionJS.](https://github.com/emotion-js/emotion)

## How can you start using this wonderful thing called CSS-in-JS?

The guys from EmotionJS already made a great job explaining how you can use this beauty in here their [documentation.](https://emotion.sh/docs/introduction)

__What?... So you want me to explain it?... OK, then...__

Do me a favor and jump into this [codesandbox link.](https://codesandbox.io/s/new) You there yet? Cool.

Now you should be seeing something like this:
![Initial Sandbox][cssinjs_emotion_initial]

Remove the line with the css import (🤮)

```javascript
import "./styles.css";
```
After removing that thingo, click in the blue button with the text: `Add Dependency`.

A modal will appear, here you should type: `@emotion/core` and click in this package. ![Package @emotion/core][cssinjs_emotion_core] 

After that package was added to your sandbox let's type: `@emotion/styled` and click in this package. ![Package @emotion/styled][cssinjs_emotion_styled] 

Excellent padawan, you are doing great.
Walk with me, and after the react-dom import, add on the top of the file this line:

```javascript
import styled from '@emotion/styled';
```

Now... the moment of truth has arrived. You are going to create your first CSS-in-JS component! 🎉

```javascript
// Add this to your code sandbox
const WrapperApp = styled.div`
    color:red;
    background: aqua;
`;
```

Well done! 👏👏👏

There it is, your first component.
Now let's see what that was.
You have created a styled component called `WrapperApp` that is a `div` and we use the `styled` object from EmotionJS to do it.
We have inside that component the css rules `color:red` and `background:aqua` 

To include this new styled component in your code, you can just replace the old `<div>` that wrapped your App.

After replacing it, your `function App()` should look like this:
```javascript
function App() {
  return (
    <WrapperApp>
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
    </WrapperApp>
  );
}
```

Here is how your react application example should look like:
![Final state][cssinjs_emotion_final]

Alright my friends, give yourselves one pat on the back because you have done it!
![Pat on the back][cssinjs_emotion_patback]

Here is the codesandbox I have used for [this example.](https://codesandbox.io/s/friendly-microservice-78hfd)


In case you want to contact me here are some places:

- [LinkedIn](https://www.linkedin.com/in/grekz/)
- [Github](https://github.com/grekz)
- [Stackoverflow](https://stackoverflow.com/users/551773/grekz)
- [Blog](https://grekz.wordpress.com/)

## The end.

Now my children, go and play with your new knowledge. Go!

<!-- Asset definitions -->
[cssinjs_emotion_initial]: ../assets/img/cssinjs_emotion_initial.png "Initial Sandbox with React"
[cssinjs_emotion_core]: ../assets/img/cssinjs_emotion_core.png "Add Dependency @emotion/core"
[cssinjs_emotion_styled]: ../assets/img/cssinjs_emotion_styled.png "Add Dependency @emotion/styled"
[cssinjs_emotion_final]: ../assets/img/cssinjs_emotion_final.png "Final react app with CSS-in-JS example"
[cssinjs_emotion_patback]: ../assets/img/cssinjs_emotion_patback.png "Pat on the back"
