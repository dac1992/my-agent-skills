#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号排版转换脚本（带图版）
将 Markdown 或纯文本转换为可直接粘贴到微信公众号编辑器的 HTML
支持自动在合适位置插入配图占位符或实际图片

用法：
    python format.py --input article.md --output output.html
    python format.py --input article.md --output output.html --with-images
    python format.py --input article.txt --title "我的文章" --theme "#07c160"
    python format.py --input article.md --output output.html --image-style "flat illustration"
"""

import re
import sys
import argparse
from pathlib import Path


# ─── 主题色配置 ────────────────────────────────────────────────────────────────
DEFAULT_THEME = "#07c160"
DEFAULT_THEME_LIGHT = "#e8f5ef"
DEFAULT_THEME_BORDER = "#b7dfc8"

# ─── 图片配置 ──────────────────────────────────────────────────────────────────
DEFAULT_IMAGE_STYLE = "minimalist flat illustration, soft colors, modern tech style, no text, no watermark, no logo"
DEFAULT_IMAGE_PLACEHOLDER = "https://via.placeholder.com/677x340/e8f5ef/07c160?text=配图占位"

# 图片插入策略：每隔多少个 H2 章节插一张图
IMAGE_EVERY_N_SECTIONS = 1  # 每个章节都尝试插图

# ─── 样式常量 ──────────────────────────────────────────────────────────────────
FONT_FAMILY = "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', Arial, sans-serif"
MONO_FAMILY = "'Menlo', 'Monaco', 'Consolas', monospace"


def build_styles(theme: str = DEFAULT_THEME) -> dict:
    """根据主题色构建样式字典"""
    light = DEFAULT_THEME_LIGHT
    border = DEFAULT_THEME_BORDER

    return {
        "container": (
            f"font-family: {FONT_FAMILY}; font-size: 16px; color: #3d3d3d; "
            f"line-height: 1.8; padding: 0 16px; max-width: 677px; "
            f"margin: 0 auto; word-break: break-word;"
        ),
        "h1": (
            f"font-size: 24px; font-weight: bold; color: #1a1a1a; "
            f"text-align: center; margin: 32px 0 8px; line-height: 1.4;"
        ),
        "h1_underline": (
            f"width: 48px; height: 4px; background: {theme}; "
            f"border-radius: 2px; margin: 0 auto 32px;"
        ),
        "h2": (
            f"font-size: 18px; font-weight: bold; color: #1a1a1a; "
            f"margin: 40px 0 16px; padding: 10px 16px; "
            f"background: {light}; border-left: 4px solid {theme}; "
            f"border-radius: 0 6px 6px 0; line-height: 1.5;"
        ),
        "h3": (
            f"font-size: 16px; font-weight: bold; color: #1a1a1a; "
            f"margin: 28px 0 12px; padding-left: 12px; "
            f"border-left: 3px solid {theme}; line-height: 1.5;"
        ),
        "p": (
            f"font-size: 16px; color: #3d3d3d; line-height: 1.8; "
            f"margin: 0 0 20px;"
        ),
        "blockquote": (
            f"margin: 20px 0; padding: 12px 16px; background: #f7f7f7; "
            f"border-left: 4px solid {theme}; border-radius: 0 6px 6px 0; "
            f"color: #555; font-size: 15px; line-height: 1.8;"
        ),
        "code_inline": (
            f"font-family: {MONO_FAMILY}; font-size: 14px; background: #f6f8fa; "
            f"color: #e96900; padding: 2px 6px; border-radius: 4px; "
            f"border: 1px solid #e1e4e8;"
        ),
        "code_block_wrap": (
            f"margin: 20px 0; border-radius: 8px; overflow: hidden; "
            f"border: 1px solid #e1e4e8;"
        ),
        "code_block_header": (
            f"background: #f0f0f0; padding: 8px 16px; font-size: 12px; "
            f"color: #666; border-bottom: 1px solid #e1e4e8; font-family: {MONO_FAMILY};"
        ),
        "code_block_pre": (
            f"margin: 0; padding: 16px; background: #f6f8fa; overflow-x: auto; "
            f"font-size: 14px; line-height: 1.6; white-space: pre-wrap; word-break: break-all;"
        ),
        "code_block_code": (
            f"font-family: {MONO_FAMILY}; color: #24292e;"
        ),
        "copy_block_wrap": (
            f"margin: 20px 0; border-radius: 8px; overflow: hidden; "
            f"border: 1px solid {border};"
        ),
        "copy_block_header": (
            f"background: {light}; padding: 8px 16px; font-size: 13px; "
            f"color: {theme}; font-weight: bold; border-bottom: 1px solid {border};"
        ),
        "copy_block_pre": (
            f"margin: 0; padding: 16px; background: #f9fdfb; overflow-x: auto; "
            f"font-size: 14px; line-height: 1.7; white-space: pre-wrap; word-break: break-all;"
        ),
        "tip_green": (
            f"margin: 20px 0; padding: 14px 16px; background: {light}; "
            f"border-radius: 8px; border: 1px solid {border};"
        ),
        "tip_green_text": (
            f"margin: 0; font-size: 15px; color: #2d7a4f; line-height: 1.7;"
        ),
        "tip_yellow": (
            f"margin: 20px 0; padding: 14px 16px; background: #fffbe6; "
            f"border-radius: 8px; border: 1px solid #ffe58f;"
        ),
        "tip_yellow_text": (
            f"margin: 0; font-size: 15px; color: #7c5e00; line-height: 1.7;"
        ),
        "divider": (
            f"margin: 32px 0; height: 1px; background: #ebebeb;"
        ),
        "step_wrap": (
            f"display: flex; margin-bottom: 24px; align-items: flex-start;"
        ),
        "step_num": (
            f"flex-shrink: 0; width: 32px; height: 32px; background: {theme}; "
            f"color: #fff; font-size: 14px; font-weight: bold; border-radius: 50%; "
            f"display: flex; align-items: center; justify-content: center; "
            f"margin-top: 2px; margin-right: 16px; text-align: center; line-height: 32px;"
        ),
        "step_content": "flex: 1;",
        "step_title": (
            f"font-size: 16px; font-weight: bold; color: #1a1a1a; "
            f"margin: 0 0 8px; line-height: 1.5;"
        ),
        "step_desc": (
            f"font-size: 15px; color: #555; line-height: 1.8; margin: 0;"
        ),
        "ul_item": (
            f"display: flex; margin-bottom: 10px; font-size: 15px; "
            f"color: #3d3d3d; line-height: 1.7; align-items: flex-start;"
        ),
        "ul_bullet": (
            f"color: {theme}; font-size: 18px; line-height: 1.4; "
            f"flex-shrink: 0; margin-right: 10px; font-weight: bold;"
        ),
        "footer": (
            f"margin: 48px 0 32px; text-align: center; padding: 24px; "
            f"background: linear-gradient(135deg, #f0faf4 0%, {light} 100%); "
            f"border-radius: 12px;"
        ),
        "footer_text": (
            f"font-size: 16px; color: #333; margin: 0 0 12px; line-height: 1.8;"
        ),
        "footer_sub": (
            f"font-size: 14px; color: #999; margin: 0;"
        ),
        "strong": (
            f"color: #1a1a1a; font-weight: bold;"
        ),
        "link": (
            f"color: #576b95; text-decoration: none;"
        ),
        # ── 图片组件样式 ──────────────────────────────────────────────
        "figure": (
            f"margin: 28px 0; text-align: center;"
        ),
        "img_full": (
            f"max-width: 100%; border-radius: 8px; display: block; margin: 0 auto; "
            f"box-shadow: 0 4px 16px rgba(0,0,0,0.10);"
        ),
        "img_cover": (
            f"max-width: 100%; border-radius: 12px; display: block; margin: 0 auto; "
            f"box-shadow: 0 6px 24px rgba(0,0,0,0.14);"
        ),
        "img_inline": (
            f"max-width: 80%; border-radius: 8px; display: block; margin: 0 auto;"
        ),
        "figcaption": (
            f"font-size: 13px; color: #999; margin-top: 8px; line-height: 1.6; "
            f"font-style: italic;"
        ),
        # 图片占位符注释样式（仅用于 --with-images 模式）
        "img_placeholder_wrap": (
            f"margin: 28px 0; padding: 20px; text-align: center; "
            f"background: #f7faf8; border: 2px dashed #b7dfc8; border-radius: 10px;"
        ),
        "img_placeholder_text": (
            f"font-size: 14px; color: #07c160; margin: 0;"
        ),
    }


# ─── 图片 HTML 生成器 ──────────────────────────────────────────────────────────

def make_image_html(src: str, alt: str = "", caption: str = "",
                    style_key: str = "img_full", s: dict = None,
                    is_placeholder: bool = False) -> str:
    """生成图片 HTML 组件"""
    if s is None:
        s = build_styles()

    if is_placeholder:
        # 占位符模式：输出带说明的占位区域
        placeholder_src = DEFAULT_IMAGE_PLACEHOLDER
        keyword_hint = f"关键词：{alt}" if alt else "请替换为实际图片"
        return (
            f'<figure style="{s["figure"]}">\n'
            f'  <!-- AI配图占位符 | {keyword_hint} -->\n'
            f'  <img src="{placeholder_src}" alt="{escape_html(alt)}"\n'
            f'       style="{s[style_key]}" />\n'
            f'  <figcaption style="{s["figcaption"]}">'
            f'{escape_html(caption) if caption else escape_html(alt)}</figcaption>\n'
            f'</figure>\n'
        )
    else:
        cap_html = f'\n  <figcaption style="{s["figcaption"]}">{escape_html(caption)}</figcaption>' if caption else ""
        return (
            f'<figure style="{s["figure"]}">\n'
            f'  <img src="{escape_html(src)}" alt="{escape_html(alt)}"\n'
            f'       style="{s[style_key]}" />'
            f'{cap_html}\n'
            f'</figure>\n'
        )


def make_section_image_placeholder(section_title: str, s: dict,
                                    image_style: str = DEFAULT_IMAGE_STYLE) -> str:
    """为章节生成自动插图占位符（--with-images 模式下使用）"""
    clean_title = re.sub(r'[^\w\s\u4e00-\u9fff]', '', section_title).strip()
    hint = f"{clean_title}, {image_style}"
    return (
        f'<!-- [AUTO_IMAGE] prompt="{hint}" width=677 height=340 -->\n'
        f'<figure style="{s["figure"]}">\n'
        f'  <img src="{DEFAULT_IMAGE_PLACEHOLDER}" alt="{escape_html(clean_title)}"\n'
        f'       style="{s["img_full"]}" />\n'
        f'  <figcaption style="{s["figcaption"]}">▲ {escape_html(clean_title)}</figcaption>\n'
        f'</figure>\n'
    )


# ─── 转换函数 ──────────────────────────────────────────────────────────────────

def escape_html(text: str) -> str:
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;"))


def process_inline(text: str, s: dict) -> str:
    """处理行内格式：加粗、代码、链接、斜体"""
    # 行内代码
    text = re.sub(
        r'`([^`]+)`',
        lambda m: f'<code style="{s["code_inline"]}">{escape_html(m.group(1))}</code>',
        text
    )
    # 加粗
    text = re.sub(
        r'\*\*(.+?)\*\*',
        lambda m: f'<strong style="{s["strong"]}">{m.group(1)}</strong>',
        text
    )
    # 斜体
    text = re.sub(
        r'\*(.+?)\*',
        lambda m: f'<em>{m.group(1)}</em>',
        text
    )
    # 链接
    text = re.sub(
        r'\[(.+?)\]\((.+?)\)',
        lambda m: f'<a href="{m.group(2)}" style="{s["link"]}">{m.group(1)}</a>',
        text
    )
    return text


def process_image_line(line: str, s: dict) -> str:
    """
    处理 Markdown 图片语法：
    - ![alt](url)          → 全宽图片组件
    - ![alt](AUTO)         → AI 自动生成占位（实际生成需 AI 工具介入）
    - ![alt|caption](url)  → 带说明文字的图片
    """
    img_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$', line.strip())
    if not img_match:
        return None

    raw_alt = img_match.group(1)
    src = img_match.group(2).strip()

    # 解析 alt|caption 格式
    if "|" in raw_alt:
        alt, caption = raw_alt.split("|", 1)
        alt = alt.strip()
        caption = caption.strip()
    else:
        alt = raw_alt.strip()
        caption = alt  # 默认用 alt 作为说明文字

    # AUTO 模式：生成占位符
    if src.upper() == "AUTO":
        return make_image_html(
            src=DEFAULT_IMAGE_PLACEHOLDER,
            alt=alt,
            caption=caption,
            style_key="img_full",
            s=s,
            is_placeholder=True
        )

    # 普通图片
    return make_image_html(src=src, alt=alt, caption=caption, style_key="img_full", s=s)


def parse_markdown(md: str, theme: str = DEFAULT_THEME,
                   with_images: bool = False,
                   image_style: str = DEFAULT_IMAGE_STYLE,
                   no_cover: bool = False) -> str:
    """
    将 Markdown 转换为微信公众号 HTML

    参数：
        md: Markdown 文本
        theme: 主题色
        with_images: 是否在章节处自动插入图片占位符
        image_style: AI 图片风格描述（用于生成提示词）
        no_cover: 是否跳过封面图
    """
    s = build_styles(theme)
    lines = md.split("\n")
    html_parts = []

    i = 0
    in_code_block = False
    code_lang = ""
    code_lines = []
    is_copy_block = False
    in_ul = False
    ul_items = []
    h1_seen = False        # 是否已处理第一个 H1（用于决定是否插封面图）
    h2_count = 0           # H2 章节计数（用于控制图片插入频率）
    section_char_count = 0  # 当前章节字符数（决定是否值得插图）
    current_section_title = ""  # 当前章节标题

    def flush_ul():
        nonlocal in_ul, ul_items
        if not in_ul:
            return ""
        result = f'<ul style="margin: 16px 0; padding: 0; list-style: none;">\n'
        for item in ul_items:
            result += (
                f'  <li style="{s["ul_item"]}">'
                f'<span style="{s["ul_bullet"]}">•</span>'
                f'<span>{process_inline(item, s)}</span></li>\n'
            )
        result += "</ul>\n"
        in_ul = False
        ul_items = []
        return result

    def maybe_insert_section_image(title: str) -> str:
        """在章节前尝试插入配图（仅 with_images 模式）"""
        if not with_images:
            return ""
        if section_char_count < 80:  # 内容太少则不插图
            return ""
        return make_section_image_placeholder(title, s, image_style)

    while i < len(lines):
        line = lines[i]

        # ── 代码块 ──────────────────────────────────────────────────
        if line.strip().startswith("```"):
            if not in_code_block:
                is_copy_block = False
                for k in range(1, 4):
                    prev = lines[i-k].strip() if i >= k else ""
                    if "\U0001f4cb" in prev or "复制发给" in prev:
                        is_copy_block = True
                        break

                html_parts.append(flush_ul())
                in_code_block = True
                code_lang = line.strip()[3:].strip() or "bash"
                code_lines = []
            else:
                code_content = escape_html("\n".join(code_lines))
                if is_copy_block:
                    block = (
                        f'<div style="{s["copy_block_wrap"]}">\n'
                        f'  <div style="{s["copy_block_header"]}">📋 复制发给助手</div>\n'
                        f'  <pre style="{s["copy_block_pre"]}">'
                        f'<code style="{s["code_block_code"]}">{code_content}</code></pre>\n'
                        f'</div>\n'
                    )
                else:
                    block = (
                        f'<div style="{s["code_block_wrap"]}">\n'
                        f'  <div style="{s["code_block_header"]}">{code_lang}</div>\n'
                        f'  <pre style="{s["code_block_pre"]}">'
                        f'<code style="{s["code_block_code"]}">{code_content}</code></pre>\n'
                        f'</div>\n'
                    )
                html_parts.append(block)
                in_code_block = False
                code_lines = []
                is_copy_block = False
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # ── 空行 ──────────────────────────────────────────────────
        if not line.strip():
            html_parts.append(flush_ul())
            i += 1
            continue

        # ── 分割线 ────────────────────────────────────────────────
        if re.match(r'^[-*_]{3,}\s*$', line):
            html_parts.append(flush_ul())
            html_parts.append(f'<div style="{s["divider"]}"></div>\n')
            i += 1
            continue

        # ── Markdown 图片语法 ─────────────────────────────────────
        img_html = process_image_line(line, s)
        if img_html is not None:
            html_parts.append(flush_ul())
            html_parts.append(img_html)
            i += 1
            continue

        # ── H1 ──────────────────────────────────────────────────
        if line.startswith("# "):
            html_parts.append(flush_ul())
            text = process_inline(line[2:].strip(), s)
            html_parts.append(
                f'<h1 style="{s["h1"]}">{text}</h1>\n'
                f'<div style="{s["h1_underline"]}"></div>\n'
            )
            # 封面图：H1 之后插入（仅首次且未禁用）
            if not h1_seen and not no_cover and with_images:
                cover_title = line[2:].strip()
                cover_prompt = f"{cover_title}, {image_style}"
                html_parts.append(
                    f'<!-- [AUTO_IMAGE:COVER] prompt="{cover_prompt}" width=677 height=340 -->\n'
                    f'<figure style="{s["figure"]}">\n'
                    f'  <img src="{DEFAULT_IMAGE_PLACEHOLDER}" alt="{escape_html(cover_title)}"\n'
                    f'       style="{s["img_cover"]}" />\n'
                    f'  <figcaption style="{s["figcaption"]}">▲ 封面图</figcaption>\n'
                    f'</figure>\n'
                )
            h1_seen = True
            section_char_count = 0
            i += 1
            continue

        # ── H2 ──────────────────────────────────────────────────
        if line.startswith("## "):
            html_parts.append(flush_ul())
            # 在新章节开始前，为上一章节插入配图（如内容足够多）
            if with_images and h2_count > 0 and section_char_count >= 80:
                html_parts.append(maybe_insert_section_image(current_section_title))

            section_title_raw = line[3:].strip()
            text = process_inline(section_title_raw, s)
            html_parts.append(f'<h2 style="{s["h2"]}">{text}</h2>\n')

            h2_count += 1
            current_section_title = section_title_raw
            section_char_count = 0
            i += 1
            continue

        # ── H3 ──────────────────────────────────────────────────
        if line.startswith("### "):
            html_parts.append(flush_ul())
            text = process_inline(line[4:].strip(), s)
            html_parts.append(f'<h3 style="{s["h3"]}">{text}</h3>\n')
            i += 1
            continue

        # ── 引用块 ────────────────────────────────────────────────
        if line.startswith("> "):
            html_parts.append(flush_ul())
            text = process_inline(line[2:].strip(), s)
            html_parts.append(
                f'<blockquote style="{s["blockquote"]}">{text}</blockquote>\n'
            )
            section_char_count += len(line)
            i += 1
            continue

        # ── 提示框 ────────────────────────────────────────────────
        if line.startswith("💡") or line.lower().startswith("> 💡"):
            html_parts.append(flush_ul())
            clean = re.sub(r'^>?\s*', '', line).strip()
            text = process_inline(clean, s)
            html_parts.append(
                f'<div style="{s["tip_green"]}">'
                f'<p style="{s["tip_green_text"]}">{text}</p></div>\n'
            )
            section_char_count += len(line)
            i += 1
            continue

        if line.startswith("⚠️") or line.lower().startswith("> ⚠️"):
            html_parts.append(flush_ul())
            clean = re.sub(r'^>?\s*', '', line).strip()
            text = process_inline(clean, s)
            html_parts.append(
                f'<div style="{s["tip_yellow"]}">'
                f'<p style="{s["tip_yellow_text"]}">{text}</p></div>\n'
            )
            section_char_count += len(line)
            i += 1
            continue

        # ── Step N: 步骤 ────────────────────────────────────────
        step_match = re.match(r'^[Ss]tep\s*(\d+)[：:]\s*(.*)', line)
        if step_match:
            html_parts.append(flush_ul())
            num = step_match.group(1)
            title = process_inline(step_match.group(2).strip(), s)
            desc_lines = []
            j = i + 1
            while j < len(lines) and (lines[j].startswith("  ") or lines[j].startswith("\t")):
                desc_lines.append(lines[j].strip())
                j += 1
            desc = process_inline(" ".join(desc_lines), s) if desc_lines else ""
            desc_html = f'<p style="{s["step_desc"]}">{desc}</p>' if desc else ""
            html_parts.append(
                f'<div style="{s["step_wrap"]}">\n'
                f'  <div style="{s["step_num"]}">{num}</div>\n'
                f'  <div style="{s["step_content"]}">\n'
                f'    <p style="{s["step_title"]}">{title}</p>\n'
                f'    {desc_html}\n'
                f'  </div>\n'
                f'</div>\n'
            )
            section_char_count += len(line)
            i = j
            continue

        # ── 无序列表 ─────────────────────────────────────────────
        if re.match(r'^[-*+]\s+', line):
            in_ul = True
            ul_items.append(re.sub(r'^[-*+]\s+', '', line).strip())
            section_char_count += len(line)
            i += 1
            continue

        # ── 有序列表 ─────────────────────────────────────────────
        ol_match = re.match(r'^(\d+)\.\s+(.*)', line)
        if ol_match:
            html_parts.append(flush_ul())
            num = ol_match.group(1)
            text = process_inline(ol_match.group(2).strip(), s)
            html_parts.append(
                f'<p style="font-size: 15px; color: #3d3d3d; line-height: 1.8; '
                f'margin: 0 0 10px; padding-left: 4px;">'
                f'<span style="color: {theme}; font-weight: bold; margin-right: 6px;">{num}.</span>'
                f'{text}</p>\n'
            )
            section_char_count += len(line)
            i += 1
            continue

        # ── 普通段落 ─────────────────────────────────────────────
        html_parts.append(flush_ul())
        text = process_inline(line.strip(), s)
        html_parts.append(f'<p style="{s["p"]}">{text}</p>\n')
        section_char_count += len(line)
        i += 1

    # 处理末尾未关闭的列表
    html_parts.append(flush_ul())

    # 文章末尾：为最后一个章节插图
    if with_images and current_section_title and section_char_count >= 80:
        html_parts.append(maybe_insert_section_image(current_section_title))

    return "".join(html_parts)


def wrap_full_html(content: str, title: str = "文章") -> str:
    """包裹为完整 HTML 文档（用于本地预览）"""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape_html(title)}</title>
</head>
<body style="margin: 0; padding: 20px; background: #f5f5f5;">
<section style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', Arial, sans-serif; font-size: 16px; color: #3d3d3d; line-height: 1.8; padding: 24px 16px; max-width: 677px; margin: 0 auto; word-break: break-word; background: #fff; border-radius: 8px; box-shadow: 0 2px 12px rgba(0,0,0,0.08);">
{content}
</section>
</body>
</html>
"""


def wrap_wechat_html(content: str) -> str:
    """包裹为仅含 section 的微信公众号版本（无 body 外壳）"""
    return (
        f'<section style="font-family: -apple-system, BlinkMacSystemFont, \'PingFang SC\', '
        f'\'Helvetica Neue\', Arial, sans-serif; font-size: 16px; color: #3d3d3d; '
        f'line-height: 1.8; padding: 0 16px; max-width: 677px; margin: 0 auto; word-break: break-word;">\n'
        f'{content}\n'
        f'</section>'
    )


def count_images_in_html(html: str) -> int:
    """统计 HTML 中的图片数量"""
    return len(re.findall(r'<img\s', html))


# ─── 主程序 ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="微信公众号排版转换工具（带图版）- 将 Markdown/纯文字转为公众号 HTML，支持自动配图"
    )
    parser.add_argument("--input", "-i", required=True, help="输入文件路径（.md 或 .txt）")
    parser.add_argument("--output", "-o", default="output.html", help="输出 HTML 文件路径（默认 output.html）")
    parser.add_argument("--title", "-t", default="", help="文章标题（可选）")
    parser.add_argument("--theme", default=DEFAULT_THEME, help=f"主题色（默认 {DEFAULT_THEME}）")
    parser.add_argument("--wechat-only", action="store_true",
                        help="仅输出微信粘贴用的 section 片段，不含 HTML 外壳")
    # ── 图片相关参数 ────────────────────────────────────
    parser.add_argument("--with-images", action="store_true",
                        help="在合适位置自动插入图片占位符（章节配图 + 封面图）")
    parser.add_argument("--image-style", default=DEFAULT_IMAGE_STYLE,
                        help=f"图片风格描述，用于 AI 生成提示词（默认：'{DEFAULT_IMAGE_STYLE}'）")
    parser.add_argument("--no-cover", action="store_true",
                        help="跳过封面图，不在 H1 后插入封面配图")
    args = parser.parse_args()

    # 读取输入
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"错误：找不到文件 {args.input}", file=sys.stderr)
        sys.exit(1)

    md_content = input_path.read_text(encoding="utf-8")
    title = args.title or input_path.stem

    # 转换
    body_html = parse_markdown(
        md_content,
        theme=args.theme,
        with_images=args.with_images,
        image_style=args.image_style,
        no_cover=args.no_cover,
    )

    # 包裹
    if args.wechat_only:
        final_html = wrap_wechat_html(body_html)
    else:
        final_html = wrap_full_html(body_html, title=title)

    # 写出
    output_path = Path(args.output)
    output_path.write_text(final_html, encoding="utf-8")

    img_count = count_images_in_html(final_html)
    print(f"[OK] 转换完成！输出文件：{output_path.resolve()}")
    if img_count > 0:
        print(f"[图片] 共包含 {img_count} 张图片/占位符")
        if args.with_images:
            print(f"[提示] 占位符图片需替换为实际图片后再上传公众号")
            print(f"[提示] 搜索 HTML 中的 <!-- [AUTO_IMAGE] 注释，按 prompt 生成并替换对应图片")


if __name__ == "__main__":
    main()
