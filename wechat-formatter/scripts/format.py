#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号排版转换脚本
将 Markdown 或纯文本转换为可直接粘贴到微信公众号编辑器的 HTML

用法：
    python format.py --input article.md --output output.html
    python format.py --input article.txt --title "我的文章" --theme "#07c160"
"""

import re
import sys
import argparse
from pathlib import Path


# ─── 主题色配置 ────────────────────────────────────────────────────────────────
DEFAULT_THEME = "#07c160"
DEFAULT_THEME_LIGHT = "#e8f5ef"
DEFAULT_THEME_BORDER = "#b7dfc8"


# ─── 样式常量 ──────────────────────────────────────────────────────────────────
FONT_FAMILY = "-apple-system, BlinkMacSystemFont, 'PingFang SC', 'Helvetica Neue', Arial, sans-serif"
MONO_FAMILY = "'Menlo', 'Monaco', 'Consolas', monospace"


def build_styles(theme: str = DEFAULT_THEME) -> dict:
    """根据主题色构建样式字典"""
    # 计算浅色版本（简化处理：固定用预设浅色）
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
    }


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


def parse_markdown(md: str, theme: str = DEFAULT_THEME) -> str:
    """将 Markdown 转换为微信公众号 HTML"""
    s = build_styles(theme)
    lines = md.split("\n")
    html_parts = []
    
    i = 0
    step_counter = 0  # 用于 Step N 自动编号
    in_code_block = False
    code_lang = ""
    code_lines = []
    is_copy_block = False
    in_ul = False
    ul_items = []

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

    while i < len(lines):
        line = lines[i]

        # ── 代码块 ──────────────────────────────────────────────────
        if line.strip().startswith("```"):
            if not in_code_block:
                # 检查前几行（最多3行）是否包含 📋 复制标记
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
                # 关闭代码块
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

        # ── H1 ──────────────────────────────────────────────────
        if line.startswith("# "):
            html_parts.append(flush_ul())
            text = process_inline(line[2:].strip(), s)
            html_parts.append(
                f'<h1 style="{s["h1"]}">{text}</h1>\n'
                f'<div style="{s["h1_underline"]}"></div>\n'
            )
            i += 1
            continue

        # ── H2 ──────────────────────────────────────────────────
        if line.startswith("## "):
            html_parts.append(flush_ul())
            text = process_inline(line[3:].strip(), s)
            html_parts.append(f'<h2 style="{s["h2"]}">{text}</h2>\n')
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
            i += 1
            continue

        # ── 提示框：💡 开头为绿色提示，⚠️ 开头为黄色警告 ─────────────
        if line.startswith("💡") or line.lower().startswith("> 💡"):
            html_parts.append(flush_ul())
            clean = re.sub(r'^>?\s*', '', line).strip()
            text = process_inline(clean, s)
            html_parts.append(
                f'<div style="{s["tip_green"]}">'
                f'<p style="{s["tip_green_text"]}">{text}</p></div>\n'
            )
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
            i += 1
            continue

        # ── Step N: 步骤 ────────────────────────────────────────
        step_match = re.match(r'^[Ss]tep\s*(\d+)[：:]\s*(.*)', line)
        if step_match:
            html_parts.append(flush_ul())
            num = step_match.group(1)
            title = process_inline(step_match.group(2).strip(), s)
            # 收集后续缩进行作为步骤描述
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
            i = j
            continue

        # ── 无序列表 ─────────────────────────────────────────────
        if re.match(r'^[-*+]\s+', line):
            in_ul = True
            ul_items.append(re.sub(r'^[-*+]\s+', '', line).strip())
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
            i += 1
            continue

        # ── 普通段落 ─────────────────────────────────────────────
        html_parts.append(flush_ul())
        text = process_inline(line.strip(), s)
        html_parts.append(f'<p style="{s["p"]}">{text}</p>\n')
        i += 1

    # 处理末尾未关闭的列表
    html_parts.append(flush_ul())

    return "".join(html_parts)


def wrap_full_html(content: str, title: str = "文章") -> str:
    """包裹为完整 HTML 文档"""
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


# ─── 主程序 ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="微信公众号排版转换工具 - 将 Markdown/纯文字转为公众号 HTML"
    )
    parser.add_argument("--input", "-i", required=True, help="输入文件路径（.md 或 .txt）")
    parser.add_argument("--output", "-o", default="output.html", help="输出 HTML 文件路径（默认 output.html）")
    parser.add_argument("--title", "-t", default="", help="文章标题（可选）")
    parser.add_argument("--theme", default=DEFAULT_THEME, help=f"主题色（默认 {DEFAULT_THEME}）")
    parser.add_argument("--wechat-only", action="store_true", help="仅输出微信粘贴用的 section 片段，不含 HTML 外壳")
    args = parser.parse_args()

    # 读取输入
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"错误：找不到文件 {args.input}", file=sys.stderr)
        sys.exit(1)

    md_content = input_path.read_text(encoding="utf-8")
    title = args.title or input_path.stem

    # 转换
    body_html = parse_markdown(md_content, theme=args.theme)

    # 包裹
    if args.wechat_only:
        final_html = wrap_wechat_html(body_html)
    else:
        final_html = wrap_full_html(body_html, title=title)

    # 写出
    output_path = Path(args.output)
    output_path.write_text(final_html, encoding="utf-8")
    print(f"[OK] 转换完成！输出文件：{output_path.resolve()}")


if __name__ == "__main__":
    main()
