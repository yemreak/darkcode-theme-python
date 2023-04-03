# 💖 Contributing

🙋‍♂️ Hello, this guide will help you to understand my theme and my color systems

## 🚀 Generating More Themes

- 👪 You can create your own DarkCode theme family
- 💁‍♂️ You can use `YThemeCretor` to generate more [DarkCode Themes](https://marketplace.visualstudio.com/items?itemName=yedhrab.darkcode-theme-adopted-python-and-markdown)
- 📦 `YThemeCreator` is part of [`ypackage`](https://github.com/yedhrab/YPackage) python package
- ⏬ Downlaod [`ypackage`](https://github.com/yedhrab/YPackage) with `pip install ypackage`
- 🐣 After installation, just use `ythemecreator -h` command to more usage options
- ⭐ For ex: `ythemecreator ./core/dark-settings.json` to create darkcode themes
- ⭐ For ex: `ythemecreator ./core/light-settings.json` to create light themes

> 💁‍♂️ Light themes are generated with `invert.js` (from dark themes and ythemecreator)

## 📦 Packaging Extension

- Install Nodejs
- Install vsce with `npm install -g vsce` command
- Generate extension (`.vsix`) with `vsce package` command
- If u want to publish, use `vsce publish` command without packaging

## 👨‍💻 Color System

- ⚖️ Every DarkCode color hex value has equivalent value in DarkCode Contrast 
- 🧮 This formula is given in [📜 ./core/dark-settings.json](./core/dark-settings.json) file

## ✨ Plus Themes

- ➕ Plus themes has a few additional improvements that are given the below

> ⭐ Long story short, more yellow color features

### ➕ One Plus

- ✨ All `⭐ Normal` features and additional settings that are given the below

```json
{
    "editorSuggestWidget.border": "#413701",
    "editorSuggestWidget.foreground": "#bb8b12",
    "editorSuggestWidget.highlightForeground": "#ffbf40b4",
    "editorSuggestWidget.selectedBackground": "#41370177",
    "tab.activeBorderTop": "#FFC000",
    "tab.hoverBackground": "#FFC00010",
    "tab.hoverBorder": "#ffd90070",
}
```

### ➕➕ Two Plus

- ✨ All `➕ One Plus` features and additional settings that are given the below

```json
{
    "editorHoverWidget.foreground": "#bb8b12",
    "menu.foreground": "#bb8b12",
    "titleBar.activeForeground": "#bb8b12"
}
```
