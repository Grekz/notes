"use strict";

function _extends() {
  _extends =
    Object.assign ||
    function (target) {
      for (var i = 1; i < arguments.length; i++) {
        var source = arguments[i];
        for (var key in source) {
          if (Object.prototype.hasOwnProperty.call(source, key)) {
            target[key] = source[key];
          }
        }
      }
      return target;
    };
  return _extends.apply(this, arguments);
}

function _objectWithoutProperties(source, excluded) {
  if (source == null) return {};
  var target = _objectWithoutPropertiesLoose(source, excluded);
  var key, i;
  if (Object.getOwnPropertySymbols) {
    var sourceSymbolKeys = Object.getOwnPropertySymbols(source);
    for (i = 0; i < sourceSymbolKeys.length; i++) {
      key = sourceSymbolKeys[i];
      if (excluded.indexOf(key) >= 0) continue;
      if (!Object.prototype.propertyIsEnumerable.call(source, key)) continue;
      target[key] = source[key];
    }
  }
  return target;
}

function _objectWithoutPropertiesLoose(source, excluded) {
  if (source == null) return {};
  var target = {};
  var sourceKeys = Object.keys(source);
  var key, i;
  for (i = 0; i < sourceKeys.length; i++) {
    key = sourceKeys[i];
    if (excluded.indexOf(key) >= 0) continue;
    target[key] = source[key];
  }
  return target;
}

var valuesMap = {
  SomeString: {
    whichString: "aString",
    whichNumber: 123,
  },
  OtherString: {
    whichString: "bString",
    whichNumber: 321,
  },
};
var extraThing = "Hey! I am a string";

var OtherComponent = function OtherComponent(props) {
  return React.createElement("div", props);
};

var MyComponent = function MyComponent(_ref) {
  var _ref$oneList = _ref.oneList,
    oneList = _ref$oneList === void 0 ? [] : _ref$oneList,
    aType = _ref.aType,
    props = _objectWithoutProperties(_ref, ["oneList", "aType"]);

  return React.createElement(
    "ul",
    null,
    oneList.map(function (item) {
      return React.createElement(
        OtherComponent,
        _extends(
          {
            alt: item,
            key: item,
            extraThing: extraThing,
          },
          valuesMap[aType],
          props
        )
      );
    })
  );
};

var MyApp = function MyApp(props) {
  return React.createElement(
    MyComponent,
    _extends(
      {
        id: 123,
        aType: "SomeString",
      },
      props,
      {
        containerOfThings: true,
        oneList: ["alt1", "alt2", "alt3"],
      }
    ),
    "some content"
  );
};

var domContainer = document.querySelector("#root");
ReactDOM.render(MyApp(), domContainer);
