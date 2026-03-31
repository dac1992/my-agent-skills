# 微信公众号排版样式指南

风格参考：「摸鱼小李」公众号（https://mp.weixin.qq.com/s/EMahAzgfAbRQrYukWE7_IQ）

---

## 一、全局容器

```html
<section style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', Arial, sans-serif; font-size: 16px; color: #3d3d3d; line-height: 1.8; padding: 0 16px; max-width: 677px; margin: 0 auto; word-break: break-word;">
  <!-- 文章内容 -->
</section>
```

---

## 二、标题组件

### H1 主标题
```html
<h1 style="font-size: 24px; font-weight: bold; color: #1a1a1a; text-align: center; margin: 32px 0 8px; line-height: 1.4;">
  文章主标题
</h1>
<div style="width: 48px; height: 4px; background: #07c160; border-radius: 2px; margin: 0 auto 32px;"></div>
```

### H2 章节标题（带绿色左边框）
```html
<h2 style="font-size: 18px; font-weight: bold; color: #1a1a1a; margin: 40px 0 16px; padding: 10px 16px; background: #f0faf4; border-left: 4px solid #07c160; border-radius: 0 6px 6px 0; line-height: 1.5;">
  章节标题
</h2>
```

### H3 小节标题（带序号圆点）
```html
<h3 style="font-size: 16px; font-weight: bold; color: #1a1a1a; margin: 28px 0 12px; display: flex; align-items: center; gap: 8px; line-height: 1.5;">
  <span style="display: inline-block; width: 24px; height: 24px; background: #07c160; color: #fff; font-size: 12px; font-weight: bold; border-radius: 50%; text-align: center; line-height: 24px; flex-shrink: 0;">1</span>
  小节标题
</h3>
```

### 带数字的章节分隔标题（01/02/03 风格）
```html
<div style="margin: 48px 0 24px; text-align: center;">
  <div style="display: inline-block; position: relative;">
    <span style="font-size: 48px; font-weight: 900; color: #e8f5ef; line-height: 1;">01</span>
    <h2 style="font-size: 18px; font-weight: bold; color: #1a1a1a; margin: 0; padding: 6px 16px; background: #07c160; color: #fff; border-radius: 4px; display: inline-block;">章节标题</h2>
  </div>
  <p style="font-size: 13px; color: #999; margin: 8px 0 0; font-style: italic;">副标题说明文字</p>
</div>
```

---

## 三、正文段落

```html
<p style="font-size: 16px; color: #3d3d3d; line-height: 1.8; margin: 0 0 20px;">
  正文段落内容
</p>
```

### 加粗强调文字（内联）
```html
<strong style="color: #1a1a1a; font-weight: bold;">加粗文字</strong>
```

### 绿色高亮强调（内联）
```html
<span style="color: #07c160; font-weight: bold;">重点强调内容</span>
```

### 行内代码
```html
<code style="font-family: 'Menlo', 'Monaco', 'Consolas', monospace; font-size: 14px; background: #f6f8fa; color: #e96900; padding: 2px 6px; border-radius: 4px; border: 1px solid #e1e4e8;">代码内容</code>
```

---

## 四、引用块

```html
<blockquote style="margin: 20px 0; padding: 12px 16px; background: #f7f7f7; border-left: 4px solid #07c160; border-radius: 0 6px 6px 0; color: #555; font-size: 15px; line-height: 1.8;">
  引用内容文字
</blockquote>
```

---

## 五、代码块

```html
<div style="margin: 20px 0; border-radius: 8px; overflow: hidden; border: 1px solid #e1e4e8;">
  <div style="background: #f0f0f0; padding: 8px 16px; font-size: 12px; color: #666; border-bottom: 1px solid #e1e4e8; font-family: monospace;">bash</div>
  <pre style="margin: 0; padding: 16px; background: #f6f8fa; overflow-x: auto; font-size: 14px; line-height: 1.6;"><code style="font-family: 'Menlo', 'Monaco', 'Consolas', monospace; color: #24292e;">命令内容</code></pre>
</div>
```

### 可复制命令框（带📋标题）
```html
<div style="margin: 20px 0; border-radius: 8px; overflow: hidden; border: 1px solid #d0e8d8;">
  <div style="background: #e8f5ef; padding: 8px 16px; font-size: 13px; color: #07c160; font-weight: bold; border-bottom: 1px solid #d0e8d8;">📋 复制发给助手</div>
  <pre style="margin: 0; padding: 16px; background: #f9fdfb; overflow-x: auto; font-size: 14px; line-height: 1.7;"><code style="font-family: 'Menlo', 'Monaco', 'Consolas', monospace; color: #24292e; white-space: pre-wrap;">命令或提示词内容</code></pre>
</div>
```

---

## 六、步骤列表（Step N 风格）

```html
<div style="margin: 24px 0;">
  <!-- 单个步骤 -->
  <div style="display: flex; gap: 16px; margin-bottom: 24px; align-items: flex-start;">
    <div style="flex-shrink: 0; width: 32px; height: 32px; background: #07c160; color: #fff; font-size: 14px; font-weight: bold; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-top: 2px;">1</div>
    <div style="flex: 1;">
      <p style="font-size: 16px; font-weight: bold; color: #1a1a1a; margin: 0 0 8px; line-height: 1.5;">步骤标题</p>
      <p style="font-size: 15px; color: #555; line-height: 1.8; margin: 0;">步骤说明内容</p>
    </div>
  </div>
</div>
```

---

## 七、卡片导航组（Part 01/02 风格）

```html
<div style="margin: 32px 0; display: flex; gap: 12px; flex-wrap: wrap;">
  <!-- 单张卡片 -->
  <div style="flex: 1; min-width: 120px; background: #fff; border: 1px solid #e8e8e8; border-radius: 10px; padding: 16px 12px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
    <div style="font-size: 28px; font-weight: 900; color: #e8f5ef; line-height: 1; margin-bottom: 4px;">01</div>
    <div style="font-size: 14px; font-weight: bold; color: #1a1a1a; margin-bottom: 6px;">标题</div>
    <div style="font-size: 12px; color: #999; line-height: 1.5;">副标题说明</div>
  </div>
</div>
```

---

## 八、提示框 / 小贴士

### 绿色提示框
```html
<div style="margin: 20px 0; padding: 14px 16px; background: #e8f5ef; border-radius: 8px; border: 1px solid #b7dfc8;">
  <p style="margin: 0; font-size: 15px; color: #2d7a4f; line-height: 1.7;">💡 <strong>提示：</strong>提示内容文字</p>
</div>
```

### 黄色警告框
```html
<div style="margin: 20px 0; padding: 14px 16px; background: #fffbe6; border-radius: 8px; border: 1px solid #ffe58f;">
  <p style="margin: 0; font-size: 15px; color: #7c5e00; line-height: 1.7;">⚠️ <strong>注意：</strong>注意内容文字</p>
</div>
```

---

## 九、分割线

```html
<div style="margin: 32px 0; height: 1px; background: #ebebeb;"></div>
```

### 装饰性分割（带文字）
```html
<div style="margin: 40px 0; display: flex; align-items: center; gap: 12px;">
  <div style="flex: 1; height: 1px; background: #ebebeb;"></div>
  <span style="font-size: 13px; color: #bbb; white-space: nowrap;">— 分节文字 —</span>
  <div style="flex: 1; height: 1px; background: #ebebeb;"></div>
</div>
```

---

## 十、列表

### 无序列表
```html
<ul style="margin: 16px 0; padding: 0; list-style: none;">
  <li style="display: flex; gap: 10px; margin-bottom: 10px; font-size: 15px; color: #3d3d3d; line-height: 1.7; align-items: flex-start;">
    <span style="color: #07c160; font-size: 18px; line-height: 1.4; flex-shrink: 0;">•</span>
    <span>列表项内容</span>
  </li>
</ul>
```

### 有序列表
```html
<ol style="margin: 16px 0; padding: 0; list-style: none; counter-reset: ol-counter;">
  <li style="display: flex; gap: 10px; margin-bottom: 10px; font-size: 15px; color: #3d3d3d; line-height: 1.7; align-items: flex-start; counter-increment: ol-counter;">
    <span style="color: #07c160; font-weight: bold; min-width: 20px; flex-shrink: 0;">1.</span>
    <span>列表项内容</span>
  </li>
</ol>
```

---

## 十一、文章结尾（署名 + 互动引导）

```html
<div style="margin: 48px 0 32px; text-align: center; padding: 24px; background: linear-gradient(135deg, #f0faf4 0%, #e8f5ef 100%); border-radius: 12px;">
  <p style="font-size: 16px; color: #333; margin: 0 0 12px; line-height: 1.8;">
    如果这篇文章对你有帮助，欢迎点赞👍 在看📖 转发🔁
  </p>
  <p style="font-size: 14px; color: #999; margin: 0;">遇到问题评论区聊聊 👇</p>
</div>
```

---

## 十二、完整 HTML 文档模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>文章标题</title>
</head>
<body>
<section style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', Arial, sans-serif; font-size: 16px; color: #3d3d3d; line-height: 1.8; padding: 0 16px; max-width: 677px; margin: 0 auto; word-break: break-word;">

  <!-- H1 主标题 -->
  <h1 style="font-size: 24px; font-weight: bold; color: #1a1a1a; text-align: center; margin: 32px 0 8px; line-height: 1.4;">文章标题</h1>
  <div style="width: 48px; height: 4px; background: #07c160; border-radius: 2px; margin: 0 auto 32px;"></div>

  <!-- 正文内容 -->
  
</section>
</body>
</html>
```

---

## 十二、图片组件

### 封面题图（H1 主标题之后，必须有）
```html
<figure style="margin: 28px 0; text-align: center;">
  <img src="图片URL" alt="文章主题关键词"
       style="max-width: 100%; border-radius: 12px; display: block; margin: 0 auto;
              box-shadow: 0 6px 24px rgba(0,0,0,0.14);" />
  <figcaption style="font-size: 13px; color: #999; margin-top: 8px; line-height: 1.6; font-style: italic;">▲ 封面图</figcaption>
</figure>
```

### 全宽章节配图（H2 章节内容区块内）
```html
<figure style="margin: 28px 0; text-align: center;">
  <img src="图片URL" alt="章节主题关键词"
       style="max-width: 100%; border-radius: 8px; display: block; margin: 0 auto;
              box-shadow: 0 4px 16px rgba(0,0,0,0.10);" />
  <figcaption style="font-size: 13px; color: #999; margin-top: 8px; line-height: 1.6; font-style: italic;">图片说明文字</figcaption>
</figure>
```

### 小图插图（正文中偏小的说明图，宽度 80%）
```html
<figure style="margin: 20px auto; text-align: center; max-width: 80%;">
  <img src="图片URL" alt="说明关键词"
       style="max-width: 100%; border-radius: 8px; display: block; margin: 0 auto;" />
  <figcaption style="font-size: 13px; color: #999; margin-top: 8px; font-style: italic;">说明文字</figcaption>
</figure>
```

### 图片占位符（开发/排版阶段使用）
```html
<!-- [AUTO_IMAGE] prompt="章节主题, minimalist flat illustration, no text" width=677 height=340 -->
<figure style="margin: 28px 0; text-align: center;">
  <img src="https://via.placeholder.com/677x340/e8f5ef/07c160?text=配图占位"
       alt="章节关键词"
       style="max-width: 100%; border-radius: 8px; display: block; margin: 0 auto;
              box-shadow: 0 4px 16px rgba(0,0,0,0.10);" />
  <figcaption style="font-size: 13px; color: #999; margin-top: 8px; font-style: italic;">▲ 章节配图</figcaption>
</figure>
```

### 图片位置策略

| 位置 | 图片类型 | 触发条件 | 推荐尺寸 |
|------|---------|---------|---------|
| H1 之后 | 封面题图 | 每篇必须 | 677×340（横版）|
| H2 章节内（章节≥80字）| 章节配图 | 每章节可有 1 张 | 677×340 或 677×677 |
| 步骤说明之后（可选）| 步骤插图 | 有实操截图时 | 677×auto |
| 文章结尾 | 结尾装饰图 | 可选 | 677×200 |

### AI 生成图片提示词规范

生成公众号配图时，提示词遵循以下模板：
- **基础结构**：`{内容主题}, {风格描述}, {颜色描述}, no text, no watermark, no logo`
- **推荐风格**：`minimalist flat illustration`、`isometric vector art`、`clean digital art`
- **推荐颜色**：soft green and white、light pastel、neutral tones
- **示例**：`"knowledge management workflow, connected nodes diagram, minimalist flat illustration, soft green and white color palette, no text, no watermark"`

---

## 完整 HTML 文档模板（含图片）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>文章标题</title>
</head>
<body>
<section style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', Arial, sans-serif; font-size: 16px; color: #3d3d3d; line-height: 1.8; padding: 0 16px; max-width: 677px; margin: 0 auto; word-break: break-word;">

  <!-- H1 主标题 -->
  <h1 style="font-size: 24px; font-weight: bold; color: #1a1a1a; text-align: center; margin: 32px 0 8px; line-height: 1.4;">文章标题</h1>
  <div style="width: 48px; height: 4px; background: #07c160; border-radius: 2px; margin: 0 auto 32px;"></div>

  <!-- 封面题图（H1 之后必须插入）-->
  <figure style="margin: 28px 0; text-align: center;">
    <img src="封面图片URL" alt="文章主题"
         style="max-width: 100%; border-radius: 12px; display: block; margin: 0 auto;
                box-shadow: 0 6px 24px rgba(0,0,0,0.14);" />
    <figcaption style="font-size: 13px; color: #999; margin-top: 8px; line-height: 1.6; font-style: italic;">▲ 封面图</figcaption>
  </figure>

  <!-- 正文内容 -->

  <!-- H2 章节标题 -->
  <h2 style="font-size: 18px; font-weight: bold; color: #1a1a1a; margin: 40px 0 16px; padding: 10px 16px; background: #e8f5ef; border-left: 4px solid #07c160; border-radius: 0 6px 6px 0; line-height: 1.5;">章节标题</h2>

  <!-- 章节内容段落 -->
  <p style="font-size: 16px; color: #3d3d3d; line-height: 1.8; margin: 0 0 20px;">段落内容</p>

  <!-- 章节配图 -->
  <figure style="margin: 28px 0; text-align: center;">
    <img src="章节图片URL" alt="章节主题"
         style="max-width: 100%; border-radius: 8px; display: block; margin: 0 auto;
                box-shadow: 0 4px 16px rgba(0,0,0,0.10);" />
    <figcaption style="font-size: 13px; color: #999; margin-top: 8px; line-height: 1.6; font-style: italic;">图片说明</figcaption>
  </figure>

</section>
</body>
</html>
```

---

## 重要约束（微信编辑器兼容性）

1. **所有样式必须内联**（inline style），不能使用 `<style>` 标签
2. **不使用外部字体**（Google Fonts 等）
3. **不使用 JavaScript**
4. **不使用 CSS 变量**（`var(--color)` 不被支持）
5. **不使用 `flexbox` 的 `gap` 属性**（部分旧版微信不支持），改用 `margin`
6. **图片使用** `max-width: 100%; display: block; margin: 0 auto;`
7. **链接色** 统一用 `#576b95`
8. **图片上传**：公众号编辑器需要先上传图片获取微信 CDN 地址，不能直接使用外链图片

---

## 十三、进阶排版组件（卡片 + 展示风格）

> 以下组件适合用于：技能说明页、演示页、对比页、教程索引页等非纯文章内容场景。风格更现代、层次更清晰。

### 页面 Header（渐变标题栏）

适用于文档顶部或分节大标题区域：

```html
<div style="background: linear-gradient(135deg, #07c160, #0a9c4a); color: #fff; border-radius: 16px; padding: 40px; margin-bottom: 24px;">
  <h1 style="margin: 0 0 8px; font-size: 28px; font-weight: 800;">🎨 技能标题</h1>
  <p style="margin: 0; opacity: 0.9; font-size: 16px;">技能副标题描述文字</p>
  <span style="display: inline-block; background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px; font-size: 13px; margin-top: 12px;">🏷️ 标签</span>
</div>
```

### 卡片式内容区块

适用于功能分组、特性说明：

```html
<div style="background: #fff; border-radius: 12px; padding: 32px; margin-bottom: 24px; box-shadow: 0 2px 12px rgba(0,0,0,0.06);">
  <h2 style="font-size: 20px; font-weight: 700; color: #1a1a1a; margin: 0 0 20px; padding-left: 14px; border-left: 4px solid #07c160;">📊 章节标题</h2>
  <!-- 区块内容 -->
</div>
```

### Feature 卡片组（2列网格）

适用于展示多个功能点，每个卡片有浅绿背景和绿色强调：

```html
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px;">
  <div style="background: #f7faf8; border: 1px solid #b7dfc8; border-radius: 10px; padding: 18px;">
    <h3 style="margin: 0 0 8px; font-size: 15px; color: #07c160; display: flex; align-items: center; gap: 6px;">🖼️ 功能名称</h3>
    <p style="margin: 0; font-size: 14px; color: #555; line-height: 1.7;">功能描述文字</p>
  </div>
</div>
```

### 对比表格（Diff Table）

适用于改造前后对比、能力对比等场景：

```html
<table style="width: 100%; border-collapse: collapse; margin-top: 16px; font-size: 14px;">
  <thead>
    <tr>
      <th style="background: #f7f7f7; padding: 10px 16px; text-align: left; font-weight: 600; color: #555; border-bottom: 2px solid #e8e8e8;">能力</th>
      <th style="background: #f7f7f7; padding: 10px 16px; text-align: left; font-weight: 600; color: #555; border-bottom: 2px solid #e8e8e8;">原版</th>
      <th style="background: #f7f7f7; padding: 10px 16px; text-align: left; font-weight: 600; color: #555; border-bottom: 2px solid #e8e8e8;">新版</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px 16px; border-bottom: 1px solid #f0f0f0; color: #3d3d3d;">功能项</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #f0f0f0; color: #cf1322;">❌ 不支持</td>
      <td style="padding: 12px 16px; border-bottom: 1px solid #f0f0f0; color: #389e0d;">✅ 支持</td>
    </tr>
  </tbody>
</table>

<!-- 版本标签 -->
<span style="display: inline-block; background: #fff2f0; color: #cf1322; border-radius: 4px; padding: 2px 8px; font-size: 12px; font-weight: 600;">旧版</span>
<span style="display: inline-block; background: #f6ffed; color: #389e0d; border-radius: 4px; padding: 2px 8px; font-size: 12px; font-weight: 600;">新版</span>
```

### 文件目录树（File Tree）

适用于展示项目结构，目录蓝色、文件深灰、新增绿色、修改橙色：

```html
<div style="background: #f6f8fa; border: 1px solid #e1e4e8; border-radius: 8px; padding: 20px; font-family: 'Menlo', 'Consolas', monospace; font-size: 13px; line-height: 2;">
  <span style="color: #0366d6; font-weight: 600;">project/</span><br>
  &nbsp;&nbsp;├── <span style="color: #24292e;">README.md</span><br>
  &nbsp;&nbsp;├── <span style="color: #22863a; font-weight: 600;">SKILL.md</span> <span style="color:#6a737d;"># 新增文件</span><br>
  &nbsp;&nbsp;└── <span style="color: #e36209;">scripts/</span> <span style="color:#6a737d;"># 修改目录</span>
</div>
```

### 步骤流程（Steps）

适用于操作步骤指引：

```html
<div style="counter-reset: step; margin: 24px 0;">
  <div style="display: flex; gap: 16px; margin-bottom: 20px; align-items: flex-start;">
    <div style="flex-shrink: 0; width: 32px; height: 32px; background: #07c160; color: #fff; font-size: 14px; font-weight: 700; border-radius: 50%; display: flex; align-items: center; justify-content: center;">1</div>
    <div style="flex: 1;">
      <p style="font-size: 15px; font-weight: 700; color: #1a1a1a; margin: 0 0 6px;">步骤标题</p>
      <p style="font-size: 14px; color: #555; line-height: 1.7; margin: 0;">步骤说明内容</p>
    </div>
  </div>
</div>
```

### 代码块（带语法高亮）

适用于展示代码示例，支持关键字/字符串/注释/标签着色：

```html
<div style="background: #f6f8fa; border: 1px solid #e1e4e8; border-radius: 8px; padding: 16px; font-family: 'Menlo', 'Consolas', monospace; font-size: 13px; line-height: 1.7; overflow-x: auto; margin: 16px 0;">
<span style="color: #6a737d;"># 注释文字</span>
<span style="color: #d73a49;">if</span> <span style="color: #24292e;">condition:</span>
  <span style="color: #22863a;">&lt;tag</span> <span style="color: #032f62;">"value"</span><span style="color: #22863a;">&gt;</span>
</div>
```

> **内联代码**（短代码片段）：
> ```html
> <code style="font-family: 'Menlo', monospace; font-size: 13px; background: #f6f8fa; color: #e96900; padding: 2px 6px; border-radius: 4px; border: 1px solid #e1e4e8;">代码</code>
> ```

### Feature 标签（Chip / Badge）

适用于展示功能关键词：

```html
<span style="display: inline-flex; align-items: center; gap: 4px; background: #e8f5ef; color: #07c160; font-size: 12px; font-weight: 600; padding: 3px 10px; border-radius: 12px; margin: 4px 4px 4px 0;">✨ 功能名</span>
```

### 警告提示框（Warning）

黄色背景，适用于上传说明、注意事项：

```html
<div style="background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; padding: 16px; margin: 16px 0;">
  <p style="margin: 0; font-size: 14px; color: #7c5e00; line-height: 1.8;">
    <strong>⚠️ 注意：</strong>提示内容文字
  </p>
</div>
```

### 完整展示页模板（技能说明页）

整合以上所有组件，适合作为技能说明文章：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>技能名称</title>
</head>
<body style="margin: 0; padding: 20px; background: #f0f2f5; font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', Arial, sans-serif;">
<div style="max-width: 960px; margin: 0 auto;">

  <!-- 页面 Header -->
  <div style="background: linear-gradient(135deg, #07c160, #0a9c4a); color: #fff; border-radius: 16px; padding: 40px; margin-bottom: 24px;">
    <h1 style="margin: 0 0 8px; font-size: 28px; font-weight: 800;">技能标题</h1>
    <p style="margin: 0; opacity: 0.9; font-size: 16px;">技能副标题</p>
    <span style="display: inline-block; background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px; font-size: 13px; margin-top: 12px;">✅ 完成</span>
  </div>

  <!-- 卡片区块 -->
  <div style="background: #fff; border-radius: 12px; padding: 32px; margin-bottom: 24px; box-shadow: 0 2px 12px rgba(0,0,0,0.06);">
    <h2 style="font-size: 20px; font-weight: 700; color: #1a1a1a; margin: 0 0 20px; padding-left: 14px; border-left: 4px solid #07c160;">核心功能</h2>

    <!-- Feature 卡片组 -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
      <div style="background: #f7faf8; border: 1px solid #b7dfc8; border-radius: 10px; padding: 18px;">
        <h3 style="margin: 0 0 8px; font-size: 15px; color: #07c160;">✨ 功能一</h3>
        <p style="margin: 0; font-size: 14px; color: #555; line-height: 1.7;">描述</p>
      </div>
      <div style="background: #f7faf8; border: 1px solid #b7dfc8; border-radius: 10px; padding: 18px;">
        <h3 style="margin: 0 0 8px; font-size: 15px; color: #07c160;">🚀 功能二</h3>
        <p style="margin: 0; font-size: 14px; color: #555; line-height: 1.7;">描述</p>
      </div>
    </div>
  </div>

</div>
</body>
</html>
```
