# DEV_STATE

## Current Goal
- 在 `.agents/skills/starline-gzh-design` 和 `FreeCodeCampXYG/starline-gzh-design` 维护可直接使用、可核对来源、可规范提交 Issue/PR 的 Starline 微信公众号排版 skill。
- 当前增量目标：把“读者任务优先、整理法则降级”和“关键结构禁止 50% 半宽列”固化为排版流程、组件模板、确定性校验与回归用例。

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
- 首次增强发布已通过 GitHub Pull Request #1 合并到 `main`，合并提交为 `9cdd6d8`；未直接推送或改写默认分支历史。
- GitHub 仓库描述已更新为当前 8 套主题和增强能力，并增加 `agent-skill`、`claude-code`、`codex`、`markdown`、`wechat` 分类标签。
- GitHub Fork 创建时默认关闭的 Issues 功能已显式开启；`bug_report.md`、`feature_request.md` 和 `theme_request.md` 可从新建 Issue 页面选择。
- 本地安装目录已新增 `references/theme-apple-open-course.md`，并在主题索引与自动推荐规则中登记为第 9 套主题。
- 新主题提供课程开场、学习目标、编号章节、四象限、步骤线、来源致谢与作者签名组件；不使用 Apple 品牌资产。
- `SKILL.md` 与 `manifest.json` 的本地版本已更新为 `1.1.0`，中英文 README 已同步主题数量。
- 已将本地版本更新为 `1.2.0`：发布前优先读取项目 `DEV_STATE.md` 的“公众号发布身份”，缺失时一次询问两项，确认后写回并复用。
- 已禁止把作者身份占位符作为可直接发布成品交付；`validate_gzh_html.py` 会把未替换的署名、简介或作者身份占位符判为 ERROR。
- 已同步更新一阶段、两阶段标注格式、回归用例与 `agents/interface.yaml`；全自动模式不能绕过发布身份门槛，明确匿名发布可省略作者介绍区。
- 已将本地版本更新为 `1.3.0`，新增 `references/content-hierarchy.md`：排版前先写读者任务、唯一结果、核心路径和辅助信息四行层级简报。
- 已规定用户说“用二八／STAR／四象限整理 X”时，默认 X 是文章主题、法则是整理手段；只有文章明确讲法则本身时，法则才能进入封面和主章节。
- 已将苹果公开课风的四象限组件由 2×2 半宽 flex 改为四张全宽纵向卡片，五步课程线也改为不依赖 flex 的块级结构。
- 已在 `component_lint.py` 与 `validate_gzh_html.py` 中拦截 `width:50%`／`flex-basis:50%`，避免微信剥离父级 flex 后内容堆在左半屏。
- 已同步更新中英文 README、主题索引、默认 Prompt 和回归用例；真实公众号粘贴结果的证据优先级高于浏览器预览。
- 已把 README 许可证标题改为发布器可识别的标准 `## License`，继续明确继承上游 AGPL-3.0，不改成 MIT。
- 已新增 `evals/trigger_cases.json`，覆盖公众号排版、自动主题、两阶段标注、图床修复与草稿上传，并加入普通网页、PPT、写作和 PDF 笔记等误触发边界。
- 已为 `component_lint.py`、`minify_gzh_html.py`、`upload_image.py`、`wechat_draft.py`、`wrap_preview.py` 补齐 `argparse --help`，保留原有位置参数调用方式。
- 已新增 `tests/test_release_behaviors.py`，固定验证半宽组件拦截、全宽组件放行、HTML 压缩和 5 个公开脚本帮助入口。
- 已用 `starline-meta-skill` 导出 `reports/skill-ir.json` 与通过的 `reports/trigger-eval.json`，满足版本和评估报告一致性门禁。
- 2026-08-16：预览页新增「复制标题」一键复制功能：`wrap_preview.py` 新增 `--title` 参数（建议标题可改、HTML 转义），`assets/preview-template.html` 增加可修改的建议标题顶栏与「复制标题」按钮（保留「复制到公众号」正文复制）；SKILL.md 方向一流程与 README 一键复制说明同步更新。

## Key Decisions
- #6 是与 #7 重复的已关闭 PR，未重复合并；采用包含主题推荐规则的 #7。
- #3、#5、#8、#12、#13 只有 issue 描述，没有可审查的提交，因此没有伪造合并记录或擅自实现不明确需求。
- API 草稿箱、图床和脚注能力继续放在同一个 `gzh-design` skill 中。
- 苹果公开课风用系统蓝、细线与大留白建立层级；来源致谢放在正文完成后、参考资料前，不打断开场且不省略署名。
- Windows 控制台含 emoji 的脚本验证使用 `PYTHONIOENCODING=utf-8`，文件内容按 UTF-8 处理。
- 已将本地目录从 `.agents/skills/gzh-design` 移动为 `.agents/skills/starline-gzh-design`；上游 URL 和 `~/.gzh-design` 图床配置路径保持不变，以兼容已有配置。
- 已补齐 Starline 包元数据：`manifest.json`、`agents/interface.yaml`，并在根 `SKILL.md` 写入 author/version/upstream metadata。
- GitHub Issue 默认不接受空白提交；非主题能力使用独立的 `Feature request` 模板，避免与主题设计需求混杂。
- GitHub 发布使用功能分支和 Pull Request，不直接在默认分支开发；目标仓库固定使用仓库级 `core.autocrlf=false`。
- 发布身份只保存用户确认可公开的署名与简介，不从 Git 邮箱、系统账户或文件信息推断，也不把联系方式和凭证写入公开项目。
- 内容层级的核心顺序固定为“读者任务／核心动作 > 步骤与证据 > 整理法则／来源”；主题组件只能表达这个顺序，不能反转它。
- #8 没有可合并提交，但本次已有真实公众号粘贴截图和可复现的父级 flex／子项半宽失效结构，因此独立实现窄范围兼容规则，不声称合并了上游修复。
- 未全局禁止 `flex-wrap`：其它主题仍用它处理自适应标签；只确定性禁止会导致半屏空白的 50% 固定半宽列，并要求关键关系使用全宽块级结构。
- 本次属于生产故障的定向泛化，不做新的 prior-art 搜索；通过显式反例保留“文章本身讲 STAR 时可把 STAR 作为主主题”的边界。

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
- `references/content-hierarchy.md`
- `references/theme-klein-blue.md`
- `references/theme-apple-open-course.md`
- `references/theme-tech-cobalt.md`
- `references/annotated-format.md`
- `references/common-components.md`
- `references/format-normalize.md`
- `references/eval-cases.md`
- `evals/trigger_cases.json`
- `reports/skill-ir.json`
- `reports/trigger-eval.json`
- `tests/test_release_behaviors.py`
- `scripts/validate_gzh_html.py`
- `scripts/component_lint.py`
- `scripts/extract_docx.py`
- `scripts/wechat_draft.py`
- `scripts/minify_gzh_html.py`
- `scripts/upload_image.py`

## Verification
- 历史远端 `main` 浅克隆验证曾通过 `validate_skill.py`、`compileall` 与全部画廊合规检查；GitHub 仓库 Issues 和 3 个 Issue 模板已启用。
- `wrap_preview.py` 固定使用 LF 输出，避免 `core.autocrlf=false` 仓库中的逐行尾随空白。
- v1.3.0 本地验证：`python -m compileall -q scripts` 通过；`component_lint.py` 为 17/17 个组件库 `ERROR×0、WARN×0`。
- v1.3.0 正反例验证：父级 flex + 子项 `width:50%` 的旧失败结构被 `validate_gzh_html.py` 按预期拦截并返回退出码 1；全宽块级结构返回退出码 0。
- v1.3.0 真实产物验证：`learning-library` 当前公众号正文为 132 处 `span leaf`，新校验器 `ERROR×0、WARN×0`。
- `trigger_eval.py` 对 16 个触发、非触发和相邻场景全部判定正确，`pass_rate=1.0`。
- `python -m unittest discover -s tests -p test_*.py -v` 的 4 项回归测试全部通过。
- `starline-meta-skill/scripts/validate_skill.py .` 通过，`failures=[]`、`warnings=[]`；5 个命令行脚本的 `--help` 均返回退出码 0。
- `manifest.json` 与根 `SKILL.md` 版本均为 `1.3.0`；UTF-8 读取和 JSON 解析通过。

## Known Issues
- `docs/gallery/index.html` 是导航网页，不是公众号正文，不能送入 `validate_gzh_html.py`；文章画廊文件与导航页需分开校验。
- #3、#5、#12、#13 当前仍是无提交 issue；其中 #5 描述不足，#12/#13 需要明确设计方案后再实现。#8 已基于真实粘贴复现独立实现兼容规则，但仍没有可归因的上游提交。
- 本地安装目录不是 Git 工作树；v1.3.0 已完成 GitHub Fork 同步，尚未创建 Release（版本号与发布说明待确认）。

## Failed Approaches

- 未采用“全局禁止 `flex-wrap`”：现有主题把它用于标签自然换行，全面禁用会误伤安全组件。最终规则只拦截 `width/flex-basis:50%`，并把关键矩阵改为全宽块级结构。
- 未把“法则名称一律降级”写成绝对规则：这会误伤真正讲 STAR／二八法则的文章。最终以读者任务是否就是该法则作为边界。
