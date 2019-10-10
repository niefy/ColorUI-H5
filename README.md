# ColorUI-H5
[ColorUI](https://github.com/weilanwl/ColorUI) H5可直接使用的版本，适合无需webpack编译的简单H5页面使用

# 使用
在H5页面head中引入
```html
<!-- 必选 -->
<link rel="stylesheet" href="https://raw.githubusercontent.com/niefy/ColorUI-H5/master/css/ColorUi-H5.css">

<!-- 动画样式，可选 -->
<link rel="stylesheet" href="https://raw.githubusercontent.com/niefy/ColorUI-H5/master/css/animation.css">
<!-- 图标，可选 -->
<link rel="stylesheet" href="https://raw.githubusercontent.com/niefy/ColorUI-H5/master/css/icon.css">
```
# 部分示例
- 90%用法与[官网示例](http://demo.color-ui.com/h5.html#/)无差别
- [颜色](http://demo.color-ui.com/h5.html#/pages/basics/background)
```html
<div class="bg-red">红色背景</div>
<div class="bg-gradual-blue">靛青渐变背景</div>
<div class="text-brown">棕色文字</div>
```
- [布局](http://demo.color-ui.com/h5.html#/pages/basics/layout)
```html
<div class="fl">左浮动</div>
<div class="fr">右浮动</div>
<div class="marin">外边距</div>
<div class="marin-lr">水平方向边距</div>
<div class="marin-tb-lg">垂直方向边距（大）</div>
<div class="padding-sm">内边距(小)</div>
<div class="flex justify-start align-center">
    <div class="flex-sub">flex1</div>
    <div class="flex-sub">flex2</div>
</div>
```
- [标签](http://demo.color-ui.com/h5.html#/pages/basics/tag)
```html
<div class="cu-tag bg-green">森绿色标签</div>
<div class="cu-tag line-yellow">明黄色镂空标签</div>
```
- [进度条](http://demo.color-ui.com/h5.html#/pages/basics/progress)
```html
<div class="cu-progress">
    <div class="bg-red" style="width: 61.8%;">红色进度条</div>
</div>
<div class="cu-progress round sm striped">
    <div class="bg-green" style="width: 61.8%;">条纹进度条</div>
</div>
```

# 更改内容
- 长度单位全部更改为px
- 移除不使用于H5的组件：switch、swiper
- image标签更名为img
- view/scroll-view标签更名为div
- navigator标签更名为a
- radio标签更改为input[type="radio"]
- checkbox标签更改为input[type="checkbox"]


