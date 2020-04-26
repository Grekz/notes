# Improve your React skills with these 5 tips

## Summary

We will go through a piece of Javascript code that we have all seen(or eventually will see) in some of our careers. And I will try to make some improvements and I will provide some arguments on why I make them. I hope you find this helpful!

## The scene of the crime

```jsx
function Othercomponent({ children, props }) {
  return <div {...props}>{children}</div>;
}
const MyComponent = ({
  id,
  text,
  style,
  extraProps,
  oneList,
  containerOfThings,
  aType,
}) => {
  const whichString = aType == "SomeString" ? "aString" : "bString";
  const whichNumber = aType == "SomeString" ? 123 : 321;
  const extraThing = "Hey! I am a string";
  if (containerOfThings && oneList && oneList.length > 1) {
    return (
      <ul>
        <OtherComponent
          whichString={whichString}
          whichNumber={whichNumber}
          id={id}
          style={style}
          extraProps={extraProps}
          alt={oneList[0]}
          extraThing={extraThing}
        >
          {text}
        </OtherComponent>
        <OtherComponent
          whichString={whichString}
          whichNumber={whichNumber}
          id={id}
          style={style}
          extraProps={extraProps}
          alt={oneList[1]}
          extraThing={extraThing}
        >
          {text}
        </OtherComponent>
        <OtherComponent
          whichString={whichString}
          whichNumber={whichNumber}
          id={id}
          style={style}
          extraProps={extraProps}
          alt={oneList[2]}
          extraThing={extraThing}
        >
          {text}
        </OtherComponent>
      </ul>
    );
  } else {
    return (
      <OtherComponent
        whichString={whichString}
        whichNumber={whichNumber}
        id={id}
        style={style}
        extraProps={extraProps}
        extraThing={extraThing}
        alt={text}
      >
        {text}
      </OtherComponent>
    );
  }
  return <></>;
};

const MyApp = (props) => (
  <MyComponent id={123} aType={"SomeString"} text="some content" {...props} />
);
```

Ok... bear with me now. I know it is ugly. Let us try to make it better one step at the time.

### #1 Stay consistent

In the first component(`<Othercomponent/>`) we are declaring our component in the way: `function XXXXX() { /* ... */ }` and not in a PascalCase. While in the second component(`<MyComponent/>`) we are using arrow functions and PascalCase. It is important to stay consistent across your codebase so when you start to create another component you don't have to question yourself or your teammates on what is the right way to define my components. If you have a consistent codebase it allows your fellow developers to make better assumptions on what's the current state and rules followed, liberating from questioning every single step of the way while implementing code around an existing piece of code.

Result:

```jsx
const OtherComponent = (props) => <div {...props} />;

const MyComponent = ({
  id,
  children,
  style,
  extraProps,
  oneList,
  containerOfThings,
  aType,
}) => {
  const whichString = aType == "SomeString" ? "aString" : "bString";
  const whichNumber = aType == "SomeString" ? 123 : 321;
  const extraThing = "Hey! I am a string";
  if (containerOfThings && oneList && oneList.length > 1) {
    return (
      <ul>
        <OtherComponent
          whichString={whichString}
          whichNumber={whichNumber}
          id={id}
          style={style}
          extraProps={extraProps}
          alt={oneList[0]}
          extraThing={extraThing}
        >
          {children}
        </OtherComponent>
        <OtherComponent
          whichString={whichString}
          whichNumber={whichNumber}
          id={id}
          style={style}
          extraProps={extraProps}
          alt={oneList[1]}
          extraThing={extraThing}
        >
          {children}
        </OtherComponent>
        <OtherComponent
          whichString={whichString}
          whichNumber={whichNumber}
          id={id}
          style={style}
          extraProps={extraProps}
          alt={oneList[2]}
          extraThing={extraThing}
        >
          {children}
        </OtherComponent>
      </ul>
    );
  } else {
    return (
      <OtherComponent
        whichString={whichString}
        whichNumber={whichNumber}
        id={id}
        style={style}
        extraProps={extraProps}
        extraThing={extraThing}
        alt={children}
      >
        {children}
      </OtherComponent>
    );
  }
  return <></>;
};

const MyApp = (props) => (
  <MyComponent id={123} aType={"SomeString"} {...props}>
    some content
  </MyComponent>
);
```

### #2 Leverage the language/framework features

One incredibly common thing I've seen recently when doing code reviews for Frontend Engineers is that we are no longer familiar with the features that the framework or the syntactic sugar the language offers.

#### Children as props

We know that everything you write inside a React component is a children and children are passed as props(you can send them inside or with the `children={'my child'}` prop). So we can always leverage this when we are implementing our components.

#### No return statement

We can make use of the JS feature of the one-liner functions, that don't need any `return` keyword. Please use the features that the good people working on them! https://github.com/tc39/proposals

```jsx
const OtherComponent = (props) => <div {...props} />;

const MyComponent = ({
  id,
  children,
  style,
  extraProps,
  oneList,
  containerOfThings,
  aType,
}) => {
  const whichString = aType == "SomeString" ? "aString" : "bString";
  const whichNumber = aType == "SomeString" ? 123 : 321;
  const extraThing = "Hey! I am a string";
  if (containerOfThings && oneList && oneList.length > 1) {
    return (
      <ul>
        <OtherComponent
          whichString={whichString}
          whichNumber={whichNumber}
          id={id}
          style={style}
          extraProps={extraProps}
          alt={oneList[0]}
          extraThing={extraThing}
        >
          {children}
        </OtherComponent>
        <OtherComponent
          whichString={whichString}
          whichNumber={whichNumber}
          id={id}
          style={style}
          extraProps={extraProps}
          alt={oneList[1]}
          extraThing={extraThing}
        >
          {children}
        </OtherComponent>
        <OtherComponent
          whichString={whichString}
          whichNumber={whichNumber}
          id={id}
          style={style}
          extraProps={extraProps}
          alt={oneList[2]}
          extraThing={extraThing}
        >
          {children}
        </OtherComponent>
      </ul>
    );
  } else {
    return (
      <OtherComponent
        whichString={whichString}
        whichNumber={whichNumber}
        id={id}
        style={style}
        extraProps={extraProps}
        extraThing={extraThing}
        alt={children}
      >
        {children}
      </OtherComponent>
    );
  }
  return <></>;
};

const MyApp = (props) => (
  <MyComponent id={123} aType={"SomeString"} {...props}>
    some content
  </MyComponent>
);
```

### #3 Being explicit without reason

Some people like to argue that we should always be explicit. That every single component should have all the props deconstructed. I understand that this approach is desirable in some scenarios, but in most cases is just noise to the code. If you have this need, please consider moving to Typescript(or if you just want to make better JS code in general). In our example we can make a lot of things implicit because we are deconstructing some variables that we never touch and we don't care.

```jsx
const OtherComponent = (props) => <div {...props} />;

const MyComponent = ({ oneList, containerOfThings, aType, ...props }) => {
  const whichString = aType == "SomeString" ? "aString" : "bString";
  const whichNumber = aType == "SomeString" ? 123 : 321;
  const extraThing = "Hey! I am a string";
  if (containerOfThings && oneList && oneList.length > 1) {
    return (
      <ul>
        <OtherComponent
          whichString={whichString}
          whichNumber={whichNumber}
          alt={oneList[0]}
          extraThing={extraThing}
          {...props}
        />
        <OtherComponent
          whichString={whichString}
          whichNumber={whichNumber}
          alt={oneList[1]}
          extraThing={extraThing}
          {...props}
        />
        <OtherComponent
          whichString={whichString}
          whichNumber={whichNumber}
          alt={oneList[2]}
          extraThing={extraThing}
          {...props}
        />
      </ul>
    );
  } else {
    return (
      <OtherComponent
        whichString={whichString}
        whichNumber={whichNumber}
        alt={oneList[0]}
        extraThing={extraThing}
        {...props}
      />
    );
  }
  return <></>;
};

const MyApp = (props) => (
  <MyComponent
    id={123}
    aType={"SomeString"}
    {...props}
    containerOfThings={true}
    oneList={["alt1", "alt2", "alt3"]}
  >
    some content
  </MyComponent>
);
```

### #4 Reduce Logical branches / Make your code less error prone

We all love ternaries and unnecessary variables, I get it. I've fallen into this trap, where you want to make something work and then you decide that checking with an `if` or assigning a value with a ternary is the solution. Most of the time is not. It just increase the time you will spend on reaching full/good test coverage of your code.

When we add those logical branches once in a while we make dumb mistakes such a code that is unreachable or we make our code more complex than it should.

#### Remove the ternary if

One nifty trick that you should use to reduce logical branches from ternary ifs is the usage of maps(you can also call them hashes/objects). You can think of them as some configuration helpers. 😇

```jsx
const OtherComponent = (props) => <div {...props} />;

const MyComponent = ({ oneList, containerOfThings, aType, ...props }) => {
  const valuesMap = {
    SomeString: { str: "aString", num: 123 },
    OtherString: { str: "bString", num: 321 },
  };
  const extraThing = "Hey! I am a string";
  if (containerOfThings && oneList && oneList.length > 1) {
    return (
      <ul>
        <OtherComponent
          whichString={valuesMap[aType].str}
          whichNumber={valuesMap[aType].num}
          alt={oneList[0]}
          extraThing={extraThing}
          {...props}
        />
        <OtherComponent
          whichString={valuesMap[aType].str}
          whichNumber={valuesMap[aType].num}
          alt={oneList[1]}
          extraThing={extraThing}
          {...props}
        />
        <OtherComponent
          whichString={valuesMap[aType].str}
          whichNumber={valuesMap[aType].num}
          alt={oneList[2]}
          extraThing={extraThing}
          {...props}
        />
      </ul>
    );
  } else {
    return (
      <OtherComponent
        whichString={valuesMap[aType].str}
        whichNumber={valuesMap[aType].num}
        alt={oneList[0]}
        extraThing={extraThing}
        {...props}
      />
    );
  }
  return <></>;
};

const MyApp = (props) => (
  <MyComponent
    id={123}
    aType={"SomeString"}
    {...props}
    containerOfThings={true}
    oneList={["alt1", "alt2", "alt3"]}
  >
    some content
  </MyComponent>
);
```

#### Remove complexity, remove the conditionals

It has been some years now that the Functional Programming(FP) paradigm has been around and re-hyped. So the time has come for you to stop using `ifs` and improve the quality of your code.

In this example we can see that there is unnecessary return, and the example is pretty dumb or obvious but I guarantee you will read or have read some code with conditions that are useless.

Now if we can work around having the same html structure for all the scenarios, it will make your code ridiculously simple. You might need to improve your CSS skills if you don't see a clear way on doing this.

```jsx
const OtherComponent = (props) => <div {...props} />;

const MyComponent = ({ oneList = [], aType, ...props }) => {
  const valuesMap = {
    SomeString: { str: "aString", num: 123 },
    OtherString: { str: "bString", num: 321 },
  };
  const extraThing = "Hey! I am a string";
  return (
    <ul>
      {oneList.map((item) => (
        <OtherComponent
          whichString={valuesMap[aType].str}
          whichNumber={valuesMap[aType].num}
          alt={item}
          key={item}
          extraThing={extraThing}
          {...props}
        />
      ))}
    </ul>
  );
};

const MyApp = (props) => (
  <MyComponent
    id={123}
    aType={"SomeString"}
    {...props}
    containerOfThings={true}
    oneList={["alt1", "alt2", "alt3"]}
  >
    some content
  </MyComponent>
);
```

### #5 Constants in your React Apps

My last advice for this article is this: Check your Constants!

Always make sure to leave them outside your React Components, you don't need to redeclare them every time the component is called. Also use set default values for your props, you will save some time by letting everyone know which is the default behavior of your component.

```jsx
const STRING_TYPES = { SomeString: "SomeString", OtherString: "OtherString" };

const valuesMap = {
  SomeString: { whichString: "aString", whichNumber: 123 },
  OtherString: { whichString: "bString", whichNumber: 321 },
};

const extraThing = "Hey! I am a string";

const OtherComponent = (props) => <div {...props} />;

const MyComponent = ({
  aType = STRING_TYPES.SomeString,
  oneList = [],
  ...props
}) => (
  <ul>
    {oneList.map((item) => (
      <OtherComponent
        alt={item}
        key={item}
        extraThing={extraThing}
        {...valuesMap[aType]}
        {...props}
      />
    ))}
  </ul>
);

const MyApp = (props) => (
  <MyComponent
    id={123}
    aType={STRING_TYPES.SomeString}
    containerOfThings={true}
    oneList={["alt1", "alt2", "alt3"]}
    {...props}
  >
    some content
  </MyComponent>
);
```

## The end!

I hope this helps you guys!

Cheers, stay safe!
