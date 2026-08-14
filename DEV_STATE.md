# DEV_STATE

## Current Goal
- 在 `.agents/skills/starline-gzh-design` 和 `FreeCodeCampXYG/starline-gzh-design` 维护可直接使用、可核对来源、可规范提交 Issue/PR 的 Starline 微信公众号排版 skill。

## Completed Work
- 已安装 `isjiamu/gzh-design-skill` 基础版，并迁移为本地 `name: starline-gzh-design`。
- 已合并 fork 的 API 草稿箱、HTML 压缩和本地图片图床能力：`wechat_draft.py`、`minify_gzh_html.py`、`upload_image.py`、`references/image-host.md`。
- 已合并 PR #11：Markdown 超链接转正文脚注和文末参考资料，正文不保留可点击外链。
- 已合并 issue/PR 关联提交：
  - #1：组件 lint 的虚线边框修复和橄榄手记居中修复。
  - #2：外层背景丢失规则和 HTML 背景校验 warning。
  - #4：`--annotate` 两阶段排版和 `references/annotated-format.md`。
  - #7：克莱因蓝艺术展册主题。
  - #10：科技钴蓝主题和画廊预览。
  - #15：DOCX 表格首行包含转义竖线时的列数修复（关联 #14）。
- 已修正合并后的文档数量：实际为 8 套主题；仓库当前提供 7 套主题的本地画廊 HTML，克莱因蓝已注册但未随 #7 提供画廊文件。
- 已扩充 `README.md` 的 Starline 修改说明、验证命令、自然语言使用示例、当前边界和故障排查。
- 已优化 Bug、主题建议、功能建议和 Pull Request 模板，补齐最小复现、环境、验证结果、关联 Issue、兼容风险、敏感信息和发布前检查。
- 已扩充 `CONTRIBUTING.md`，明确 Issue 到 PR 的协作流程、分支命名、独立修改说明、`core.autocrlf=false` 和 Windows UTF-8 规则。
- 已从 `isjiamu/gzh-design-skill` 创建公开 Fork `FreeCodeCampXYG/starline-gzh-design`，保留上游关系和 `main` 默认分支。
- README 的安装、克隆和更新命令已切换到 Starline Fork；上游署名、灵感来源和上游 Release 图片链接继续保留。

## Key Decisions
- #6 是与 #7 重复的已关闭 PR，未重复合并；采用包含主题推荐规则的 #7。
- #3、#5、#8、#12、#13 只有 issue 描述，没有可审查的提交，因此没有伪造合并记录或擅自实现不明确需求。
- API 草稿箱、图床和脚注能力继续放在同一个 `gzh-design` skill 中。
- Windows 控制台含 emoji 的脚本验证使用 `PYTHONIOENCODING=utf-8`，文件内容按 UTF-8 处理。
- 已将本地目录从 `.agents/skills/gzh-design` 移动为 `.agents/skills/starline-gzh-design`；上游 URL 和 `~/.gzh-design` 图床配置路径保持不变，以兼容已有配置。
- 已补齐 Starline 包元数据：`manifest.json`、`agents/interface.yaml`，并在根 `SKILL.md` 写入 author/version/upstream metadata。
- GitHub Issue 默认不接受空白提交；非主题能力使用独立的 `Feature request` 模板，避免与主题设计需求混杂。
- GitHub 发布使用功能分支和 Pull Request，不直接在默认分支开发；目标仓库固定使用仓库级 `core.autocrlf=false`。

## Core Files
- `SKILL.md`
- `manifest.json`
- `agents/interface.yaml`
- `README.md`
- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/theme_request.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `references/theme-index.md`
- `references/theme-klein-blue.md`
- `references/theme-tech-cobalt.md`
- `references/annotated-format.md`
- `references/common-components.md`
- `references/format-normalize.md`
- `references/eval-cases.md`
- `scripts/validate_gzh_html.py`
- `scripts/extract_docx.py`
- `scripts/wechat_draft.py`
- `scripts/minify_gzh_html.py`
- `scripts/upload_image.py`

## Verification
- 临时合并仓库：`python -m compileall -q scripts` 通过。
- 临时合并仓库：`PYTHONIOENCODING=utf-8 python scripts/component_lint.py .` 通过，15/15 个组件库 `ERROR×0、WARN×0`。
- 临时合并仓库：合并提交范围 `git diff --check` 通过。
- 临时合并仓库：7 个文章画廊 HTML 通过 `validate_gzh_html.py`，ERROR/WARN 均为 0。
- 安装目录同步后已重新执行：`python -m compileall -q scripts` 通过；`component_lint.py` 为 15/15 个组件库 `ERROR×0、WARN×0`；7 个文章画廊 HTML 的 `validate_gzh_html.py` 均为 ERROR/WARN 0；源仓库与安装目录文件哈希一致（排除 DEV_STATE、`.git`、缓存文件）。
- Starline 包门禁：`validate_skill.py .` 通过，`failures=[]`。
- 本次文档和模板更新后重新验证：`python -m compileall -q scripts` 通过；`component_lint.py` 为 15/15 个组件库 `ERROR×0、WARN×0`；7 个文章画廊 HTML 全部合规。
- 本次文档和模板更新后 `validate_skill.py .` 继续通过；README 的自然语言示例、验证命令和故障排查提醒均已消除。
- 准备推送的 Git 工作树已重新执行全部门禁：`compileall` 通过；15/15 个组件库 `ERROR×0、WARN×0`；7 个文章画廊 HTML 全部合规；`validate_skill.py` 为 `ok=true`；`git diff --check` 通过。

## Known Issues
- `docs/gallery/index.html` 是导航网页，不是公众号正文，不能送入 `validate_gzh_html.py`；文章画廊文件与导航页需分开校验。
- #3、#5、#8、#12、#13 当前仍是无提交 issue；其中 #5 描述不足，#8 涉及平台红线下的移动适配策略，#12/#13 需要明确设计方案后再实现。
- `validate_skill.py` 仍提示缺少机器化 `evals/trigger_cases.json`，以及 5 个脚本缺少 argparse 帮助或内部模块标记；当前为本地 Scaffold 迁移，不阻塞使用。
- 安装目录本身不是 Git 工作树；Git 差异检查、提交和远端同步在工作区的发布工作树中执行。
- 当前尚未创建版本化 Release；首个正式 Release 应在后续确认版本号和发布说明后单独执行。
