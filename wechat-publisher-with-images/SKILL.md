---
name: wechat-publisher-with-images
description: "微信公众号图文发布工具（含 AI 配图）。将普通文章/Markdown内容转换为风格统一的微信公众号HTML排版，并在合适位置自动生成/插入配图。包括：标题样式、正文样式、引用块、代码块、步骤列表、卡片式分节导航、强调文字、分割线、图片组件（封面图、章节配图、说明插图）等。参考风格来自「摸鱼小李」公众号。"
description_zh: "将文章内容转换为带 AI 配图的微信公众号图文排版格式"
description_en: "Convert article content to WeChat Official Account HTML layout with AI-generated images"
---

# 微信公众号排版技能（带图版）

将任意文章、Markdown、或纯文字内容，自动排版为**微信公众号可直接粘贴使用**的 HTML 格式，并在合适位置插入配图。风格参考「摸鱼小李」公众号。

## 工作流程

1. **接收内容** → 用户提供原始文章、Markdown 或纯文字
2. **分析结构** → 识别标题层级、段落、代码块、列表、引用等，**同时分析适合插图的位置**
3. **规划配图** → 确定图片数量（通常 2-5 张）、类型（封面图/章节图/插图）、风格和关键词
4. **生成/获取图片** → 使用 `image_gen` 工具生成 AI 配图，按需生成
5. **生成排版** → 输出完整 HTML，图片以内联 `<img>` 标签嵌入，调用 `scripts/format.py` 或直接手工生成
6. **预览确认** → 输出 HTML 预览文件，供用户查看效果
7. **输出交付** → 提供可直接复制到微信公众号编辑器的 HTML 内容

---

## 图片插入规则

### 图片位置选择策略

| 位置 | 图片类型 | 触发条件 | 尺寸 |
|------|---------|---------|------|
| 文章最顶部（H1之后） | **封面题图** | 每篇文章必须有 | 1024×512（横版）|
| 每个 H2 章节之前/之后 | **章节配图** | 章节内容≥100字时 | 1024×512 或 1024×1024 |
| 步骤说明旁 | **步骤插图** | Step N 组件后，步骤有实操内容时 | 可选 |
| 文章结尾 | **结尾装饰图** | 可选，用于品牌感收尾 | 1024×256（横幅）|
| Markdown 中已有 `![...]()` | **用户指定图** | 直接渲染，不替换 | 保持原始 |

### 图片生成提示词规范

生成图片时，提示词（prompt）需要：
1. **风格统一**：偏向简洁、现代、扁平风格，适合科技/知识类公众号
2. **与内容相关**：根据该章节/段落的核心主题生成
3. **颜色和谐**：主色调偏向微信绿（#07c160）或中性色调
4. **无文字水印**：提示词加 `no text, no watermark, no logo`
5. **示例提示词**：
   - 知识管理类：`"minimalist flat illustration, knowledge management workflow, connected nodes, soft green and white color palette, modern tech style, no text, no watermark"`
   - AI工具类：`"clean vector illustration, AI assistant robot helping human, friendly style, light green accent, no text"`
   - 技术教程类：`"isometric flat illustration, computer programming, code editor screen, soft colors, no text, no watermark"`

### 图片 HTML 组件样式

#### 全宽配图（封面图/章节图）
```html
<figure style="margin: 24px 0; text-align: center;">
  <img src="图片路径或URL" alt="图片描述"
       style="max-width: 100%; border-radius: 8px; display: block; margin: 0 auto;" />
  <figcaption style="font-size: 13px; color: #999; margin-top: 8px; line-height: 1.6;">图片说明文字</figcaption>
</figure>
```

#### 带圆角阴影的精美配图
```html
<figure style="margin: 32px 0; text-align: center;">
  <img src="图片路径或URL" alt="图片描述"
       style="max-width: 100%; border-radius: 12px; display: block; margin: 0 auto;
              box-shadow: 0 4px 20px rgba(0,0,0,0.12);" />
  <figcaption style="font-size: 13px; color: #999; margin-top: 10px; font-style: italic;">图片说明</figcaption>
</figure>
```

#### 小图（行内插图，50%宽）
```html
<figure style="margin: 20px auto; text-align: center; max-width: 50%;">
  <img src="图片路径或URL" alt="图片描述"
       style="max-width: 100%; border-radius: 8px; display: block; margin: 0 auto;" />
</figure>
```

---

## 排版风格规范

排版细节完整定义见 `references/style-guide.md`，核心要点如下：

> 💡 **高阶展示组件**：第十三节新增了适合技能说明页、演示页的组件（卡片布局、Diff Table、File Tree、Feature Card、代码语法高亮等），可参考 `demo-改造说明.html` 的实际效果。

### 配色方案
- 主色：`#1a1a1a`（正文）
- 强调色：`#07c160`（微信绿，用于左边框装饰、按钮）
- 标题色：`#333`
- 辅助色：`#666`（副标题、说明文字）
- 背景色：`#fff`（主背景），`#f7f7f7`（代码块/引用背景）
- 链接色：`#576b95`

### 标题系统（三级）
- **H1 主标题**：24px，加粗，底部绿色下划线装饰，`margin-bottom: 24px`
- **H2 章节标题**：带绿色左边框（4px solid #07c160），浅绿背景，18px，加粗
- **H3 小节标题**：带圆形数字序号装饰或 emoji 前缀，16px，加粗

### 正文样式
- 字号：16px
- 行高：1.8
- 颜色：`#3d3d3d`
- 段间距：`margin-bottom: 20px`
- 不首行缩进（微信公众号规范）

### 特殊组件
- **引用块**：左侧 4px 绿色竖条，浅灰背景 `#f7f7f7`，内边距 12px 16px
- **代码块**：灰色背景 `#f6f8fa`，圆角 6px，等宽字体，关键字橙红色 `#e96900`
- **步骤列表**（Step 1/2...）：圆形序号 + 加粗标题 + 缩进说明
- **卡片组**（Part 01/02...）：横向排列，带编号圆圈，绿色强调
- **小贴士/提示框**：浅黄/浅绿背景，emoji 前缀，圆角
- **分割线**：细灰线 `1px solid #ebebeb`，上下留白 24px

### 可复制按钮块
重要的可操作命令/内容，用带边框的代码框 + 顶部标注"📋 复制发给助手"展示。

---

## 使用方式

### 方式1：直接生成（推荐，带 AI 配图）

用户提供内容后，按以下步骤操作：

1. 分析文章结构，规划图片插入位置
2. 用 `image_gen` 工具逐张生成配图，保存到工作目录
3. 将图片路径嵌入 HTML `<img>` 标签
4. 手工生成完整排版 HTML

输出格式：
```
以下是带配图的排版 HTML，可直接复制到微信公众号编辑器：

[HTML 内容]

预览文件已保存到：[路径]
配图已生成并嵌入：共 N 张
```

### 方式2：运行脚本（支持配图选项）

```bash
python scripts/format.py --input article.md --output output.html
python scripts/format.py --input article.md --output output.html --with-images
python scripts/format.py --input article.md --output output.html --image-style "flat illustration"
```

参数：
- `--input`：输入文件（Markdown 或 txt）
- `--output`：输出 HTML 文件路径（默认 `output.html`）
- `--title`：文章标题（可选，会覆盖正文中的 H1）
- `--theme`：主题色（默认 `#07c160`，可自定义）
- `--with-images`：启用图片占位符模式（在合适位置插入图片占位注释）
- `--image-style`：图片风格描述（默认 `"minimalist flat illustration"`）
- `--no-cover`：跳过封面图生成

---

## 内容结构识别规则

| 原始内容 | 转换为 |
|---------|--------|
| `# 标题` / 一级标题 | H1 主标题样式 + 封面图 |
| `## 章节` / 二级标题 | H2 绿色左边框章节标题 + 可选章节配图 |
| `### 小节` / 三级标题 | H3 带序号小节标题 |
| `> 引用` | 绿色左条引用块 |
| `` ` `` 代码 `` ` `` | 行内代码（橙红色） |
| ```` ``` ```` 代码块 | 灰色背景代码框 |
| `**加粗**` | 加粗 + 强调色文字 |
| `Step 1:` / 步骤 | 圆形序号步骤组件 |
| `Part 01` / 部分卡片 | 卡片式分节导航组件 |
| `📋 复制...` 后跟代码 | 可复制命令框 |
| `---` 分割线 | 细灰分割线 |
| `![alt](url)` 图片 | 全宽图片组件（figcaption 用 alt 文字）|
| `![alt](AUTO)` | 触发 AI 图片生成，关键词从 alt 提取 |
| 普通段落 | 标准正文段落 |

## 注意事项

- 微信公众号编辑器不支持外部字体，不要引用 Google Fonts
- 所有样式必须**内联（inline style）**，不能用 `<style>` 标签（粘贴到微信编辑器时会丢失）
- 图片使用 `max-width: 100%; display: block; margin: 0 auto;`，确保移动端适配
- 不使用 JavaScript（微信不支持）
- 整体宽度约 94%，两侧留白，适配微信移动端
- **AI 生成的图片**保存在工作目录的 `generated-images/` 文件夹下，上传公众号后替换路径
- 图片数量建议：**短文（<1000字）2-3 张，中文（1000-3000字）3-5 张，长文（>3000字）5-8 张**
