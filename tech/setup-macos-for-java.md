# Setup your MacOS for Java Development with multiple Java Versions.

## Disclaimer
This is my personal preference on how to setup my local environment for Java development.
Feel free to leave your suggestions if you think there is a better setup.

## Getting a new Terminal
I've used iTerm2 for some years now, and I've found it pretty useful.
You can download it [here in its own SITE.](https://iterm2.com/downloads.html)
After you have downloaded the zip file, you just installed, for more info you can check their [FAQs.](https://iterm2.com/faq.html)

## Grabbing your Favorite Package Manager
If you have been using MacOS for a while, by now you should be familiar with [Hombebrew](https://brew.sh/).
To install it you can just run this command:
```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Or if you prefer, you can go to their [page](https://brew.sh/) and check the steps there.

### Homebrew already installed?
In case you have installed homebrew some time before.
Remember to update your formulas with the next command:
```bash
$ brew update
```

## Improving your shell experience
I've used ZSH and Oh My Zsh for some time. And you can install them by running this two commands.
```bash
$ brew install zsh
$ sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
If you want to know more about, check out [the Oh My Zsh site.](https://ohmyz.sh/)

## Managing your Java environment
When you are developing with multiple services, it is fairly common that you find yourself in the situation on having multiple java versions in your local machine. The tool that I have used in the past is [jEnv.](https://www.jenv.be/)
To install this great tool in your local machine, you just need to run the following command:
```bash
$ brew install jenv
```

After you have installed jenv you need to make sure that this is available every time you start your computer, to do this you will need to update your `~/.zshrc` with this next commands:
```bash
$ echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.zshrc
$ echo 'eval "$(jenv init -)"' >> ~/.zshrc
```

## Knowing & installing the Java versions you want
To know which versions of java you have available in homebrew you can run this:
```bash
$ brew search java
```
At this point in time we have available 3 java versions: `java, java11 and java6`. The first java formula is the latest.
To install these three java versions, you can run these commands:
```bash
$ brew cask install java
$ brew cask install java11
$ brew cask install java6
```
After installing this, you need to add them to the available jenv versions.
```bash
## First create the versions folder.
$ mkdir ~/.jenv/versions
## Add the versions to jenv
$ jenv add /Library/Java/JavaVirtualMachines/openjdk-13.0.2.jdk/Contents/Home
$ jenv add /Library/Java/JavaVirtualMachines/openjdk-11.0.2.jdk/Contents/Home
$ jenv add /Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
```

### Extra commands
To make easier to change the java version I use some aliases, by running these next commands you run:
```bash
$ echo 'alias refreshZsh="source ~/.zshrc"' >> ~/.zshrc
$ echo 'alias goJava13="jenv global 13.0 && refreshZsh"' >> ~/.zshrc
$ echo 'alias goJava11="jenv global 11.0 && refreshZsh"' >> ~/.zshrc
$ echo 'alias goJava6="jenv global 1.6 && refreshZsh"' >> ~/.zshrc
```
After this you can run:
```bash
$ source ~/.zshrc
```

## Installing Gradle
You can check the official documentation from Gradle on [how to install it with a package manager here.](https://gradle.org/install/#with-a-package-manager)
Or simply running this command:
```bash
$ brew install gradle
```

## Test your environment
We can test this configuration by cloning this repo from SpringBoot:
```bash
$ git clone https://github.com/spring-guides/gs-rest-service.git
$ cd gs-rest-service/complete
$ gradle bootRun
```
By now, you should see the spring ascii art in the console, and you should have accessible: `http://localhost:8080/greeting`

## Success!
Now you should be able to configure multiple java versions in your local computer.