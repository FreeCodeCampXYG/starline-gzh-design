# 贡献指南 · Contributing

欢迎为 `starline-gzh-design` 贡献新主题风格、修复排版问题或改进文档。本项目优先接受可复现、可验证、范围清晰的改动。

## Issue 与 Pull Request 流程

### 提交 Issue

1. 先搜索已有 Issue，确认不是重复问题；不同问题不要合并到同一个 Issue。
2. Bug 请使用 `Bug report` 模板，写清主题、输入格式、最小复现内容、期望结果、实际结果、运行环境和完整校验输出。
3. 新主题请使用 `Theme request` 模板；脚本、输入支持、上传能力等改进请使用 `Feature request` 模板，写清使用场景和可检查的验收标准。
4. 若只是讨论想法，不要先提交无法验证的代码。输入内容应脱敏，不要上传文章原文、个人信息、公众号密钥、Access Token、Cookie 或本地绝对路径中的敏感部分。

### 提交 Pull Request

1. 从最新默认分支创建工作分支，分支名使用 `fix/<主题>`、`feat/<主题>` 或 `docs/<主题>`，不要直接在默认分支开发。
2. 一个 PR 只解决一个主题：一套新主题、一处缺陷、一个工具改进或一组文档改动。跨范围改动请拆分，或在 PR 描述中解释原因。
3. PR 标题用一句话说明“改了什么”；正文必须说明“为什么改、影响哪些文件、如何验证、是否有兼容性风险”，并关联对应 Issue，例如 `Fixes #123`。
4. 每个提交都要有具体的提交主题，并在提交正文或 PR 描述中增加独立的修改说明，避免只有“更新”“修复问题”这类无法追溯的描述。
5. 维护者合并前会检查模板中的验证清单、敏感信息、未提交产物和默认分支保护状态。没有复现输入或验证证据的 PR 可能会被要求补充。

### Windows 编码与 Git 约束

- 固定使用 `core.autocrlf=false`，避免主题 HTML、Markdown、YAML 和示例文件在跨平台提交时发生换行漂移。
- PowerShell 控制台显示可能是 GBK；文件读写必须显式使用 UTF-8。不要把终端里已经乱码的内容复制回源文件。
- 需要展示中文命令输出时，可以单独处理控制台编码；不要用改变文件编码的方式解决显示问题。
- 提交前检查 `git diff --check`，并确认新增文件实际以 UTF-8 保存。

## 项目结构速览

- `SKILL.md` — 排版工作流主文档（Agent 入口）
- `references/` — 8 套主题组件库 + 通用增量库 + 主题索引 + 主题生成器 + 触发用例
- `scripts/` — 校验、HTML 压缩、公众号草稿上传和本地图片图床上传脚本
- `assets/` — 演示输入文章
- `docs/gallery/` — 主题风格的浏览器预览

## 可验证循环（改动前后都要跑）

任何改动组件库或 SKILL 后，按这个双关卡闭环自检，两关全绿才提 PR：

```bash
# 语法关：检查脚本是否能被 Python 编译
python -m compileall -q scripts

# 源头关：扫所有组件库的 HTML 块，查大空白 / 正文虚线框 / 平台禁用项
python scripts/component_lint.py .

# 产物关：用改动后的 skill 排版 assets/sample-article.md，再校验产物
python scripts/validate_gzh_html.py <生成的.html>
```

- `component_lint.py` 须 **0 ERROR**
- `validate_gzh_html.py` 须 **0 ERROR、半角标点 0 WARN**
- `compileall` 不得产生语法错误；提交前还要运行 `git diff --check`。
- 改动公众号 HTML 或主题时，建议在公众号编辑器和移动端预览各检查一次，确认粘贴后样式、图片、代码块和长标题没有异常。

细节见 `references/eval-cases.md` 的「维护 · 可验证循环」一节。

## 新增一套主题风格

1. 照 `references/theme-red-white.md` 的结构，新建一份 `references/theme-{你的英文标识}.md`（如 `theme-ocean-breeze.md`；内含设计变量 + 各组件 HTML + 模板骨架 + 映射规则，标题里的风格显示名可用中文）。
2. 硬性约束：所有样式内联、文字用 `<span leaf="">` 包裹、禁 `div/class/id/style/grid/position/var/@media`、正文强调用左竖条或小标签而**非四周虚线框**、代码块用「每行一个 `<p>`」而**非 `white-space:pre`**。
3. 在 `references/theme-index.md` 登记（主色 + 适用场景 + 组件库文件 + 正文下划线 CSS）。
4. 跑可验证循环，两关全绿。
5. 提 PR，附上用 `assets/sample-article.md` 生成的预览 HTML。

## 提交规范

- 一个 PR 只做一件事（一套新主题 / 一处修复 / 一处文档）。
- commit 信息说清「改了什么 + 为什么」，并在 PR 中保留独立的修改说明。
- 不要提交本地排版产物（`.gitignore` 已忽略 `*_排版_*.html`）。
- 不要提交密钥、令牌、Cookie、个人文章原文或仅用于本机的绝对路径。
- PR 合并前，维护者应确认 Issue 已关联、验证命令已通过、文档已同步，且没有未说明的破坏性变更。

## 修改说明模板

可直接复制到 PR 描述中：

```text
修改目的：
修改内容：
影响范围：
关联 Issue：Fixes #
验证命令及结果：
兼容性/破坏性变更：无
未提交的本地文件或敏感信息：已确认无
```
