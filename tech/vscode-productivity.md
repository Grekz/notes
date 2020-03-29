# Improve your productivity in VS Code

## Plugins

- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
  - It helps you understand a little more the piece of code you are seeing by providing you with some quick overview on who and when was updated the current line of code.
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
  - I use a lot this extension. I have never learnt how words are written =). And having this extension has helped me to avoid some typos on naming things. Although we know this is the hardest part of being a software engineer.
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
  - Another essential tool. To have all nice and tidy after you save your file. This tool will auto format your files.
- [Indent Rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)
  - Cool tool to see the current scope of some functions. Useful if you do not want to search with your eyes what's the scope of this function???
- [Turbo Console Log](https://marketplace.visualstudio.com/items?itemName=ChakrounAnas.turbo-console-log)
  - We never console.log our code I know. Just try this in case you need to save some time.
- [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
  - Great tool that allows you to start local dev server.

## Keyboard Shortcuts

| **Shortcut**                          | **Action**                                                                         |
| ------------------------------------- | ---------------------------------------------------------------------------------- |
| Cmd + B                               | Hide or Show side panel.                                                           |
| Cmd + D                               | Select next occurrence of current selection.                                       |
| Cmd + E                               | Highlights all occurrences of current selection.                                   |
| Cmd + F                               | Search in current file.                                                            |
| Cmd + P                               | Go to File...                                                                      |
| Cmd + M                               | Minimize VS Code editor.                                                           |
| Cmd + N                               | Create new file.                                                                   |
| Cmd + S                               | Save current changes.                                                              |
| Cmd + W                               | Close current tab.                                                                 |
| Cmd + 2                               | Open second split panel.                                                           |
| Cmd + Shift + L                       | Select all occurrences of current selection.                                       |
| Cmd + Shift + F                       | Search: Find in files.                                                             |
| Cmd + Shift + K                       | Delete current line.                                                               |
| Cmd + Shift + P                       | Open Command palette. Here you can check all the commands that you have available. |
| Cmd + F2                              | Change all occurrences of the current selection.                                   |
| Cmd + Option + arrows (up or down)    | Add cursor to next or previous line.                                               |
| Cmd + Option + arrows (left or right) | Move to next tab.                                                                  |
| Cmd + arrows (left or right)          | Go to the end or the beginning of the current line.                                |
| Option + arrows (left or right)       | Move to next line token (spaces or dots).                                          |
| Option + arrows (up or down)          | Move swap lines with the next in the arrow direction.                              |
| Option + Shift + arrows (up or down)  | Copy current line up or down.                                                      |
| Option + Shift + F                    | Format current document.                                                           |
| Esc                                   | Remove current selection or action.                                                |
| Cmd + K (release Cmd) + C             | Compare current changes with previous changes.                                     |
| Shift + `` ` ``(backtick)             | Open the terminal in your VS Code.                                                 |

## Custom settings.json

- Customize your workspace with a color header:

```json
  "workbench.colorCustomizations": {
    "titleBar.activeBackground": "#8bbff3",
    "titleBar.activeForeground": "#333333",
    "titleBar.inactiveForeground": "#EEEEEE"
  },
```

- Format on save:

```json
    "editor.formatOnSave": true,
```

## Extra Info

- [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables)
