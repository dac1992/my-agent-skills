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

## 重要约束（微信编辑器兼容性）

1. **所有样式必须内联**（inline style），不能使用 `<style>` 标签
2. **不使用外部字体**（Google Fonts 等）
3. **不使用 JavaScript**
4. **不使用 CSS 变量**（`var(--color)` 不被支持）
5. **不使用 `flexbox` 的 `gap` 属性**（部分旧版微信不支持），改用 `margin`
6. **图片使用** `max-width: 100%; display: block; margin: 0 auto;`
7. **链接色** 统一用 `#576b95`
