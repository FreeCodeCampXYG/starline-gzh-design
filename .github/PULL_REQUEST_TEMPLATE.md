## 这个 PR 做了什么

（一句话说清：新增 X 主题 / 修复 X 问题 / 改进 X 文档）

## 关联 Issue

Fixes #

## 修改说明

### 修改目的

### 修改内容与影响范围

### 兼容性与风险

（是否影响现有主题、输入格式、公众号粘贴结果、API 配置或脚本参数？没有请写“无”。）

## 可验证循环自检（必填）

- [ ] 已从最新默认分支创建工作分支，未直接修改默认分支
- [ ] `python -m compileall -q scripts` → 通过
- [ ] `python scripts/component_lint.py .` → 0 ERROR、0 WARN
- [ ] `python scripts/validate_gzh_html.py <产物>` → 0 ERROR、半角 0 WARN
- [ ] `git diff --check` → 通过
- [ ] 若新增/改动主题，已在 `references/theme-index.md` 登记
- [ ] 未提交本地排版产物（`*_排版_*.html`）
- [ ] 未提交密钥、Token、Cookie、个人文章原文或其他敏感信息
- [ ] 已同步更新 README / `CONTRIBUTING.md`（如行为或流程有变化）

## 预览

（附上用 `assets/sample-article.md` 生成的产物截图或 HTML；涉及样式时请补充公众号编辑器或移动端预览结果。）

## 提交记录

- [ ] commit 主题已说明“改了什么”
- [ ] PR 描述已说明“为什么改”和“如何验证”
