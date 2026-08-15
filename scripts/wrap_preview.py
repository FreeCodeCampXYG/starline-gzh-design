#!/usr/bin/env python3
"""把已校验的公众号正文片段（纯 <section>）包成带「复制」按钮的浏览器预览页。

用户打开预览页 → 点右上角「复制到公众号」→ 按钮选中并复制里面渲染后的富文本
（等价手动 Ctrl+A/Ctrl+C，样式全保留）→ 到公众号编辑器 Ctrl+V 粘贴即可。

按钮和 JS 只存在于预览外壳里，**不在被复制的 section 内**，所以粘进公众号的
仍是干净合规的正文，不含 <script>/<button>。校验请对原始 section 文件跑
validate_gzh_html.py（本预览页含 script/style，不参与校验）。

用法:
    wrap_preview.py <section.html> [output.html]
    默认输出 <section去扩展名>_预览.html
"""

import argparse
import os


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="把公众号正文片段包装成带复制按钮的浏览器预览页。"
    )
    parser.add_argument("section_html", help="已校验的公众号正文 HTML 片段。")
    parser.add_argument("output_html", nargs="?", help="预览页输出路径。")
    args = parser.parse_args(argv)
    src = args.section_html
    if not os.path.isfile(src):
        print(f"✗ 找不到文件: {src}")
        raise SystemExit(1)

    content = open(src, encoding="utf-8").read().strip()
    tpl_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "assets", "preview-template.html")
    tpl = open(tpl_path, encoding="utf-8").read()

    title = os.path.splitext(os.path.basename(src))[0]
    out_html = tpl.replace("{{TITLE}}", title).replace("<!--GZH_CONTENT-->", content)

    out = args.output_html or os.path.splitext(src)[0] + "_预览.html"
    # 固定使用 LF，避免 Windows 默认 CRLF 在关闭 autocrlf 的仓库中被
    # git diff --check 误判为逐行尾随空白。
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(out_html)
    print(f"✓ 已生成带「复制」按钮的预览页: {out}")
    print("  用浏览器打开它，点右上角「复制到公众号」，再去公众号编辑器 Ctrl/⌘+V 粘贴。")


if __name__ == "__main__":
    main()
